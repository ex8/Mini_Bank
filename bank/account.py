from models import Account, Transaction
import datetime
import csv as xl


class BankAccount(object):
    """
    Check current balance of given account

    :param name - account name to check
    """
    def check_pin(self, name, pin_input):
        try:
            acc = Account.get(name=name)
            if acc.pin == pin_input:
                return True
            return False
        except IOError as e:
            print('Checking pin error', e)

    """
    Check current balance of given account

    :param name - account name to check
    """
    def balance(self, name):
        try:
            acc = Account.get(name=name)
            print('Account', name, 'has', '$' + str(acc.balance), 'in it.')
        except IOError as e:
            print('Error getting balance', e)

    """
    Create new bank account. Checks if name exists within DB.

    :param name - account name to create
    :param type - account type (personal or business)
    :param pin - pin linked to account
    """
    def new(self, name, type, pin):
        try:
            q = Account.select().where(Account.name == name)
            if q.exists():
                print('Account name', name, 'already exists')
                raise IOError
            now = datetime.datetime.now()
            new_acc = Account(name=name, type=type, balance=0, pin=pin, last_updated=now)
            new_acc.save()
            print('New account created:', name)
        except IOError as e:
            print('Error creating new account', e)

    """
    Delete existing bank account.

    :param name - account name to delete
    """
    def delete(self, name):
        try:
            acc = Account.get(name=name)
            acc.delete_instance()
            print('Deleted account:', name)
        except IOError as e:
            print('Error deleting account', e)

    """
    Deposit money into associated bank account. Also updates last_updated column

    :param name - account name
    :param amount - amount to deposit
    """
    def deposit(self, name, amount):
        try:
            acc = Account.get(name=name)
            acc.balance += int(amount)
            acc.last_updated = datetime.datetime.now()
            acc.save()
            print('Successfully deposited', '$' + amount, 'into', name)
        except IOError as e:
            print('Error depositing', e)

    """
    Withdraw money from associated bank account. Checks if funds are sufficient.
    Also updates last_updated column.

    :param name - account name
    :param amount - amount to deposit
    """
    def withdraw(self, name, amount):
        try:
            acc = Account.get(name=name)
            if acc.balance < amount:
                print('Insufficient funds in bank, current balance', '$'+str(acc.balance))
                raise IOError
            acc.balance -= int(amount)
            acc.last_updated = datetime.datetime.now()
            acc.save()
            print('Successfully withdrawn', '$' + amount, 'from', name)
        except IOError as e:
            print('Error withdrawing', e)

    """
    Upload transaction records using CSV file. Look in uploads/ to see example
    data.csv for format. Can also re-write this function to work for your CSV file
    structure. Updates last_updated column and balance accordingly.

    :param name - associated account name
    :param file - CSV file path (uploads/ dir for quick placement!)
    :param source - source of CSV file to better keep track of all transactions
    """
    def upload(self, name, file, source):
        try:
            acc = Account.get(name=name)
            balance_to_add = 0
            with open(file) as f:
                csv_f = xl.reader(f)
                next(csv_f)  # Skip filename line
                next(csv_f)  # Skip column headers
                for row in csv_f:
                    cleaned = lambda s: float(s[1:len(s)-4])
                    date = datetime.datetime.strptime(row[0], '%d/%m/%Y').strftime('%Y/%m/%d')
                    trans = Transaction(date=date,
                                        amount_in=cleaned(row[1]),
                                        fees=cleaned(row[2]),
                                        amount_out=cleaned(row[4]),
                                        source=source,
                                        account=acc)
                    trans.save()
                    balance_to_add += cleaned(row[4])
            acc.balance += balance_to_add
            acc.last_updated = datetime.datetime.now()
            acc.save()

            print('Successfully uploaded', file, 'to account', name)
            print('Added', '$' + str(balance_to_add), 'to account', name)
            print('New balance for account', name, 'is', '$' + str(acc.balance))
        except IOError as e:
            print('Error uploading', e)
