# PP11
# group members: Xin Zeng, Katrina Gonzalez, Hanwen Zhang

import sqlite3

is_first = True
all_candidates = []
for line in open('candidates.txt'):
    if is_first: 
        is_first = False; 
        pass
    else:
        # Split on delimiter ("|")
        # Need to trim the newline
        line = line.rstrip()
        candidate_stats = line.split('|')
        all_candidates.append(candidate_stats)

#print(all_candidates)

db = sqlite3.connect('test_db.sqlite') # Create a connection to the database
cursor = db.cursor() # https://www.python.org/dev/peps/pep-0249/#cursor-objects
cursor.execute("DROP TABLE IF EXISTS candidates") # Convenient in case you want to start over
cursor.execute("DROP TABLE IF EXISTS contributors") # Convenient in case you want to start over

cursor.execute('''CREATE TABLE candidates (
               id INTEGER PRIMARY KEY NOT NULL, 
               first_name TEXT, 
               last_name TEXT, 
               middle_init TEXT, 
               party TEXT NOT NULL)''')

db.commit() # Commit changes to the database

for cand in all_candidates:
    cursor.execute('''INSERT INTO candidates
               (id, first_name, last_name, middle_init, party)
               VALUES (?, ?, ?, ?, ?)''', 
                (cand[0], cand[1], cand[2], cand[3], cand[4]))
db.commit()

cursor.execute("SELECT * FROM candidates")
for i in cursor:
    print(i)