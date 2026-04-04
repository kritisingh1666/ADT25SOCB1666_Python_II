# bank account practice
class BankAccount:
    def __init__(self, name, account_number, balance=0 ):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount>0:
            self.balance += amount
            print(f"Rs {amount} deposited successfully")
        else:
            print("invalid amount")

    def withdraw(self, amount):
        if amount<self.balance:
            self.balance -= amount
            print(f"Rs {amount} withdrawn successfully")

    def display(self):
        print("\n---account_details---") 
        print("name :", self.name)
        print("account number :", self.account_number)
        print("balance: ", self.balance)

 # main program
name = input("enter your name: ")
acc_no = input("enter account number: ")

acc = BankAccount(name, acc_no)

while True:
    print("1: display")
    print("2: deposit")
    print("3: withdraw")
    print("4: exit")

    choice = input("enter you choice: ")

    if choice =='1':
        acc.display()

    elif choice =='2':
        amt = float(input("Enter amount you want to deposit: "))
        acc.deposit(amt)

    elif choice =='3':
        amt = float(input("Enter amount you want to withdraw: "))
        acc.withdraw(amt)

    elif choice =='4':
        print("Thank You for using the banking system")

    else:
        print("invalid choice")       
  

    

                   

              
