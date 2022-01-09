from sqlalchemy.exc import IntegrityError
from pf_py_common.pf_exception import PFException


class PFFlaskDBException:
    EXCEPTION_TYPE = "FLASK_DB"

    def parse_integrity_error(self, exception: IntegrityError):
        try:
            if exception.orig and exception.orig.args and exception.orig.args[1]:
                return str(exception.orig.args[1])
        except:
            return "Integrity Error"
        return str(exception.orig)

    def get_exception(self, exception: Exception):
        if isinstance(exception, IntegrityError):
            return PFException(self.parse_integrity_error(exception), exception_type=self.EXCEPTION_TYPE)
        return PFException(str(exception), exception_type=self.EXCEPTION_TYPE)

    @staticmethod
    def ins():
        return PFFlaskDBException()
