from bank_account import BankAccount

account1 = BankAccount(1231234, 1000.03, 'Shawn Cute')
account2 = BankAccount(1231233, 2000.10, 'Shawn Cutey')

print(account1.get_account_number)
print(account1.get_balance)
print(account1.get_owner_name)

print(account2.get_account_number)
print(account2.get_balance)
print(account2.get_owner_name)

account1.set_account_number(7654321)
account1.get_balance(123.12)
account1.get_owner_name("Fan Shawn")

account2.set_account_number(1234567)
account2.get_balance(99999.92)
account2.get_owner_name("Fan Shawney")

print(account1.get_account_number)
print(account1.get_balance)
print(account1.get_owner_name)

print(account2.get_account_number)
print(account2.get_balance)
print(account2.get_owner_name)

withdrawn_bal = int(input("Enter the amount to withdraw: "))
account1.withdraw(withdrawn_bal)
print(account1.get_balance())

deposited_bal = int(input("Enter the amount to deposit: "))
account1.deposit(deposited_bal)
print(account1.get_balance())