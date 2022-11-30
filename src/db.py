# Learning SQLite syntax
# None of this is relevant to the classes

import sqlite3

# Connect to an on-disk database
connection = sqlite3.connect("./tutorial.db")

# Create and return a cursor
cursor = connection.cursor()

# Create a 'movie' table
cursor.execute("DROP TABLE movie")
cursor.execute("CREATE TABLE movie(title, year, score)")

# Select the 'movie' database
print("SELECT name FROM sqlite_master")
result = cursor.execute("SELECT name FROM sqlite_master")
print(result.fetchone())

# Insert two movies
print("Inserting movies...")
cursor.execute("""
    INSERT INTO movie VALUES
        ('Monty Python and the Holy Grail', 1975, 8.2),
        ('And Now for Something Completely Different', 1971, 7.5)
""")
# And commit the transaction
connection.commit()

# Check that the data was inserted
scoreResult = cursor.execute("SELECT score FROM movie")
print(scoreResult.fetchall())

data = [
    ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
    ("Monty Python's The Meaning of Life", 1983, 7.5),
    ("Monty Python's Life of Brian", 1979, 8.0),
]
cursor.executemany("INSERT INTO movie VALUES(?, ?, ?)", data)
connection.commit()  # Remember to commit the transaction after executing INSERT.

for row in cursor.execute("SELECT year, title FROM movie ORDER BY year"):
    print(row)

# Close connection to DB file
connection.close()

# Test DB is persisted to disk
newConnection = sqlite3.connect("./tutorial.db")
newCursor = newConnection.cursor()
newResult = newCursor.execute("SELECT title FROM movie")
print(newResult.fetchall())
newConnection.close()