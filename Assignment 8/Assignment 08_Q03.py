
def main():
    num_to_word = {
        '0': 'zero',
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine'
    }

    integer = input("Enter an integer to convert to words: ")
    result = ' '.join(num_to_word[digit] for digit in integer)
    print(result)

if __name__ == "__main__":
    main()
