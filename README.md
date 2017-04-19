# Mini_Bank
Mini Bank project to better familiarize myself with PostgreSQL and Object Relational Mapping (ORM) technologies. I used peewee ORM as it's lightweight and simple. 

# Requirements
Python 3+ (I am using Python 3.4 when I developed this)

You must have peewee installed.

```
pip3 install peewee
```

You need to edit models.py to configure your DB credentials
```
# PostgreSQL database configuration
db = peewee.PostgresqlDatabase(
    'DB_NAME',
    user='DB_USER',
    password='DB_PASSWORD',
    host='localhost'
)
```

# Usage
To make a new bank account:
```
python3 main.py --new business test_account
```

To deposit money into a bank account:
```
python3 main.py --deposit test_account 50
```

To upload a CSV file with transaction reports (please note code reads auto-generated WHMCS transactions reports and parses the data accordingly!):
```
python3 main.py --upload test_account data_march2017 uploads/data.csv
```

# TODO
- implement '--reports' command with pandas DataFrames (will replace csv library)
- reset pin option
- add '--archive' command that archives all transaction data with a certain account
