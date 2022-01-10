### In the name of God, the Most Gracious, the Most Merciful.

# PF-Flask-DB

Problem Fighter PF Flask DB (PF-Flask-DB) basically started with a Wrapper of Flask SQLAlchemy, When we try to create a
project using Flask that moment we have to think about many area, such as Database, ORM, Migration etc. It's make developer
life difficult, this project aim to integrate various library and provide a single but useful solution.


<br/><br/><br/>
## Example Codes
```python
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
```



<br/><br/><br/>
## Documentation
Install and update using [pip](https://pip.pypa.io/en/stable/getting-started/):
```bash
pip install -U PF-Flask-DB
```

**Please find [the Documentation](https://www.hmtmcse.com/pf/pf-flask-db/bismillah) with example from [hmtmcse.com](https://www.hmtmcse.com/pf/pf-flask-db/bismillah)**


<br/><br/><br/>
## Donate
[Problem Fighter](https://www.problemfighter.com/) develops and supports PF-Flask-DB and the libraries it uses. In order to grow
the community of contributors and users, and allow the maintainers to devote more time to the projects.


<br/><br/><br/>
## Contributing
For guidance on setting up a development environment and how to make a contribution to PF-Flask-DB, see the contributing guidelines.


<br/><br/><br/>
## Links
* **Changes :** [https://opensource.problemfighter.org/flask/pf-flask-db](https://opensource.problemfighter.org/flask/pf-flask-db)
* **PyPI Releases :** [https://pypi.org/project/pf-flask-db](https://pypi.org/project/pf-flask-db)
* **Source Code :** [https://github.com/problemfighter/pf-flask-db](https://github.com/problemfighter/pf-flask-db)
* **Issue Tracker :** [https://github.com/problemfighter/pf-flask-db/issues](https://github.com/problemfighter/pf-flask-db/issues)
* **Website :** [https://www.problemfighter.com/open-source](https://www.problemfighter.com/open-source)

