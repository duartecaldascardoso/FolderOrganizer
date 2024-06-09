import os
import shutil

# Idea of the python script: Used to clean all of the folders from the system (in this case a macbook) - will work for any machine as long as the paths are right
# The files will be joined together according to the file type (from a subselected few, if not in the intended ones, will be moved to a misc folder)
# Step 1 -> Verify if the folder already contains the subfolders created (related to each file type)
# Step 2 -> If folder types are not created, then create all of the needed subfolders
# Step 3 -> List all of the file types (so that the users knows what is happening)
# Step 4 -> Move all of the files into the correct destination folder 
# Step 5 -> Show the user where the changes were made and inform of success

path = "INPUT YOUR PATH HERE"
destination = "INPUT YOUR DESTINATION PATH HERE"
enumerate_fileTypes = [".mp3", ".mp4", ".exe", ".docx", ".txt", ".pdf", ".png", ".zip", ".epub"] #feel free to add more file types to this list
MISC_FOLDER_NAME = "misc"

# Verifying if the folders are already created and creating them if not
for file_type in enumerate_fileTypes:
    os.makedirs(os.path.join(destination, file_type[1:]), exist_ok=True)

# Creating a folder type for misc files (ones that are not in the list above)
os.makedirs(os.path.join(destination, MISC_FOLDER_NAME), exist_ok=True)

def get_file_types(directory):
    file_types = set()
    for file in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, file)):
            _, ext = os.path.splitext(file)
            file_types.add(ext)
    return file_types

print("All format files in the folder:")
file_types = get_file_types(path)
print(file_types)      

def verify_if_file_exists(src, dst):
    if not os.path.exists(dst):
        shutil.move(src, dst)
    else:
        print(f"File {dst} already exists. Will not be added again.")

# Move files to the appropriate destination folder
for file in os.listdir(path):
    full_file_path = os.path.join(path, file)
    if os.path.isfile(full_file_path):
        moved = False
        for file_type in enumerate_fileTypes:
            if file.endswith(file_type):
                destination_path = os.path.join(destination, file_type[1:], file)
                verify_if_file_exists(full_file_path, destination_path)
                moved = True
                break
        if not moved:
            destination_path = os.path.join(destination, MISC_FOLDER_NAME, file)
            verify_if_file_exists(full_file_path, destination_path)

print(f"The files from the folder {path} have been moved to a new folder according to their file type.")


