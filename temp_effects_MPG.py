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

def main():
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

if __name__ == "__main__":
    main()
