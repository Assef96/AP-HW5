import sqlite3

connect = sqlite3.connect('database.db')
connect.execute("DROP TABLE users")
connect.commit()

connect.execute("DROP TABLE locations")
connect.commit()

connect.execute("""CREATE TABLE users (id integer primary key autoincrement, name text,
phone integer, username text, password text)""")

connect.execute("""CREATE TABLE locations (id integer primary key autoincrement, user_id
integer, lat integer, lon integer)""")