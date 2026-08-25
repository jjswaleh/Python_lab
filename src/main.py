from utils import square, is_even, celsius_to_fahrenheit, greet

def main():
    # Ask for a name first
    user_name = input("Enter your name: ")
    print(greet(user_name))
    print("-" * 30)

    try:
        user_input = float(input("Enter a number: "))
        
        # Calculate results
        sq_val = square(user_input)
        even_check = is_even(user_input)
        fah_val = celsius_to_fahrenheit(user_input)
        
        # Print results
        print(f"Square: {sq_val}")
        print(f"Is even: {even_check}")
        print(f"Fahrenheit equivalent: {fah_val}")
        
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
