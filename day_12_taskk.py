import mysql.connector as mysql

pythonDataTypes = [
    ("INT", 1),
    ("FLOAT", "7.5"),
    ("COMPLEX", "2+5j"),
    ("STRING", "BestEnlist Python Development"),
    ("LIST", "[1, 2, 3, 4, 5]"),
    ("TUPLE", "(1, 2, 3, 4, 5)"),
    ("BOLLEAN", "True"),
    ("SET", "{3,8,9,5}"),
    ("DICTIONARY", "{'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}")
]

conn = mysql.connect(host="localhost", user="root",
                     password="", database="bepythondb", port="3308")

cursor = conn.cursor()

insert_query = "INSERT INTO datatypes(datatype,example) VALUES(%s, %s)"

cursor.executemany(insert_query, pythonDataTypes)

conn.commit()

if cursor:
    print("Data inserted successfully")
    select_query = "SELECT * FROM datatypes"
    cursor.execute(select_query)
    for data in cursor:
        print(data)
else:
    print("Error")

conn.close()