#while loop
condition = 10
while condition >= 1:
    print(condition)
    condition = condition -1
    
    
#natural numbers
sum = 0
condition = 1
while condition <= 20:
    total_sum = sum + condition
    print(total_sum)
    condition = condition + 1
    
    
    
#even numbers
condition = 1
while condition <= 50:
    if condition % 2 == 0:
        print(condition)
    condition = condition + 1
    
#password 
correct_password = "shantal"
#number of attempts
attempts = 3
while attempts<=3:
    password = input("enter password")
    if password == correct_password:
        print("access granted")
        break
    else:
        print("access denied")
        attempts = attempts - 1

        
        
#prime numbers less than 20
condition = 2
while condition < 20:
    is_prime = True
    for i in range(2, condition):
        if condition % i == 0:
            is_prime = False
            break
    if is_prime:
        print(condition)
    condition = condition + 1
        
        
        
#user input sum
total_sum = 0
number = int(input('enter a number(or 0 to exit): '))
# while loop
while number !=0:
    total_sum = number + total_sum
    number = int(input('enter a number(or 0 to exit):'))
    print(f"the total sum is: {total_sum}")



    
        
    
    
    


    
