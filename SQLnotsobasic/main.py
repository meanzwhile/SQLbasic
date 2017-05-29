from flask import Flask, request, render_template, redirect, url_for, abort
from connection import database_handler, write_to_database, get_description

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/mentors")
def mentors():
    column_name = [col_names[0] for col_names in get_description("SELECT mentors.first_name, mentors.last_name,\
                                                                 schools.name, schools.country\
                                                                 FROM mentors\
                                                                 INNER JOIN schools ON mentors.city=schools.city;")]
    answer_list = database_handler("SELECT mentors.first_name, mentors.last_name, schools.name, schools.country\
                      FROM mentors\
                      INNER JOIN schools ON mentors.city = schools.city\
                      ORDER BY mentors.id;")
    return render_template("answer.html", column_name=column_name, answer_list=answer_list)


@app.route("/all-school")
def all_school():
    column_name = [col_names[0] for col_names in get_description("SELECT mentors.first_name, mentors.last_name,\
                                                                  schools.name, schools.country\
                                                                  FROM mentors\
                                                                  RIGHT JOIN schools ON mentors.city = schools.city;")]
    answer_list = database_handler("SELECT mentors.first_name, mentors.last_name, schools.name, schools.country\
                              FROM mentors\
                              RIGHT JOIN schools ON mentors.city = schools.city\
                              ORDER BY mentors.id;")
    return render_template("answer.html", column_name=column_name, answer_list=answer_list)


@app.route("/mentors-by-country")
def mentors_by_country():
    column_name = [col_names[0] for col_names in get_description("SELECT COUNT(first_name),\
                                                                      schools.country FROM mentors\
                                                                      INNER JOIN schools ON\
                                                                      mentors.city = schools.city\
                                                                      GROUP BY country;")]
    answer_list = database_handler("SELECT COUNT(first_name), schools.country FROM mentors\
                                    INNER JOIN schools ON mentors.city = schools.city\
                                    GROUP BY country\
                                    ORDER BY country;")
    return render_template("answer.html", column_name=column_name, answer_list=answer_list)


@app.route("/contacts")
def contacts():
    column_name = [col_names[0] for col_names in get_description("SELECT schools.name, mentors.first_name,\
                                                                  mentors.last_name FROM schools\
                                                                  INNER JOIN mentors ON\
                                                                  schools.contact_person = mentors.id;")]
    answer_list = database_handler("SELECT schools.name, mentors.first_name, mentors.last_name FROM schools\
                                    INNER JOIN mentors ON schools.contact_person = mentors.id\
                                    ;")
    return render_template("answer.html", column_name=column_name, answer_list=answer_list)


@app.route("/applicants")
def applicants():
    column_name = [col_names[0] for col_names in get_description("SELECT applicants.first_name,\
                                                                  applicants.application_code,\
                                                                  applicants_mentors.creation_date\
                                                                  FROM applicants INNER JOIN applicants_mentors\
                                                                  ON applicants.id = applicants_mentors.applicant_id;")]
    answer_list = database_handler("SELECT applicants.first_name, applicants.application_code,\
                                    applicants_mentors.creation_date\
                                    FROM applicants INNER JOIN applicants_mentors\
                                    ON applicants.id = applicants_mentors.applicant_id\
                                    WHERE applicants_mentors.creation_date > '2016-01-01'\
                                    ORDER BY creation_date DESC;")
    return render_template("answer.html", column_name=column_name, answer_list=answer_list)


@app.route("/applicants-and-mentors")
def applicants_and_mentors():
    column_name = [col_names[0] for col_names in get_description("SELECT applicants.first_name,\
                                                                  applicants.application_code,\
                                                                  mentors.first_name,\
                                                                  mentors.last_name\
                                                                  FROM applicants_mentors\
                                                                  RIGHT JOIN applicants\
                                                                    ON applicants_mentors.applicant_id = applicants.id\
                                                                  LEFT JOIN mentors\
                                                                    ON applicants_mentors.mentor_id = mentors.id;")]
    answer_list = database_handler("SELECT applicants.first_name, applicants.application_code,\
                                    mentors.first_name, mentors.last_name FROM applicants_mentors\
                                    RIGHT JOIN applicants\
                                        ON applicants_mentors.applicant_id = applicants.id\
                                    LEFT JOIN mentors\
                                        ON applicants_mentors.mentor_id = mentors.id\
                                    ORDER BY applicants.id;")
    return render_template("answer.html", column_name=column_name, answer_list=answer_list)


@app.route("/show-full-table", methods=["POST"])
def show_full_table():
    print("THIS FUCKING SHIT IS CALLED\n\n\n\n\n")
    table = request.form["name"]
    column_name = [col_names[0] for col_names in get_description("SELECT * FROM {};".format(table))]
    answer_list = database_handler("SELECT * FROM {};".format(table))
    return render_template("answer.html", column_name=column_name, answer_list=answer_list)


if __name__ == '__main__':
    app.run(debug=True)
