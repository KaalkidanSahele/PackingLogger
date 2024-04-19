**MOTIVATION**

As the description for this repo says, I'm currently packing to go home for the Chrristmas holidays. 
I have a lot to pack and making an extensive list in the notes section of my phone is inefficient and unorganised.

This is a simple Python database (made using sqlite3) to log everything I'm packing. The system uses tkinter for a simple GUI (and threading to allow for terminal inputs while the GUI is running).

**VERSIONS**
Python 3.8+
SQLite3 module version: 2.6.0
SQLite database version: 3.43.1

**COMMANDS**

When running the file, the program has 3 options:

Insert:

<p float="left">
  <img src="./terminal.JPG" width="750" />
  <img src="./gui.JPG" width="750" /> 
</p>

Update:

<p float="left">
First select the item whose status you'd like to update.
  <img src="./GUI(update1).JPG" width="750" />
Change the status via the message box
  <img src="./GUI(update2).JPG" width="750" />
Pressing OK immediately updates the status in the database
  <img src="./GUI(update3).JPG" width="750" />
</p>

Delete:

<p float="left">
First select the item whose status you'd like to delete.
  <img src="./GUI(delete1).JPG" width="750" />
A warning message box is shown.
  <img src="./GUI(delete2).JPG" width="750" />
Pressing OK immediately deletes the item in the database and this is seen in the terminal.
  <img src="./GUI(delete3).JPG" width="750" />
</p>

For both delete and update, if an item is not selected, a message box saying that an item has not been selected.

Query:

<p float="left">
Pressing query allows you to search for items. You can query by any column - name, catergoy, or status
  <img src="./GUI(query1).JPG" width="750" />
Pressing OK shows the rows matching the query
  <img src="./GUI(query2).JPG" width="750" />
Pressing refresh return the database back to its initial view
  <img src="./GUI(query3).JPG" width="750" />
</p>

