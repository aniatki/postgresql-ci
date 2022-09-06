from unittest import result
import psycopg2


# connect to db
connection = psycopg2.connect(database="chinook")


# build a cursor object of the database
cursor = connection.cursor()


# Query 1
# cursor.execute('SELECT * FROM "Artist"')


# Query 2
# cursor.execute('SELECT "Name" FROM "Artist"')


# Query 3
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])


# Query 4
cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])


# fetch the results
results = cursor.fetchall()


# fetch the result (single)
# results = cursor.fetchone()


# close the connection
connection.close()


for result in results:
    print(result)
