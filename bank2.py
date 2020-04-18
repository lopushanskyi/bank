from currency_converter import CurrencyConverter

currencies = {
    'USD': '$',
    'EUR': '€'
}

c = CurrencyConverter()


def negative(x):
    """Transform positive number in negative"""
    if x > 0:
        x -= (x * 2)
    return x


class Account:

    def __init__(self,
                 title,
                 currency,
                 balance=0.0,
                 operations=None):
        if operations is None:
            operations = []
        self.title = title
        self.currency = currency
        self.balance = balance
        self.operations = operations

        print('*' * 65)
        print(f'||| {self.title} in {self.currency} successfully created. Balance {self.currency}{self.balance} |||')
        print('*' * 65)

    def deposit(self, deposit_amount):
        deposit = ('fund deposit', deposit_amount)
        self.operations.append(deposit)
        print(f'You deposit {deposit_amount}{self.currency}')

    def withdraw(self, withdraw_amount):
        withdraw = ('fund withdraw', negative(withdraw_amount))
        self.operations.append(withdraw)
        print(f'You withdraw {withdraw_amount}{self.currency}')

    def expense(self, category, expense_amount):
        expense = (category, negative(expense_amount))
        self.operations.append(expense)
        print(f'You expense "{category}" {expense_amount}{self.currency}')

    def income(self, category, income_amount):
        income = (category, income_amount)
        self.operations.append(income)
        print(f'You income "{category}" {income_amount}{self.currency}')

    def delete(self, category, delete_amount):
        negative(delete_amount)
        print(f'You deleted "{category}" {negative(delete_amount)}{self.currency}')
        self.operations.remove((category, negative(delete_amount)))

    def statement(self):
        index = 0
        self.balance = 0
        print('*' * 45)
        print(f'You have {len(self.operations)} operations on "{self.title}":')
        print('*' * 45)
        for transaction in self.operations:
            index += 1
            self.balance += transaction[1]
            print(f'{index}.\t{transaction[0]} {transaction[1]:.2f}{self.currency}. Balance: {self.balance:.2f}{self.currency}')

    def transfer(self, transfer_amount, from_account, to_account, rate):
        if transfer_amount > 0:
            print(
                f'You transfer {transfer_amount}{self.currency}. Rate: {rate:.2f}'
            )
            transfer_amount -= (transfer_amount * 2)
            transaction = ('transfer funds', transfer_amount)
            from_account.append(transaction)
            transfer_amount *= rate
            transaction = ('transfer funds', abs(transfer_amount))
            to_account.append(transaction)

from currency_converter import CurrencyConverter

currencies = {
    'USD': '$',
    'EUR': '€'
}

c = CurrencyConverter()


def negative(x):
    """Transform positive number to negative"""
    if x > 0:
        x -= (x * 2)
    return x


class Account:

    def __init__(self,
                 title,
                 currency,
                 balance=0.0,
                 operations=None):
        if operations is None:
            operations = []
        self.title = title
        self.currency = currency
        self.balance = balance
        self.operations = operations

        print('*' * 65)
        print(f'||| {self.title} in {self.currency} successfully created. Balance {self.currency}{self.balance} |||')
        print('*' * 65)

    def deposit(self, deposit_amount):
        deposit = ('fund deposit', deposit_amount)
        self.operations.append(deposit)
        print(f'You deposit {deposit_amount}{self.currency}')

    def withdraw(self, withdraw_amount):
        withdraw = ('fund withdraw', negative(withdraw_amount))
        self.operations.append(withdraw)
        print(f'You withdraw {withdraw_amount}{self.currency}')

    def expense(self, category, expense_amount):
        expense = (category, negative(expense_amount))
        self.operations.append(expense)
        print(f'You expense "{category}" {expense_amount}{self.currency}')

    def income(self, category, income_amount):
        income = (category, income_amount)
        self.operations.append(income)
        print(f'You income "{category}" {income_amount}{self.currency}')

    def delete(self, category, delete_amount):
        negative(delete_amount)
        print(f'You deleted "{category}" {negative(delete_amount)}{self.currency}')
        self.operations.remove((category, negative(delete_amount)))

    def statement(self):
        index = 0
        self.balance = 0
        print('*' * 45)
        print(f'You have {len(self.operations)} operations on "{self.title}":')
        print('*' * 45)
        for transaction in self.operations:
            index += 1
            self.balance += transaction[1]
            print(f'{index}.\t{transaction[0]} {transaction[1]:.2f}{self.currency}. Balance: {self.balance:.2f}{self.currency}')

    def transfer(self, transfer_amount, from_account, to_account, rate):
        print(f'You transfer {negative(transfer_amount)}{self.currency}. Rate: {rate:.2f}')
        transaction = ('transfer funds', negative(transfer_amount))
        from_account.append(transaction)
        transfer_amount *= rate
        transaction = ('receive funds', abs(transfer_amount))
        to_account.append(transaction)

    def get_balance(self):
        operation_list = []
        category_list = []
        for transaction in self.operations:
            operation_list.append(transaction[1])
            category_list.append(transaction[0])
        print('/' * 45)
        print(f'"{self.title}" balance: {self.currency}{sum(operation_list)}')
        print('/' * 45)
    def get_balance(self):
        operation_list = []
        category_list = []
        for transaction in self.operations:
            operation_list.append(transaction[1])
            category_list.append(transaction[0])
        print('/' * 45)
        print(f'"{self.title}" balance: {self.currency}{sum(operation_list)}')
        print('/' * 45)
