#!/usr/bin/python3
"""
Write a script that lists all states from the database hbtn_0e_0_usa:
"""

import MySQLdb
from sys import argv
if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3])
# crear un objeto de cursor.
cur = db.cursor()
# objeto de cursor y llamar a la función 'ejecutar'.
# La función de ejecución requiere un parámetro, la consulta.
query = """SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC"""
cur.execute(query,)
# Después de ejecutar cualquier declaración SELECT se necesita mostrar los res
rows = cur.fetchall()
for row in rows:
    print(row)
# Close all cursors
cur.close()
# Close all databases
db.close()
