# main-0.py
import sys
from bank_account import BankAccount

def _fmt_amount(a):
    a = float(a)
    return str(int(a)) if a.is_integer() else str(a)

def main():
    # starting example balance as requested
    account = BankAccount(100)

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params and params[0] != '' else None

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${_fmt_amount(amount)}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${_fmt_amount(amount)}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()
