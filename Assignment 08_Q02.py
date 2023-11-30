

def main():
    rooms = {
        'CS101': 3004,
        'CS102': 4501,
        'CS103': 6755,
        'NT110': 1244,
        'CM241': 1411,
    }
    instructor = {
        'CS101': 'Haynes',
        'CS102': 'Alvarado',
        'CS103': 'Rich',
        'NT110': 'Burke',
        'CM241': 'Lee',
    }
    time = {
        'CS101': '8:00 a.m.',
        'CS102': '9:00 a.m.',
        'CS103': '10:00 a.m.',
        'NT110': '11:00 a.m.',
        'CM241': '1:00 p.m.',
    }

    user_input = ''
    while True:
        user_input = input('Enter a course number (`e`/`exit` to quit): ')
        if user_input == 'exit' or user_input == 'e':
            break
        elif (not user_input in rooms):
            print(f"{user_input} is an invalid course number")
        else:
            print(f"The details for course {user_input} are")
            print(f"Room: {rooms[user_input]}")
            print(f"Instructor: {instructor[user_input]}")
            print(f"Time: {time[user_input]}")
        print("")

if __name__ == "__main__":
    main()
