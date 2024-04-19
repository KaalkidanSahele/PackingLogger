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

**INSERT**

<p float="left">
  <img src="./images/terminal.JPG" width="750" />
  <img src="./images/gui.JPG" width="750" /> 
</p>

**UPDATE**

<p float="left">
First select the item whose status you'd like to update.
  <img src="./images/GUI(update1).JPG" width="750" />
</br>
Change the status via the message box
  <img src="./images/GUI(update2).JPG" width="750" />
</br>
Pressing OK immediately updates the status in the database
  <img src="./images/GUI(update3).JPG" width="750" />
</p>

**DELETE**

<p float="left">
First select the item whose status you'd like to delete.
  <img src="./images/GUI(delete).JPG" width="750" />
</br>
A warning message box is shown.
  <img src="./images/GUI(delete2).JPG" width="750" />
Pressing OK immediately deletes the item in the database and this is seen in the terminal.
</br>
  <img src="./images/GUI(delete3).JPG" width="750" />
</p>

For both delete and update, if an item is not selected, a message box saying that an item has not been selected.

**QUERY**

<p float="left">
</br>
Pressing query allows you to search for items. You can query by any column - name, catergoy, or status
  <img src="./images/GUI(query1).JPG" width="750" />
</br>
Pressing OK shows the rows matching the query
  <img src="./images/GUI(query2).JPG" width="750" />
</br>
Pressing refresh return the database back to its initial view
  <img src="./images/GUI(refresh).JPG" width="750" />
</p>

