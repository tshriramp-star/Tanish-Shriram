import datetime
import random
import string

class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance
        self.account_number = self._generate_account_number()
        self.transaction_history = []

    def _generate_account_number(self):
        return ''.join(random.choices(string.digits, k=10))

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        self._record_transaction("Deposit", amount)

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        self._record_transaction("Withdrawal", amount)

    def _record_transaction(self, transaction_type, amount):
        transaction = {
            "type": transaction_type,
            "amount": amount,
            "date": datetime.datetime.now()
        }
        self.transaction_history.append(transaction)

    def get_balance(self):
        return self.balance

    def get_transaction_history(self):
        return self.transaction_history

    def __str__(self):
        return f"Account Holder: {self.account_holder}, Account Number: {self.account_number}, Balance: ${self.balance:.2f}"
    