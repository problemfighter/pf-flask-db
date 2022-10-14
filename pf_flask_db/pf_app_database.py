from flask_sqlalchemy import SQLAlchemy, BaseQuery, Model

from pf_flask_db.cli.pf_flask_db_cli import init_flask_db_cli
from pf_flask_db.common.pf_flask_db_exception import PFFlaskDBException
from pf_flask_db.helper.pf_db_helper import PFDBHelper


class PFAppDatabase(SQLAlchemy):

    def __init__(self,
                 app=None, session_options=None,
                 metadata=None, query_class=BaseQuery, model_class=Model,
                 engine_options=None):
        if not query_class:
            query_class = PFDBHelper
        super().__init__(
            app=app,
            session_options=session_options, metadata=metadata,
            query_class=query_class, engine_options=engine_options, model_class=model_class
        )

    def init_app(self, app):
        super().init_app(app)
        if app:
            init_flask_db_cli(app, self)

    def run_sql(self, sql):
        try:
            connection = self.engine.connect()
            return connection.execute(sql)
        except Exception as e:
            raise PFFlaskDBException.ins().get_exception(e)


app_db = PFAppDatabase()
