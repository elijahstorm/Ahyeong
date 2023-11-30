import string

# Function to write data from a list to a file
def write_to_file(file_name, data):
    with open(file_name, 'w') as file:
        for item in data:
            file.write("%s\n" % item)

# Function to create a list of unique words from a file and return it
def get_unique_words(file_name):
    words = []
    with open(file_name, 'r') as file:
        for line in file:
            for word in line.split():
                word = word.strip(string.punctuation).lower()
                if word not in words:
                    words.append(word)
    return words

# Function to create a list of union of words in two files and return it
def get_union_words(file1, file2):
    words_file1 = get_unique_words(file1)
    words_file2 = get_unique_words(file2)
    union_words = words_file1.copy()
    for word in words_file2:
        if word not in union_words:
            union_words.append(word)
    return union_words

# Function to create a list of common words in two files and return it
def get_common_words(file1, file2):
    words_file1 = get_unique_words(file1)
    words_file2 = get_unique_words(file2)
    common_words = []
    for word in words_file1:
        if word in words_file2:
            common_words.append(word)
    return common_words

# Function to create a list of words in one file but not in another file and return it
def get_diff_words(file1, file2):
    words_file1 = get_unique_words(file1)
    words_file2 = get_unique_words(file2)
    diff_words = [word for word in words_file1 if word not in words_file2]
    return diff_words

# Function to print word count in a file
def print_word_count(file_name):
    str = ""
    words = get_unique_words(file_name)
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    str += (f"Word Count in {file_name}:\n")
    for word, count in word_count.items():
        str += (f"{word}: {count}\n")
    return str

# Function to read data from a file and return a list of words in a file
def read_file(file_name):
    words = []
    with open(file_name, 'r') as file:
        for line in file:
            for word in line.split():
                word = word.strip(string.punctuation).lower()
                words.append(word)
    return words

# Main function to call all the above functions
def main():
    file1 = input("Enter the name of the first input file: ")
    file2 = input("Enter the name of the second input file: ")
    output_file = "fileAnalysis.txt"

    unique_words_file1 = get_unique_words(file1)
    unique_words_file2 = get_unique_words(file2)
    union_words = get_union_words(file1, file2)
    common_words = get_common_words(file1, file2)
    words_in_file1_not_file2 = get_diff_words(file1, file2)
    words_in_file2_not_file1 = get_diff_words(file2, file1)

    # Write results to the output file
    write_to_file(output_file, ["Unique words in File 1:", *unique_words_file1,
                                "Unique words in File 2:", *unique_words_file2,
                                "Unique words in both files:", *common_words,
                                "Words in both files:", *common_words,
                                "Words in File 1 but not in File 2:", *words_in_file1_not_file2,
                                "Words in File 2 but not in File 1:", *words_in_file2_not_file1,
                                "Words in either File 1 or File 2 but not both:", *[word for word in union_words if word not in common_words],
                                print_word_count(file1),
                                print_word_count(file2)])

    print("Data saved in fileAnalysis.txt")
    

# Run the main function
if __name__ == "__main__":
    main()
