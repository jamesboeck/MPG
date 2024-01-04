def calculate_travel_time():
    while True:
        try:
            user_miles = int(input('Enter how many Miles you have: '))
            if user_miles > 196900000:
                print('The earth is not that big.')
                continue
        except ValueError:
            print('You must enter a number for miles.')
            continue

        while True:
            try:
                user_speed = int(input('Enter your speed in MPH: '))
                if user_speed == 0:
                    print('You would be infinitely traveling.')
                    continue
                break
            except ValueError:
                print('You must enter a number for speed.')

        time = (user_miles / user_speed)
        hours = int(time)
        minutes = round((time - hours) * 60, 2)
        time_str = f'{hours} hour(s) {minutes} minute(s)' if hours else f'{minutes} minute(s)'
        print(f'Time: {time_str}')

        user_answer = input('Would you like to continue? Yes or No: ')
        if user_answer.lower() != 'yes':
            print('Thank you!')
            break

if __name__ == "__main__":
    calculate_travel_time()