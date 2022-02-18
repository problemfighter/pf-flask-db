from pf_py_common.py_common import PyCommon
from sqlalchemy import Integer
from pf_flask_db.pf_app_database import app_db
from pf_flask_db.helper.pf_db_model import PFModel


class BaseModel(PFModel):
    __abstract__ = True


class RelationalModel(BaseModel):
    __abstract__ = True
    id = app_db.Column("id", app_db.BigInteger().with_variant(Integer, "sqlite"), primary_key=True)
    created = app_db.Column("created", app_db.DateTime, default=app_db.func.now())
    updated = app_db.Column("updated", app_db.DateTime, default=app_db.func.now(), onupdate=app_db.func.now())


class AppModel(RelationalModel):
    __abstract__ = True
    isDeleted = app_db.Column("is_deleted", app_db.Boolean, default=False)
    uuid = app_db.Column("uuid", app_db.String(50), default=PyCommon.uuid())
