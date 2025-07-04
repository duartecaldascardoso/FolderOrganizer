New ideas for the project
- Add a way to use the project via the command line (similar to Rust project damn)
- Add new usages by having argparse to parse new arguments
- Organize the folders either by where the script is invoked or by where the user says so via a path
- Add safeguards to make sure that the user does not kill his computer 

Some ideas:
User should input the sub-commands as a chain of commands. Example:

```
clean -a -d -f 
```

With that command we organize the folders by:
- -a is used to order contents alphabetically
- -d is used to order the contents by date
- -f is used to order the contents by file type

If we want to organize the contents using the AI agent we must:
- use the sub-command `-ai` that will use the AI agent to organize the files
- have an API key defined in the environment variable `AI_API_KEY`

The AI agent will be implemented as a graph, with nodes for handling with different types of prompts and directory structures.

This can be based on:
- complexity
- number of files
- file types
- file sizes

When command are used alone they have different impacts then when used within a chain. Example:
If the user uses `-a` alone it will order the files alphabetically, but if used in a chain with `-d` it will order the files alphabetically within each date.
