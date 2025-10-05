# bank_account.py
"""BankAccount class for basic banking operations."""

class BankAccount:
    def __init__(self, initial_balance=0):
        try:
            self._account_balance = float(initial_balance)
        except Exception:
            # if invalid initial balance, default to 0.0
            self._account_balance = 0.0

    def deposit(self, amount):
        """Add amount to the account balance."""
        amount = float(amount)
        self._account_balance += amount

    def withdraw(self, amount):
        """Attempt to withdraw amount.
        Return True if withdrawal succeeded, False if insufficient funds.
        """
        amount = float(amount)
        if amount <= self._account_balance:
            self._account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Print the balance in the required human-friendly format."""
        bal = float(self._account_balance)
        # show integer if whole number, otherwise show float (e.g. 2.5)
        if bal.is_integer():
            print(f"Current Balance: ${int(bal)}")
        else:
            print(f"Current Balance: ${bal}")
