from currency_converter import CurrencyConverter

currencies = {
    'USD': '$',
    'EUR': '€'
}

c = CurrencyConverter()


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
        if withdraw_amount > 0:
            withdraw_amount -= (withdraw_amount * 2)
            withdraw = ('fund withdraw', withdraw_amount)
            self.operations.append(withdraw)
        print(f'You withdraw {withdraw_amount}{self.currency}')

    def expense(self, category, expense_amount):
        if expense_amount > 0:
            expense_amount -= (expense_amount * 2)
            expense = (category, expense_amount)
            self.operations.append(expense)
        print(f'You expense "{category}" {expense_amount}{self.currency}')

    def income(self, category, income_amount):
        income = (category, income_amount)
        self.operations.append(income)
        print(f'You income "{category}" {income_amount}{self.currency}')

    def delete(self, category, delete_amount):
        if delete_amount > 0:
            delete_amount -= (delete_amount * 2)
        print(f'You deleted "{category}" {delete_amount}{self.currency}')
        self.operations.remove((category, delete_amount))

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

    def get_balance(self):
        operation_list = []
        category_list = []
        for transaction in self.operations:
            operation_list.append(transaction[1])
            category_list.append(transaction[0])
        print('/' * 45)
        print(f'"{self.title}" balance: {self.currency}{sum(operation_list)}')
        print('/' * 45)


usd = Account('Savings Dollar', currencies['USD'], 0)
usd.deposit(500)
usd.withdraw(150)
usd.deposit(35)
usd.withdraw(40)
usd.expense('books', 125)
usd.expense('eating out', 25)
usd.income('salary', 1500)
usd.expense('car service', 129)
usd.expense('alcohol', 654)
usd.deposit(333)
usd.delete('car service', 129)
usd.statement()
usd.get_balance()

eur = Account('Savings Euro', currencies['EUR'], 0)
eur.deposit(130)
eur.deposit(120)
usd.transfer(30, usd.operations, eur.operations, c.convert(1, 'USD', 'EUR'))
eur.expense('alcohol', 58)
eur.deposit(70)
eur.deposit(52)
eur.withdraw(34)
eur.transfer(75, eur.operations, usd.operations, c.convert(1, 'EUR', 'USD'))
eur.statement()
eur.get_balance()
usd.statement()
