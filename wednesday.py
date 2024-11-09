#number 2
import random

def guess_number ():
    number_guessed = random.randint(1,20)
    while True:
        number = int(input("enter a number"))
        if number == number_guessed:
            print("well guessed")
            break
        else:
            print("incorrect")
guess_number()




#reverse a string
#number 4
def word():
    word = input("enter a word:")
    reverse_word = word[::-1]
    print(f"the reversed word is {reverse_word}")
word()


#number 6
for numbers in range(11):
    if numbers == 4 or numbers == 8:
        continue
    print(numbers)
    
#number12
def count_letters():
    user_input = input("Enter a string: ")
    uppercase_count = 0
    lowercase_count = 0

    for char in user_input:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1

    print(f"Number of uppercase letters: {uppercase_count}")
    print(f"Number of lowercase letters: {lowercase_count}")

count_letters()

# Number 13
def is_valid_password(password):
  Checks if a password meets the specified criteria.

  Args:
      password: The password to validate.

  Returns:
      A tuple containing a boolean (True if valid, False otherwise) and a list of missing criteria (if applicable).
  
  # Minimum length criteria
if len(password) < 8:
 return False, ["Minimum length of 8 characters"]

  # Maximum length criteria
if len(password) > 16:
  return False, ["Maximum length of 16 characters"]
  # Character type checks
has_uppercase = any(char.isupper() for char in password)
has_lowercase = any(char.islower() for char in password)
has_digit = any(char.isdigit() for char in password)
has_special = any(char in "$%&" for char in password)

missing_criteria = []
if not has_uppercase:
    missing_criteria.append("At least 1 uppercase letter (A-Z)")
if not has_lowercase:
    missing_criteria.append("At least 1 lowercase letter (a-z)")
if not has_digit:
    missing_criteria.append("At least 1 number (0-9)")
if not has_special:
    missing_criteria.append("At least 1 special character ($%&)")
  return all([has_uppercase, has_lowercase, has_digit, has_special]), missing_criteria

# Get user input
user_password = input("Enter your password: ")

# Validate the password
# password_is_valid, missing_criteria = is_valid_password(user_password)"""

# Print the results
if valid:
  print("Your password is valid!")
else:
  print("Your password is invalid. Please address the following:")
  for criteria in missing_criteria:
    print(f"\t- {criteria}")
    
#number 39
def check_number ():
    number = float(int(input("enter number")))      
    if number > 0:
       print(f"the {number}is positive")
    elif number< 0:
       print(f"the {number} is negative")
    else:
       print("the {number}is zero")
       
check_number()


# number 8
def multiplication_table(number):
    for i in range(1,13):
        print(f"{number}  * {i} = {number * i}")

number = int(input("Enter a number: "))
multiplication_table(number)


#number 50
for i in range (0,10):
    for j in range(i,-1,-1):
         print(j,end='')
    print()
    
#number 3
rows = 5
for i in range (1, rows +1):
  print('#'* i)
for i in range(rows -1, 0, -1):
  print('#'* i)
  
  
#number 15
def construct_pattern():
    rows = 6
    # Construct the top part of the pattern
    for i in range(1, rows + 1):
        print('#' * i)
    # Construct the bottom part of the pattern
    for i in range(rows - 1, 0, -1):
        print('#' * i)

if __name__ == "__main__":
 construct_pattern() 



      
      
    

        


    

    
    
    
    
        
        
     
    

    
    