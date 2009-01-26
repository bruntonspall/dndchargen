Dungeons and Dragons 4ed Character Generator
============================================

Design
======

There is a Character, each character has a Race and a Class, along with a power selection, feat selection, skill selection and various other miscellaneous choices made.
To produce a character sheet, the application must take the basic statistics, and apply the effects from race, feat, class, producing a character sheet that shows all of the continuous powers.
Then the application uses the powers to demonstrate the number of options the character has in a given turn.

Installing
==========
Create a mysql user called dndchargen, password dndchargen and give it rights to a schema called dndchargen.
run 'python manage.py syncdb' to create the database and python manage.py runserver to start up a server on port 8000
The database must be populated using the django admin tools under localhost:8000/admin
Finally a character can be created using the django admin tools, and the character sheet displayed on http://localhost:8000/character/<name>

