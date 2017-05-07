import psycopg2
import sys


def first(cur):
    cur.execute("""SELECT first_name, last_name FROM mentors;""")
    result = cur.fetchall()
    for element in result:
        print(element[0] + " " + element[1])


def second(cur):
    cur.execute("""SELECT nick_name FROM mentors WHERE city='Miskolc';""")
    result = cur.fetchall()
    for element in result:
        print(element[0])


def third(cur):
    cur.execute("""SELECT first_name ||' '|| last_name AS full_name, phone_number
                FROM applicants WHERE first_name='Carol';""")
    result = cur.fetchall()
    for element in result:
        print(element[0] + " : " + element[1])


def fourth(cur):
    cur.execute("""SELECT first_name ||' '|| last_name AS full_name, phone_number, email FROM applicants
                WHERE email LIKE '%@adipiscingenimmi.edu';""")
    result = cur.fetchall()
    for full_name, phone_number, email in result:
        print(full_name + " : " + phone_number)


def fifth(cur):
    cur.execute("""INSERT INTO applicants (first_name, last_name, phone_number, email, application_code)
                VALUES ('Markus', 'Schaffarzyk', '003620/725-2666', 'djnovus@groovecoverage.com', '54823');
                SELECT * FROM applicants WHERE application_code=54823;""")
    result = cur.fetchall()
    for element in result:
        for applicant in element:
            print(applicant)


def sixth(cur):
    cur.execute("""UPDATE applicants
                SET phone_number='003670/223-7459'
                WHERE first_name='Jemima' AND last_name='Foreman';
                SELECT first_name, last_name, phone_number FROM applicants
                WHERE first_name='Jemima' AND last_name='Foreman';""")
    result = cur.fetchall()
    for element in result:
        print(result)


def seventh(cur):
    cur.execute("""DELETE FROM applicants
                WHERE email LIKE '%@mauriseu.net'""")


def get_inputs(list_labels):
    inputs = input(list_labels)
    while not inputs:
        inputs = input(list_labels)
    return inputs


def choose(cur):
    print("(1) Mentors Name\n"
          "(2) Mentors nickname from Miskolc\n"
          "(3) Carol's hat\n"
          "(4) Other Girl\n"
          "(5) New applicant\n"
          "(6) Jemima's new phone number\n"
          "(7) Arsenio leaves school\n"
          "(0)Exit Program")
    inputs = get_inputs(["Please enter a number: "])
    option = inputs[0]
    if option == "1":
        first(cur)
    elif option == "2":
        second(cur)
    elif option == "3":
        third(cur)
    elif option == "4":
        fourth(cur)
    elif option == "5":
        fifth(cur)
    elif option == "6":
        sixth(cur)
    elif option == "7":
        seventh(cur)
    elif option == "0":
        sys.exit(0)
    else:
        raise KeyError("There is no such option.")


def main():
    try:
        conn = psycopg2.connect("dbname='peter' user='peter' host='localhost' password='korpeter'")
        conn.autocommit = True
        cur = conn.cursor()
    except Exception as e:
        print("Can't connect. Invalid dbname, user or password.")
        print(e)

    print("Welcome to Base SQL!")
    while True:
        try:
            choose(cur)
        except KeyError as err:
            print(err)


if __name__ == '__main__':
    main()
