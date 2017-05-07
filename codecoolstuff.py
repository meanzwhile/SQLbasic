import psycopg2


def first(cur):
    cur.execute("""SELECT first_name, last_name FROM mentors;""")
    rows = cur.fetchall()
    for element in rows:
        print(element[0] + " " + element[1])


def main():
    try:
        conn = psycopg2.connect("dbname='peter' user='peter' host='localhost' password='korpeter'")
        conn.autocommit = True
        cur = conn.cursor()

    except Exception as e:
        print("Can't connect. Invalid dbname, user or password.")
        print(e)

    first(cur)

if __name__ == '__main__':
    main()
