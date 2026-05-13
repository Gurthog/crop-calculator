# git init
Goal: Build an application that calculates and visualizes data relating to crops in Stardew Valley.

I want to practice in python, so that's what I'll use.
My work has all been in web frameworks lately, so I want to build something outside of the web ecosystem.

At the onset, I'm thinking of using Tkinter and matplotlib. Pandas seems like a natural choice for a data application, but since this is practice, instead of asking "how do I do this in pandas" I want to practice using the language itself.

# First Steps
Before I can have a visual or a window with any purpose, I need data. It'll run the whole show, so lets figure it out first.

- [ ] Decide how to store and load crop data

I will need to store the data somewhere. I want to avoid using binary files like Excel or SQLite since git can't track the changes being made, and they aren't readable on the web.
- A CSV will let me edit the data in a spreadsheet application but still avoid an xlsx binary.
- Hardcoded python objects seem heavy handed and harder to edit and update than a spreadsheet.
- Other file formats like TOML and JSON are options, but share the maintainence woes of hardcoded objects.

To start, I think I'll store crop data in a csv file with a header row for readability. I'll create a class to represent one crop, and at startup I'll parse the csv into instances of the class for the rest of the program to use.

Next: [hydrating crops](2_hydrating-crops.md)

