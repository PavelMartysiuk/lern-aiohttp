from contextlib import contextmanager
from tables import Session


@contextmanager
def connect():
    sess = Session()
    yield sess
    sess.close()
