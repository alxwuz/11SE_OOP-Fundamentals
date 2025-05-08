class BankAccount:
    def __init__(self, account_number, balance, owner_name):
        self.account_number = account_number
        self.balance = balance
        self.owner_name = owner_name

    def get_account_number(self):
        return self.account_number
    
    def get_balance(self):
        return self.balance
    
    def set_account_number(self, new_account_number):
        if isinstance(new_account_number, int):
            self.account_number - new_account_number
        else:
            raise ValueError("Input must be an integer.")
        
    def set_balance(self, new_balance):
        if isinstance(new_balance, float):
            self.balance - new_balance