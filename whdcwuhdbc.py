# Program to check the age entered by the user

def check_age():
    try:
        age = int(input("Enter your age: "))
        if age < 0:
            print("Age cannot be negative.")
        elif age < 18:
            print("You are a minor.")
        elif age < 65:
            print("You are an adult.")
        else:
            print("You are a senior citizen.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    check_age()