from flask import Flask
from pf_flask_db.pf_app_model import AppModel

from pf_flask_db.pf_app_database import app_db

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pf-flask-db.sqlite"
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


@app.route('/create-bulk')
def create_bulk():
    total_record = 20
    person = Person(first_name="Flask", last_name="DB", email="flask-db@email.loc")
    for index in range(total_record):
        person.add(
            Person(
                first_name="First Name " + str(index),
                last_name="Last Name " + str(index),
                email="email-" + str(index) + "@email.loc",
                age=1 * index,
                income=100 * index)
        )
    person.save()
    response = str(total_record) + " Records successfully Inserted"
    return response


@app.route('/pagination')
@app.route('/pagination/<int:per_page>')
@app.route('/pagination/<int:page>/<int:per_page>')
def pagination(page: int = 1, per_page: int = 5):
    response = {
        "page": 0,
        "pages": 0,
        "per_page": 0,
        "totalItem": 0,
        "items": [],
    }
    persons = Person.query.paginate(page, per_page, error_out=False)
    if persons:
        response["page"] = persons.page
        response["pages"] = persons.pages
        response["per_page"] = persons.per_page
        response["totalItem"] = persons.total
        for person in persons.items:
            response["items"].append(person.first_name + " " + person.last_name + " " + person.email)
    return response


if __name__ == '__main__':
    app.run(debug=True)
