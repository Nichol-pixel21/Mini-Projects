#Python Banking Program 

def show_balance():
    print(f"Your balance is ${balance:.2f}")

def deposit():
    amount = float(input("Enter the accunt to eb a deposited:"))

    if amount < 0 :
        print("That is not valid.")
        return 0
    else :
        return amount
def withdraw():
    amount = float(input("Enter the amount to be withdrawn:"))

    if amount > balance :
        print("INsufficient man u are broke.")
    elif amount < 0 :
        print("More money needed.")
    else : 
        return amount 

balance = 0 
is_running = True 

while is_running:
    print("Banking Program ")
    print("1.Show Balnce")
    print("2. Deposit")
    print("3. Withdraw")
    print("4.Exit")

    choice = input("Enter your choice (1-4):")

    if choice == "1":
        show_balance()
    elif choice == "2":
        balance += deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        is_running = False
    else :
        print("That is not valid bro.")
        
    print("Thank you! Have A Nice Day Today.")