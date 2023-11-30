def main():
    capitals = {}
    
    while True:
        user_input = input("Enter a country and a capital comma separated (Q to quit): ")
        if user_input.lower() == 'q':
            break
        
        country, capital = user_input.split(',')
        capitals[country.strip()] = capital.strip()
    
    print("\nCOUNTRY             CAPITAL")
    for country, capital in sorted(capitals.items()):
        print(f"{country.ljust(20)} {capital.ljust(20)}")

if __name__ == "__main__":
    main()
