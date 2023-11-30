def printTable(entries):
    for entry in entries:
        print(f"{entry[0]} {entry[1]}")

def convertToEntriesList(dict):
    return list(dict.items())

def sortByKeys(entries):
    return sorted(entries, key=lambda x: x[0])

def sortByValues(entries):
    return sorted(entries, key=lambda x: x[1])

def main():
    dict = {'a': 15, 'c': 35, 'b': 10}
    print(f"Keys: {' '.join(list(dict.keys()))}")
    print(f"Values: {' '.join(map(str, dict.values()))}")
    print("Key-Value pairs")
    entries = convertToEntriesList(dict)
    printTable(entries)
    print("")
    print("Key-Value pairs - sorted by key")
    printTable(sortByKeys(entries))
    print("")
    print("Key-Value pairs - sorted by value")
    printTable(sortByValues(entries))
    print("")

if __name__ == "__main__":
    main()
