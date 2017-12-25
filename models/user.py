from base import Base
from sqlalchemy import Column, String, Integer
from bcrypt import hashpw, checkpw
class User(Base):
    __tablename__ = 'users'

    email = Column(String(128), unique=True)
    name = Column(String(128))
    _password = Column(String(128))

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = hashpw(password)

    def validate_password(self, password):
        return checkpw(self.password, password)

    def get_pk(self):
        return self.pk

    def __str__(self):
        return "{'name': {}, 'email': {}".format(self.name, self.email)
