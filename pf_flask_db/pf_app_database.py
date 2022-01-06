from flask_sqlalchemy import SQLAlchemy
from pf_flask_db.helper.pf_db_helper import PFDBHelper


class PFAppDatabase:

    def get_db(self):
        return SQLAlchemy(query_class=PFDBHelper)


app_db = PFAppDatabase().get_db()
