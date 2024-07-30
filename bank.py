#Python bank

def show_amount(balance):
    print(f"Your balance is Rs.{balance:.2f}")

def deposit():
    amt=float(input("Enter your amount for deposit:"))

    if amt<=0:
        print("The amount is not sufficient")
        return 0

    else:
        print(f"Your amount has been deposited Rs.{amt:2f}")
        return amt

def withdraw(balance):
    amt=float(input("Enter amount for withdraw:"))

    if amt>balance:
        print("Insuffiecient Balance")
        return 0

    elif amt<=0:
        print("Please enter your amount")
        return 0

    else:
        print(f"Your amount has been withdrawn Rs.{amt:2f}")
        return amt


def main():
    balance=0
    isRunning=True

    while isRunning:
        print("Welcome to python bank")
        print("1. Show amount")
        print("2. Desposit")
        print("3. Withdraw")
        print("4. Exit")

        option=input("Choose your options (1-4):")

        if option=='1':
            show_amount(balance)
        
        elif option=='2':
            balance+=deposit()

        elif option=='3':
            balance-=withdraw(balance)
        
        elif option=='4':
            isRunning=False

        else:
            print("Out of option")


    print("Thank you for visiting")


if __name__=='__main__':
    main()