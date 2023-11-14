def menu():
    print("This program performs will help you calculate operations on fractions. Enter:")
    print("1: To add fraction")
    print("2: To subtract fraction")
    print("3: To multiply fraction")
    print("4: To divide fraction")
    print("9: To exit the program")
    choice = int(input())
    return choice

def addFractions(num1:int,den1:int,num2:int,den2:int):
    print(f"({num1}/{den1}) + ({num2}/{den2}) = {(num1*den2 + num2*den1)}/{den1*den2}")

def subtractFractions(num1: int, den1: int, num2: int, den2: int):
    print(f"{num1}/{den1} - {num2}/{den2} = {(num1 * den2 - num2 * den1)}/{den1 * den2}")

def multiplyFractions(num1: int, den1: int, num2: int, den2: int):
    print(f"{num1}/{den1} * {num2}/{den2} = {(num1 * num2)}/{den1 * den2}")

def divideFractions(num1: int, den1: int, num2: int, den2: int):
    print(f"{num1}/{den1} / {num2}/{den2} = {(num1 * den2)}/{den1 * num2}")

def getInputs(action):
    print("For fraction 1")
    num1 = int(input("Enter the numerator: "))
    den1 = int(input("Enter the denominator: "))
    while den1 == 0:
        print("The denominator must be nonzero.")
        den1 = int(input("Enter the denominator: "))
    print("For fraction 2")
    num2 = int(input("Enter the numerator: "))
    den2 = int(input("Enter the denominator: "))
    while den2 == 0:
        print("To divide, the second fraction must be nonzero. ")
        den2 = int(input("Enter a nonzero number for the numerator: "))
    action(num1, den1, num2, den2)

def main():
    choice = 0
    while choice != 9:
        if choice == 1:
            getInputs(addFractions)
        elif choice == 2:
            getInputs(subtractFractions)
        elif choice == 3:
            getInputs(multiplyFractions)
        elif choice == 4:
            getInputs(divideFractions)
        elif choice == 9:
            print("Goodbye!")
        choice = menu()

main()