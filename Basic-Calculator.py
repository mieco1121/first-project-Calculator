#Functions
def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    return x / y

#Print
print("Basic Calculator")
print("1.Add")
print("2.Substract")
print("3.Multiply")
print("4.Divide")
print("Settings")
print("5.About")
print("PS:This is literally not my IDEA(NOT ORIGINAL) Credits to the Owner")

#Loop
while True:
    choice = input("Choose 1/2/3/4: ")
    
    if choice == "5":
        print("Created By: Mieco \n First Project of mine :>")

    if choice in ('1','2','3','4'):
        num1 = float(input("First Number: "))
        num2 = float(input("Second Number: "))

        if choice == "1":
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == "2":
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == "3":
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == "4":
            print(num1, "/", num2, "=", divide(num1, num2))
    
        
        
        next_calculation = input("Wanna Calculate Again?:(Y/N)")
        if next_calculation == "N":
            break