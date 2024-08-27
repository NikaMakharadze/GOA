import traceback

def calculator():
    try:
        # Get dog age
        age = input("Input dog years: ")
        
        # Cast to float
        d_age = float(age)

        if d_age < 0:
            raise ValueError("Age cannot be a negative number.")

        # Predefined human age values for the first five dog years
        dog_age_multipliers = [15, 12, 9.3, 8, 7.2]

        human_age = 0

        # Calculate dog's age in human years
        for i in range(min(5, int(d_age))):
            human_age += dog_age_multipliers[i] if i == 0 else dog_age_multipliers[i] + 7.2

        # Round the result to 2 decimal places
        human_age = round(human_age, 2)

        # Format the result
        human_age = f"{human_age:.2f}"

        print(f"The given dog age {age} is {human_age} in human years.")

    except ValueError as e:
        print(f"{age} is invalid.")

    except Exception:
        print(f"{age} is an invalid age.")
        print(traceback.format_exc())

calculator()  # This line calls the calculator function
