import datetime
from peewee import *


connection = {
    'user': 'postgres',
    'password': 'postgres',
    'host': 'localhost',
    'port': 5432
}

db = PostgresqlDatabase('mydatabase', host='localhost',  port=5432, user='postgres', password='postgres')


class Page(Model):
    title = CharField(max_length=1024, index=True)
    h1 = CharField(max_length=1024)
    url = CharField(max_length=1024)
    scanned = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db
        table_name = 'pages'


def db_saver():
    db_objects = []
    while True:
        one_obj = (yield)
        if one_obj == 'save' or len(db_objects) > 10:
            Page.insert_many(db_objects).execute()
            db_objects = []
        else:
            db_objects.append(one_obj)


if __name__ == '__main__':
    pass
    #db.drop_tables([Page])
    # db.connect()
    # db.create_tables([Page])