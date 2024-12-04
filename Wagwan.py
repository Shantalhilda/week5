def is_odd(number):
    return number % 2 != 0  # Returns True if number is odd, False if even

# Continuously prompt the user for input until a valid number is provided
while True:
    try:
        num = int(input("Enter a number (enter 0 to exit): "))
        
        if num == 0:
            print("Exiting the program.")
            break  # Exit the while loop if the user enters 0
        
        if is_odd(num):
            print(f"{num} is an odd number.")
        else:
            print(f"{num} is not an odd number.")
            
    except ValueError:
        print("Invalid input. Please enter a valid integer number.")

  
