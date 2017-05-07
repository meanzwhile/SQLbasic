import psycopg2

try:
    conn = psycopg2.connect("dbname='peter' user='peter' host='localhost' password='korpeter'")
    conn.autocommit = True
    cur = conn.cursor()

except Exception as e:
    print("Can't connect. Invalid dbname, user or password.")
    print(e)

cur.execute("""SELECT first_name, last_name FROM mentors;""")
rows = cur.fetchall()
for element in rows:
    print(element)
