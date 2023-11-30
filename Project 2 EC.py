import json

# Function to display the menu
def display_menu():
    print("Menu:")
    print("1. Look up an email address")
    print("2. Add a new name and email address")
    print("3. Change an existing email address")
    print("4. Delete an existing name and email address")
    print("5. Exit")

# Function to look up an email address
def lookup_email(dictionary):
    name = input("Enter the name to look up: ")
    if name in dictionary:
        print(f"Email address for {name}: {dictionary[name]}")
    else:
        print("Name not found in the database.")

# Function to add a new name and email address
def add_email(dictionary):
    name = input("Enter the name: ")
    email = input("Enter the email address: ")
    dictionary[name] = email
    print(f"{name} and {email} added to the database.")

# Function to change an email address
def change_email(dictionary):
    name = input("Enter the name whose email you want to change: ")
    if name in dictionary:
        new_email = input("Enter the new email address: ")
        dictionary[name] = new_email
        print(f"Email address for {name} updated to {new_email}.")
    else:
        print("Name not found in the database.")

# Function to delete a name and email address
def delete_email(dictionary):
    name = input("Enter the name to delete: ")
    if name in dictionary:
        del dictionary[name]
        print(f"{name} deleted from the database.")
    else:
        print("Name not found in the database.")

# Function to load data from a file
def load_data():
    try:
        with open("emails.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Function to save data to a file
def save_data(dictionary):
    with open("emails.json", "w") as file:
        json.dump(dictionary, file)

# Main function
def main():
    email_dictionary = load_data()

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            lookup_email(email_dictionary)
        elif choice == '2':
            add_email(email_dictionary)
        elif choice == '3':
            change_email(email_dictionary)
        elif choice == '4':
            delete_email(email_dictionary)
        elif choice == '5':
            save_data(email_dictionary)
            print("Data saved. Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()

