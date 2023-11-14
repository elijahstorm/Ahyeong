def menu():
    print("This program will convert 24hr format to 12 hour format and vice versa. Enter")
    print("1: 12 to 24 notation")
    print("2: 24 to 12 notation")
    print("99: To exit the program")
    return getNumber("> ")

# this will repeat until the number we get is a real number
def getNumber(prompt: str):
    while True:
        try:
            choice = int(input(prompt))
            return choice
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# this will repeat until the number we get is a real number
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

# From 1:00 PM to 11:59 PM you add 12 hours,
# and from 12:00 AM (midnight) to 12:59 AM you subtract 12 hours.
def convertTo24(time: int, am: bool):
    return ("", (time - 12 if time == 12 else time) if am else (time + 12 if time < 12 else time))

# Starting from the first hour of the day (0:00 / midnight to 0:59), add 12 hours and AM to the time:
# From 1:00 to 11:59, simply add AM to the time:
# For times between 12:00 to 12:59, just add PM to the time:
# For times between 13:00 to 23:59, subtract 12 hours and add PM to the time:
def convertTo12(time: int, _: bool):
    ampm = ""
    if time == 0:
        time += 12
        ampm = "AM"
    elif time >= 1  and time < 12:
        ampm = "AM"
    elif time >= 12  and time < 13:
        ampm = "PM"
    elif time > 12:
        time -= 12
        ampm = "PM"
    return (ampm, time)

# all inputs will be similar, so we can have just one imput function
def getInputs(action, askAmpm = False):
    hours = getNumberInRange("Enter the time in hours: ", 1 if askAmpm else 0, 12 if askAmpm else 23)
    minutes = getNumberInRange("Enter the time in minutes: ", 0, 59)
    seconds = getNumberInRange("Enter the time in seconds: ", 0, 59)
    am = (getInputFromValidChoices("Enter AM/PM: ", ["am", "pm"]).lower() == 'am') if askAmpm else False
    reportTime(*action(hours, am), minutes, seconds)

def reportTime(ampm: str, hours: int, minutes: int, seconds: int):
    print("")
    print("")
    print("The time is:")
    print(f"{hours:02}:{minutes:02}:{seconds:02}{ampm}")
    print("")
    print("")

def main():
    # since choice is not one of the options, this works to skip directly to the menu
    # which is located at the end of the while loop
    choice = 0
    while choice != 99:
        if choice == 1:
            getInputs(convertTo24, True)
        elif choice == 2:
            getInputs(convertTo12)
        else:
            print("")
        choice = menu()
    print("Goodbye!")

main()