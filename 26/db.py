import datetime
import peewee_async
from peewee import *
from slugify import slugify

db_table_name = slugify("Виталий Козаченко frog")

# connection = {
#     'user': 'py4seo',
#     'password': 'PY1111forSEO',
#     'host': '46.30.164.249',
#     'port': 5432
# }

db = peewee_async.PostgresqlDatabase('library', autorollback=True, host='88.198.172.182', port=5432, user='py4seo', password='PY1111forSEO')


class Page(Model):
    title = CharField(max_length=1024, index=True)
    h1 = CharField(max_length=1024)
    url = CharField(max_length=1024)
    scanned = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db
        table_name = db_table_name


objects = peewee_async.Manager(db)


if __name__ == '__main__':
    db.connect()

    db.create_tables([Page])