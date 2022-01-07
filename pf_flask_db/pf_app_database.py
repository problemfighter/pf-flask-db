from flask_sqlalchemy import SQLAlchemy, BaseQuery, Model
from pf_flask_db.helper.pf_db_helper import PFDBHelper


class PFAppDatabase(SQLAlchemy):

    def __init__(self,
                 app=None, use_native_unicode=True, session_options=None,
                 metadata=None, query_class=BaseQuery, model_class=Model,
                 engine_options=None):
        if not query_class:
            query_class = PFDBHelper
        super().__init__(
            app=app, use_native_unicode=use_native_unicode,
            session_options=session_options, metadata=metadata,
            query_class=query_class, engine_options=engine_options, model_class=model_class
        )

    def run_sql(self, sql):
        try:
            connection = self.engine.connect()
            result = connection.execute(sql)
            return result
        except Exception as e:
            pass


app_db = PFAppDatabase()
