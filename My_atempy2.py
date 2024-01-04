def get_input(prompt, name):
    while True:
        try:
            value = int(input(prompt))
            if value < 1:
                print(f'Invalid input. {name} should be greater than 0.')
                continue
            else:
                    return value
        except ValueError:
            print('Invalid input. Please enter a number.')

def calculate(old_mileage, current_mileage, gallon_gas):
    miles_driven = current_mileage - old_mileage
    print(f'You drove {miles_driven} Miles')
    mpg = miles_driven / gallon_gas
    print(f'You got {mpg} miles per gallon')

def main():
    while True:
        old_mileage = get_input('Enter your old mileage: ', 'Mileage')
        current_mileage = get_input('Enter your current mileage: ', 'Mileage')
        if current_mileage < old_mileage:
            print('Current mileage should be greater than old mileage.')
            continue

        gallon_gas = get_input('Enter how many gallons you filled up: ', 'Gas')
        calculate(old_mileage, current_mileage, gallon_gas)

        user_answer = input('Would you like to continue? Yes or No: ')
        if user_answer.lower() != 'yes':
            print('Thank you!')
            break  # Exit the loop

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

def calculate_gas_mileage(temp, base_mileage):
    optimal_temp = 77.0  # Optimal temperature in Fahrenheit

    if temp < optimal_temp:
        # Calculate the effect of cold temperature on gas mileage
        temp_effect = (optimal_temp - temp) / 100
        mileage = base_mileage * (1 + temp_effect)
    else:
        # Calculate the effect of hot temperature on gas mileage
        temp_effect = (temp - optimal_temp) / 100
        mileage = base_mileage * (1 - temp_effect)

    # Ensure mileage is not negative
    mileage = max(0, mileage)

    return mileage

def calculate_gas_mileage_main():
    while True:
        while True:
            try:
                temp = float(input('Enter the current temperature in Fahrenheit: '))  # Current temperature in Fahrenheit
                if temp > 212:
                    print('That seems extremely hot. Maybe too hot. Please enter a realistic temperature.')
                elif temp < -212:
                    print('That seems extremely cold. Maybe too cold. Please enter a realistic temperature.')
                else:
                    break
            except ValueError:
                print('Invalid input. Please enter a number.')

        while True:
            try:
                base_mileage = float(input("Enter your current miles per gallon at 77F: "))  # Base gas mileage in MPG at 77F
                if base_mileage <= 0:
                    print('You have entered a non-positive value for gas mileage. Please enter a positive number.')
                else:
                    break
            except ValueError:
                print('Invalid input. Please enter a number.')

        adjusted_mileage = calculate_gas_mileage(temp, base_mileage)
        print(f"The adjusted gas mileage at {temp}F is {adjusted_mileage:.2f} MPG.")

        # Ask the user if they would like to continue
        user_answer = input('Would you like to continue? Yes or No: ')
        if user_answer.lower() != 'yes':
            print('Thank you!')
            break  # Exit the loop

def main_new():
    options = {
        '1': calculate_travel_time,
        '2': main,
        '3': calculate_gas_mileage_main
    }

    while True:
        print('1: Calculate travel time')
        print('2: Calculate MPG for your trip')
        print('3: Calculate the effect of temperature on MPG')
        user_choices = input('Enter the numbers corresponding to your choices, separated by commas: ').split(',')
        for user_choice in user_choices:
            user_choice = user_choice.strip()  # remove leading/trailing spaces
            if user_choice in options:
                optionsuser_choice
            else:
                print(f"Invalid choice: {user_choice}. Please enter a valid number.")

if __name__ == "__main__":
    main_new()
