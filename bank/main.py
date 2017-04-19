import sys, getpass
from account import BankAccount


def main():
    args = sys.argv
    acc = BankAccount()

    # Format: python3 main.py --new account_type account_name
    if '--new' in args:
        pin = getpass.getpass('Please enter a 4 digit pin: ')
        pin_again = getpass.getpass('Please enter it again: ')
        if pin == pin_again:
            acc.new(name=args[3], type=args[2], pin=pin)

    # Format: python3 main.py --delete account_name
    elif '--delete' in args:
        pin = getpass.getpass('Please enter your 4 digit pin: ')
        if acc.check_pin(args[2], int(pin)):
            acc.delete(args[2])

    # Format: python3 main.py --deposit account_name amount
    elif '--deposit' in args:
        pin = getpass.getpass('Please enter your 4 digit pin: ')
        if acc.check_pin(args[2], int(pin)):
            acc.deposit(name=args[2], amount=float(args[3]))

    # Format: python3 main.py --withdraw account_name amount
    elif '--withdraw' in args:
        pin = getpass.getpass('Please enter a 4 digit pin: ')
        if acc.check_pin(args[2], int(pin)):
            acc.withdraw(name=args[2], amount=float(args[3]))

    # Format: python3 main.py --balance account_name
    elif '--balance' in args:
        pin = getpass.getpass('Please enter your 4 digit pin: ')
        if acc.check_pin(args[2], int(pin)):
            acc.balance(name=args[2])

    # Format: python3 main.py --upload account_name source_name file_path
    elif '--upload' in args:
        pin = getpass.getpass('Please enter a 4 digit pin: ')
        if acc.check_pin(args[2], int(pin)):
            acc.upload(args[2], args[4], args[3])

    else:
        print('Usage: python main.py --command')

if __name__ == '__main__':
    main()
