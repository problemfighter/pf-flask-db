from pf_flask_db.helper.pf_db_helper import PFDBHelper


class Query(PFDBHelper):

    def all(self):
        pass

    def first(self):
        pass

    def first_or_404(self, description=None):
        pass

    def paginate(self, page=None, per_page=None, error_out=True, max_per_page=None):
        pass

    def count(self):
        pass

    def get(self, ident):
        pass

    def get_or_404(self, ident, description=None):
        pass

    def with_entities(self, *entities):
        pass

    def filter(self, *criterion):
        return self

    def filter_by(self, **kwargs):
        return self

    def order_by(self, *clauses):
        pass

    def group_by(self, *clauses):
        pass

    def having(self, criterion):
        pass

    def join(self, target, *props, **kwargs):
        pass

    def limit(self, limit):
        pass

    def offset(self, offset):
        pass

    def from_statement(self, statement):
        pass

    def one_or_none(self):
        pass

    def one(self):
        pass

    def delete(self, synchronize_session="evaluate"):
        pass

    def update(self, values, synchronize_session="evaluate", update_args=None):
        pass
