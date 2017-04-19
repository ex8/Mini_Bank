import peewee, datetime

# PostgreSQL database configuration
db = peewee.PostgresqlDatabase(
    'DB_NAME',
    user='DB_USER',
    password='DB_PASSWORD',
    host='localhost'
    )

# Base Model as reference to DB (so we can re-use)
class BaseModel(peewee.Model):
    class Meta:
        database = db


# Accounts table - pretty straight forward
class Account(BaseModel):
    name = peewee.CharField(max_length=100, unique=True)
    type = peewee.CharField(max_length=20)
    balance = peewee.FloatField()
    pin = peewee.IntegerField()
    created = peewee.DateTimeField(default=datetime.datetime.now)
    last_updated = peewee.DateTimeField()


# Transactions table - pretty straight forward
class Transaction(BaseModel):
    date = peewee.DateField()
    amount_in = peewee.IntegerField()
    fees = peewee.IntegerField()
    amount_out = peewee.FloatField()
    source = peewee.CharField(max_length=50)
    uploaded = peewee.DateTimeField(default=datetime.datetime.now)
    account = peewee.ForeignKeyField(Account, related_name='transactions')

db.connect()
db.create_tables([Account, Transaction], safe=True)
db.close()
