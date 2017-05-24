import psycopg2


def database_handler(command):
    conn = psycopg2.connect("dbname='sql_assignment' user=''")
    cur = conn.cursor()
    with conn:
        with cur:
            cur.execute(command)
            data_query = cur.fetchall()
            listed_query = [list(element) for element in data_query]
            return listed_query


def write_to_database(command):
    conn = psycopg2.connect("dbname='sql_assignment' user=''")
    cur = conn.cursor()
    with conn:
        with cur:
            cur.execute(command)


def get_description(command):
    conn = psycopg2.connect("dbname='sql_assignment' user=''")
    cur = conn.cursor()
    with conn:
        with cur:
            cur.execute(command)
    return cur.description
