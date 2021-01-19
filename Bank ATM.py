
#Bank ATM

Balance = 1000
Chances = 3
Restart = ('Y')

print("Welcome to Pune Bank")
while Chances >= 0:
    pin = input("Enter your 4 Digit Pin : ")
    if pin == "1234":
        print("You have entered a correct pin")
        print("\n")
        while Restart not in ('n','No','no','N'):  # As restart value is Y it will enter the loop
            print("Press 1 for Balance\n")
            print("Press 2 for Withdrawal\n")
            print("Press 3 for Deposit\n")
            option  = int(input("What would you like to choose : "))
            if option == 1:
                print(f"Your Balance is : {Balance}")
                Restart = input("Would You like to go back Y or N : ")
                if Restart in ('n','No','no','N'):   #if no in restart value above it will break the loop
                    Chances = -1
                    print("Thank you for choosing Pune Bank")
                    print("Visit Again!!")
                    break
            elif option == 2:
                # option2 = ('y')
                Withdrawal = int(input("Please Enter Amount for Withdrawal (100,200,500): "))
                if Withdrawal in [100,200,500]:
                    Balance = Balance - Withdrawal
                    print(f"Your remaining Balance is {Balance}")
                    if Balance == 0:
                        Chances = -1
                        print("Cannot Withdraw more amount")
                        print("Thank you for choosing Pune Bank")
                        print("Visit Again!!")
                        break
                    Restart = input("Would You like to go back Y or N : ")
                    if Restart in ('n','No','no','N'):
                        Chances = -1
                        print("Thank you for choosing Pune Bank")
                        print("Visit Again!!")
                        break
                elif Withdrawal != [100,200,500]:
                    print("You have entered Invalid amount")
                    Restart = 'y'

            elif option == 3:
                Payment = int(input("Enter amount for Deposit : "))
                Balance = Balance + Payment
                print(f"Your current balance is {Balance}")
                Restart = input("Would you like to go back Y or N : ")
                if Restart in ('n','No','no','N') :
                    Chances = -1
                    print("Thank you for choosing Pune Bank")
                    print("Visit Again!!")
                    break

    elif pin != "1234":
        print("Incorrect Pin")
        Chances = Chances - 1
        if Chances == 0:
            print("No more Tries")
            break

