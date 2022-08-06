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
    state = str(argv[4])
    query = """SELECT cities.name
            FROM cities
            JOIN states ON cities.state_id = states.id
            WHERE states.name=%s
            ORDER BY cities.id ASC"""
    cur.execute(query, (state,))
    # Después de ejecutar cualquier declaración SELECT se necesita mostrar los
    rows = cur.fetchall()
    print(", ".join(i[0] for i in rows))
    # Close all cursors
    cur.close()
    # Close all databases
    db.close()
