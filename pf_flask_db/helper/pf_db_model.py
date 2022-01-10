from pf_flask_db.common.pf_flask_db_exception import PFFlaskDBException
from pf_flask_db.helper.query_suggestion import Query
from pf_flask_db.pf_app_database import app_db


class PFModel(app_db.Model):
    __abstract__ = True
    query: Query
    _model_list = []

    def save(self):
        try:
            app_db.session.add(self)
            if self._model_list:
                app_db.session.add_all(self._model_list)
            app_db.session.commit()
        except Exception as e:
            raise PFFlaskDBException.ins().get_exception(e)

    def delete(self):
        try:
            app_db.session.delete(self)
            app_db.session.commit()
        except Exception as e:
            raise PFFlaskDBException.ins().get_exception(e)

    def add(self, model):
        self._model_list.append(model)
        return self

    def add_all(self, models: list):
        self._model_list = models
        return self
