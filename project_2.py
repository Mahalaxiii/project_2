class BankAccount:
    def __init__(self, account_number: str, account_holder: str, initial_balance: float = 0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transaction_history = []
        if initial_balance > 0:
            self.transaction_history.append(f"Account created with initial balance: ${initial_balance:.2f}")

    def deposit(self, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self.balance += amount
        self.transaction_history.append(f"Deposited: ${amount:.2f} | Balance: ${self.balance:.2f}")
        return self.balance

    def withdraw(self, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        self.transaction_history.append(f"Withdrew: ${amount:.2f} | Balance: ${self.balance:.2f}")
        return self.balance

    def check_balance(self) -> float:
        return self.balance

    def get_transaction_history(self) -> list:
        return self.transaction_history


class BankSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number: str, account_holder: str, initial_balance: float = 0.0) -> BankAccount:
        if account_number in self.accounts:
            raise ValueError("Account number already exists.")
        account = BankAccount(account_number, account_holder, initial_balance)
        self.accounts[account_number] = account
        return account

    def get_account(self, account_number: str) -> BankAccount:
        if account_number not in self.accounts:
            raise KeyError("Account not found.")
        return self.accounts[account_number]

    def save_data(self) -> dict:
        return {acc_num: {
            "holder": acc.account_holder,
            "balance": acc.balance,
            "history": acc.transaction_history
        } for acc_num, acc in self.accounts.items()}


def main():
    bank = BankSystem()
    
    while True:
        print("\n--- Bank Account Management System ---")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. View Transaction History")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ").strip()
        
        try:
            if choice == '1':
                acc_num = input("Enter account number: ").strip()
                holder = input("Enter account holder name: ").strip()
                init_bal = float(input("Enter initial balance (default 0.0): ") or 0.0)
                bank.create_account(acc_num, holder, init_bal)
                print(f"Success: Account created for {holder} with account number {acc_num}.")
                
            elif choice == '2':
                acc_num = input("Enter account number: ").strip()
                account = bank.get_account(acc_num)
                amount = float(input("Enter amount to deposit: "))
                new_bal = account.deposit(amount)
                print(f"Success: Deposited ${amount:.2f}. New Balance: ${new_bal:.2f}")
                
            elif choice == '3':
                acc_num = input("Enter account number: ").strip()
                account = bank.get_account(acc_num)
                amount = float(input("Enter amount to withdraw: "))
                new_bal = account.withdraw(amount)
                print(f"Success: Withdrew ${amount:.2f}. New Balance: ${new_bal:.2f}")
                
            elif choice == '4':
                acc_num = input("Enter account number: ").strip()
                account = bank.get_account(acc_num)
                print(f"Current Balance: ${account.check_balance():.2f}")
                
            elif choice == '5':
                acc_num = input("Enter account number: ").strip()
                account = bank.get_account(acc_num)
                print("\n--- Transaction History ---")
                history = account.get_transaction_history()
                if not history:
                    print("No transactions yet.")
                else:
                    for record in history:
                        print(record)
                        
            elif choice == '6':
                print("Exiting application. Thank you!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")
                
        except (ValueError, KeyError) as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
