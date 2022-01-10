from flask import Flask
from pf_flask_db.pf_app_model import AppModel
from pf_flask_db.pf_app_database import app_db

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pf-flask-db-raw.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app_db.init_app(app)


class Person(AppModel):
    id = app_db.Column(app_db.Integer, primary_key=True)
    first_name = app_db.Column(app_db.String(150), nullable=False)
    last_name = app_db.Column(app_db.String(150))
    email = app_db.Column(app_db.String(120), nullable=False)
    age = app_db.Column(app_db.Integer)
    income = app_db.Column(app_db.Float, default=0)


with app.app_context():
    app_db.create_all()


@app.route('/')
def bismillah():
    return "PF Flask DB Tutorial"


@app.route('/create')
def create():
    insert = "INSERT INTO person (first_name, last_name, email) VALUES ('Raw First Name', 'Raw Last Name', 'hmtmcse.com@gmail.com')"
    app_db.run_sql(insert)
    response = "Data successfully Inserted"
    return response


@app.route('/update')
def update():
    sql = "UPDATE person SET first_name = 'updated first name', last_name = 'updated last name' WHERE id = 1"
    persons = app_db.run_sql(sql)
    return "Data has been updated."


@app.route('/delete')
def delete():
    sql = "DELETE FROM person WHERE id = 1"
    persons = app_db.run_sql(sql)
    return "Record has been deleted"


@app.route('/list')
def list():
    response = ""
    sql = "SELECT * FROM person"
    persons = app_db.run_sql(sql)
    for person in persons:
        response += person.first_name + " " + person.last_name + " " + person.email + "<br>"
    return response


if __name__ == '__main__':
    app.run(debug=True)
