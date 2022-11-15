from pf_flask_db.common.pf_flask_db_exception import PFFlaskDBException
from pf_flask_db.helper.query_suggestion import Query
from pf_flask_db.pf_app_database import app_db


class PFModel(app_db.Model):
    __abstract__ = True
    query: Query
    _model_list = []

    def save(self):
        self.bulk_save(self._model_list)
        self._model_list.clear()

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

    @staticmethod
    def save_all(models: list):
        if models:
            model = models.pop(0)
            if isinstance(model, PFModel):
                model.bulk_save(models)

    def bulk_save(self, models: list):
        try:
            self.before_save()
            app_db.session.add(self)
            if models:
                for model in models:
                    model.before_save()
                app_db.session.add_all(models)
            app_db.session.commit()
            self.after_save()
            for model in models:
                model.after_save()
        except Exception as e:
            raise PFFlaskDBException.ins().get_exception(e)

    def before_save(self):
        pass

    def after_save(self):
        pass
