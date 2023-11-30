def get_intersection(first_name, last_name):
    return set(first_name) & set(last_name)

def get_union(first_name, last_name):
    return set(first_name) | set(last_name)

def get_symmetric_difference(first_name, last_name):
    return set(first_name) ^ set(last_name)

def main():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")

    intersection = get_intersection(first_name, last_name)
    union = get_union(first_name, last_name)
    symmetric_difference = get_symmetric_difference(first_name, last_name)

    print("Intersection:", intersection)
    print("Union:", union)
    print("Symmetric:", symmetric_difference)

if __name__ == "__main__":
    main()
