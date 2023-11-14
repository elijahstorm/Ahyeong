def menu():
    print("This program performs operations on fraction. Enter")
    print("1: To add fraction")
    print("2: To subtract fraction")
    print("3: To multiply fraction")
    print("4: To divide fraction")
    print("9: To exit the program")
    return getNumber("Enter a number: ")

# since all inputs are numbers, we can make just one getNumber function
def getNumber(prompt: str):
    while True:
        try:
            choice = int(input(prompt))
            return choice
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def addFractions(num1:int,den1:int,num2:int,den2:int):
    print(f"({num1}/{den1}) + ({num2}/{den2}) = {(num1*den2 + num2*den1)}/{den1*den2}")

def subtractFractions(num1: int, den1: int, num2: int, den2: int):
    print(f"({num1}/{den1}) - ({num2}/{den2}) = {(num1 * den2 - num2 * den1)}/{den1 * den2}")

def multiplyFractions(num1: int, den1: int, num2: int, den2: int):
    print(f"({num1}/{den1}) * ({num2}/{den2}) = {(num1 * num2)}/{den1 * den2}")

def divideFractions(num1: int, den1: int, num2: int, den2: int):
    print(f"({num1}/{den1}) / ({num2}/{den2}) = {(num1 * den2)}/{den1 * num2}")

# all inputs will be the same, so we can have just one imput function
def getInputs(action, nonzero = False):
    print("For fraction 1")
    num1 = getNumber("Enter the numerator: ")
    den1 = getNumber("Enter the denominator: ")
    while den1 == 0:
        print("The denominator must be nonzero.")
        den1 = getNumber("Enter the denominator: ")
    print("For fraction 2")
    num2 = getNumber("Enter the numerator: ")
    while nonzero and num2 == 0:
        print("To divide, the second fraction must be nonzero. ")
        num2 = getNumber("Enter the numerator: ")
    den2 = getNumber("Enter the denominator: ")
    while den2 == 0:
        print("The denominator must be nonzero.")
        den2 = getNumber("Enter a nonzero number for the numerator: ")
    action(num1, den1, num2, den2)

def main():
    # since choice is not one of the options, this works to skip directly to the menu
    # which is located at the end of the while loop
    choice = 0
    while choice != 9:
        if choice == 1:
            getInputs(addFractions)
        elif choice == 2:
            getInputs(subtractFractions)
        elif choice == 3:
            getInputs(multiplyFractions)
        elif choice == 4:
            getInputs(divideFractions, True)
        elif choice == 9:
            print("Goodbye!")
        choice = menu()

main()