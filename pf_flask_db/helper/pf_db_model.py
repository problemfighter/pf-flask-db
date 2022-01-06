from pf_flask_db.helper.query_suggestion import QuerySuggestion
from pf_flask_db.pf_app_database import app_db


class PFModel(app_db.Model):
    __abstract__ = True
    query: QuerySuggestion

    def save(self):
        try:
            app_db.session.add(self)
            app_db.session.commit()
        except Exception as e:
            pass

    def delete(self):
        try:
            app_db.session.delete(self)
            app_db.session.commit()
        except Exception as e:
            pass
