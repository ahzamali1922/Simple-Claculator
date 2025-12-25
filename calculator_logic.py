def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def Multiply(x,y):
    return x*y

def Divide(x,y):
    if y == 0:
        return "Error, Cannot divide it by zero"
    return x/y

def Calculate():
    print("Simple Calculator:")
    print("for basic calculations")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("Q. Quit")

    while True:

        choice = input("Enter : 1,2,3,4 or Q \n").upper()
        if(choice == "Q"):
            print("Thank_you for using the calulator!!!")
            break

        if choice in ("1","2","3","4"):
            try:
                num1 = float(input("\n Enter the first number: "))
                num2 = float(input("\n Enter second number: "))
            except ValueError:
                print("Ivalid Input: Enter the correct Values")
                continue

            if choice == "1":
                print(f"{num1} + {num2} = {add(num1,num2)}")

            elif choice == "2":
                print(f"{num1} - {num2} = {subtract(num1,num2)}")

            elif choice == "3":
                print(f"{num1} * {num2} = {Multiply(num1,num2)}")

            elif choice == "4":
                print(f"{num1} / {num2} = {Divide(num1,num2)}")

        else:
            print("Invalid Input : \n Enter 1,2,3,4 or Q")

if __name__ == "__main__":
    Calculate()



