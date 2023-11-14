def menu():
    print("1: Enter 1 to order coffee")
    print("2: Enter 2 to check the total money made up to this time")
    print("3: Enter 3 to check the total amount of coffee sold up to this time")
    print("4: Enter 4 to check the number of cups of coffee of each size sold")
    print("5: Enter 5 to print the data")
    print("9: To exit the program")
    return getNumber("> ")

class Data:
    def __init__(self, total, orders):
        self.total = total
        self.orders = orders

# this will repeat until the number we get is a real number
def getNumber(prompt: str):
    while True:
        try:
            choice = int(input(prompt))
            return choice
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# this will repeat until the number we get is a real number that is within the range
def getNumberInRange(prompt: str, min: int, max: int):
    while True:
        try:
            choice = int(input(prompt))
            if (choice >= min and choice <= max):
                return choice
            print(f"That number is not in the valid range. Please enter a number from {min} to {max}")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# this will repeat until a given choice is entered
def getInputFromValidChoices(prompt: str, choices: list[str]):
    choice = ''
    while True:
        choice = input(prompt)
        if choice.lower() in [item.lower() for item in choices]:
            break
        print("Invalid input. Please enter from one of the following: ", ", ".join(choices))
    return choice

def askPay(total: float):
    print("")
    print("")
    print("Please pay: ", "${:.2f}".format(total))
    print("")

def orderCoffee(size: str):
    amount = -1
    while amount < 0:
        amount = getNumber('Enter a valid number of cups: ')
    return amount

def selectCoffeeFromMenu(data):
    choice = 0
    total = 0
    orders = {
        'small': 0,
        'medium': 0,
        'large': 0
    }
    prices = {
        'small': 1.75,
        'medium': 1.9,
        'large': 2
    }
    while choice != 9:
        if choice == 1:
            amount = orderCoffee("small")
            total += prices["small"] * amount
            orders["small"] += amount
        if choice == 2:
            amount = orderCoffee("medium")
            total += prices["medium"] * amount
            orders["medium"] += amount
        if choice == 3:
            amount = orderCoffee("large")
            total += prices["large"] * amount
            orders["large"] += amount
        print("1: Enter 1 to buy coffee in a small cup size (9 oz)")
        print("2: Enter 2 to buy coffee in a medium cup size (12 oz)")
        print("3: Enter 3 to buy coffee in a large cup size (15 oz)")
        print("9: To exit")
        choice = getNumber("> ")
    askPay(total)
    data.orders["small"] += orders["small"]
    data.orders["medium"] += orders["medium"]
    data.orders["large"] += orders["large"]
    data.total += total

def getTotalOz(orders):
    oz = {
        'small': 9,
        'medium': 12,
        'large': 15
    }
    return (oz["small"] * orders["small"]) + (oz["medium"] * orders["medium"]) + (oz["large"] * orders["large"])

def totalMoney(data):
    print(f"Total money made: ${data.total}")

def totalSold(data):
    print(f"Total coffee sold: {getTotalOz(data.orders)} oz")
    
def totalNumberOfEachSize(data):
    print(f"Small cup count: {data.orders['small']}")
    print(f"Medium cup count: {data.orders['medium']}")
    print(f"Large cup count: {data.orders['large']}")

def printData(data):
    totalNumberOfEachSize(data)
    totalSold(data)
    totalMoney(data)

def main():
    data = Data(0, {
        "small": 0,
        "medium": 0,
        "large": 0
    })
    choice = 0
    while choice != 9:
        if choice == 1:
            selectCoffeeFromMenu(data)
        elif choice == 2:
            totalMoney(data)
        elif choice == 3:
            totalSold(data)
        elif choice == 4:
            totalNumberOfEachSize(data)
        elif choice == 5:
            printData(data)
        print("")
        choice = menu()
        print("")
    print("Goodbye!")

main()