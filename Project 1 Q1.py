def menu():
    print("This program performs operations on fraction. Enter")
    print("1: To add fraction")
    print("2: To subtract fraction")
    print("3: To multiply fraction")
    print("4: To divide fraction")
    print("9: To exit the program")
    choice = int(input())
    return choice

def addFractions():
    print("For fraction 1")
    num1 = int(input("Enter the numerator: "))
    den1 = int(input("Enter the denominator: "))
    print("For fraction 2")
    num2 = int(input("Enter the numerator :"))
    den2 = int(input("Enter the denominator: "))
    print(num1,"/",den1," + ",num2,"/",den2," = ",(num1*den2 + num2*den1),"/",(den1*den2))

def subtractFractions():
    print("For fraction 1")
    num1 = int(input("Enter the numerator: "))
    den1 = int(input("Enter the denominator: "))
    print("For fraction 2")
    num2 = int(input("Enter the numerator :"))
    den2 = int(input("Enter the denominator: "))
    print(num1, "/", den1, " - ", num2, "/", den2, " = ", (num1 * den2 - num2 * den1), "/", (den1 * den2))


def multiplyFractions():
    print("For fraction 1")
    num1 = int(input("Enter the numerator: "))
    den1 = int(input("Enter the denominator: "))
    print("For fraction 2")
    num2 = int(input("Enter the numerator :"))
    den2 = int(input("Enter the denominator: "))
    print(num1, "/", den1, " * ", num2, "/", den2, " = ", (num1 * num2), "/", (den1 * den2))


def divideFractions():
    print("For fraction 1")
    num1 = int(input("Enter the numerator: "))
    den1 = int(input("Enter the denominator: "))
    while den1 == 0:
        print("The denominator must be nonzero.")
        den1 = int(input("Enter the denominator: "))
    print("For fraction 2")
    num2 = int(input("Enter the numerator :"))
    den2 = int(input("Enter the denominator: "))
    while den2 ==0:
        print("To divide, the second fraction must be nonzero. ")
        den2 = int(input("Enter a nonzero number for the numerator: "))
    print(num1,"/",den1," / ",num2,"/",den2," = ",(num1*den2),"/",(den1*num2))


def main():
    choice = menu()
    while choice != 9:
        if choice == 1:
            addFractions()
            menu()
        elif choice == 2:
            subtractFractions
            menu()
        elif choice == 3:
            multiplyFractions()
            menu()
        elif choice == 4:
            divideFractions()
            menu()
        elif choice == 9:
            print()
main()