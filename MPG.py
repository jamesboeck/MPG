def main():
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

if __name__ == "__main__":
    main()
