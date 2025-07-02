import asyncio
import os
import textwrap
from pathlib import Path


from langgraph.graph import StateGraph, START

from folder_cleaner.organizer_graph.schemas.directory_summary import DirectorySummary
from folder_cleaner.organizer_graph.state import OrganizerState, InputOrganizerState


async def _explore_directory_content(state: InputOrganizerState):
    """Explore the folder and extract high-level structure information."""

    root_path = Path(state["path"])
    file_extensions = []
    subfolder_depths = []
    total_files = 0
    total_directories = 0

    for directory_path, directory_names, filenames in os.walk(root_path):
        total_files += len(filenames)
        total_directories += len(directory_names)


        for f in filenames:
            ext = Path(f).suffix.lower()
            if ext:
                file_extensions.append(ext)

        depth = len(Path(directory_path).relative_to(root_path).parts)
        subfolder_depths.append(depth)

    file_type_frequency: dict[str, int] = {}

    for extension in file_extensions:
        if extension in file_type_frequency:
            file_type_frequency[extension] += 1
        else:
            file_type_frequency[extension] = 1

    five_most_predominant_extensions = sorted(file_type_frequency.items(), key=lambda x: x[1], reverse=True)[:5]
    predominant_file_types = {extension: count for extension, count in five_most_predominant_extensions}
    file_names = os.listdir(root_path)

    directory_summary = DirectorySummary(
        total_files=total_files,
        total_directories=total_directories,
        five_most_predominant_extensions=predominant_file_types,
        subfolder_depths=subfolder_depths,
        file_names=file_names,
    )

    # DO NOT EXECUTE THIS SCRIPT WITHOUT BEING FOR TESTING PURPOSES ONLY
    cleaning_script = textwrap.dedent("""\
        import os
        import shutil
        from datetime import datetime
        from pathlib import Path

        def organize_files_by_date_and_type(base_path="."):
            base_path = Path(base_path).resolve()
            target_root = base_path / "organized"

            for root, _, files in os.walk(base_path):
                if target_root in Path(root).parents or Path(root) == target_root:
                    continue

                for file in files:
                    file_path = Path(root) / file
                    if not file_path.is_file():
                        continue

                    mtime = datetime.fromtimestamp(file_path.stat().st_mtime)
                    year = f"{mtime.year:04d}"
                    month = f"{mtime.month:02d}"
                    day = f"{mtime.day:02d}"
                    ext = file_path.suffix[1:] if file_path.suffix else "no_ext"
                    target_dir = target_root / year / month / day / ext
                    target_dir.mkdir(parents=True, exist_ok=True)
                    target_path = target_dir / file
                    shutil.move(str(file_path), str(target_path))
                    print(f"Moved: {file_path} → {target_path}")

        organize_files_by_date_and_type()
    """)

    exec(cleaning_script, {})

    return {"directory_summary": directory_summary}





# Builder configuration of the graph
builder = StateGraph(OrganizerState)

# Nodes from the graph
builder.add_node("explore_directory_content", _explore_directory_content)

# Edges from the graph
builder.add_edge(START, "explore_directory_content")

graph = builder.compile()


# Main method to run the graph in testing mode
async def main():

    current_path = Path(__file__).parent.resolve()
    # Create initial state
    initial_state = InputOrganizerState(path=current_path,user_indication="Create a script which will organize files by date and  type", user_flags=["-f", "-d"])

    # Run the graph
    result = await graph.ainvoke(initial_state)

    # Print the summary result
    print("\n--- Directory Summary ---")
    print(result.directory_summary.json(indent=2))


if __name__ == "__main__":
    asyncio.run(main())