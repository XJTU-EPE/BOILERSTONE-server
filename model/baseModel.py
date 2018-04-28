from peewee import *

from .dbcommon import Pgdb as db


class BaseModel(Model):
    class Meta:
        database = db