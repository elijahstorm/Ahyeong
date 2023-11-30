import string

def count_letters(file_name):
    # Create an empty dictionary to store letter frequencies
    letter_freq = {letter: 0 for letter in string.ascii_lowercase}

    try:
        # Open the file
        with open(file_name, 'r') as file:
            # Read the file content
            content = file.read().lower()

            # Iterate through each character in the content
            for char in content:
                # Check if the character is a letter
                if char.isalpha():
                    # Increment the frequency count of the letter
                    letter_freq[char] += 1

        # Print the histogram
        print("{:<10} {:<10}".format('Letter', 'Frequency'))
        print("-" * 20)
        for letter, freq in letter_freq.items():
            print("{:<10} {:<10}".format(letter, freq))

    except FileNotFoundError:
        print("File not found!")

def main():
    file_name = input("Enter the file name: ")
    count_letters(file_name)

if __name__ == "__main__":
    main()
