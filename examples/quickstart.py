from flask import Flask
from pf_flask_db.pf_app_model import AppModel
from pf_flask_db.pf_app_database import app_db

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pf-flask-db-quick-start.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app_db.init_app(app)


class Person(AppModel):
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
    person = Person(first_name="First Name", last_name="Last Name", email="hmtmcse.com@gmail.com", age=22, income=500)
    person.save()
    response = "Data successfully Inserted"
    return response


@app.route('/update')
def update():
    person = Person.query.filter_by(id=1).first()
    if person:
        person.first_name = "FName Update"
        person.last_name = "LName Update"
        person.save()
    return "Data has been updated."


@app.route('/delete')
def delete():
    person = Person.query.filter_by(id=1).first()
    if person:
        person.delete()
    return "Record has been deleted"


@app.route('/list')
def list():
    response = ""
    persons = Person.query.all()
    for person in persons:
        response += person.first_name + " " + person.last_name + " " + person.email + "<br>"
    return response


if __name__ == '__main__':
    app.run(debug=True)
