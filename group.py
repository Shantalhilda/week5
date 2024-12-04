#Number 1
#list of array of course work marks
CourseWorkMarks = [34.4, 45,23.9,10.2]
#total number of items
totalNumberOfElements = len(CourseWorkMarks)

#total for sum using for for loop
for x in CourseWorkMarks:
    x = sum(CourseWorkMarks)
    print(x)

#formula for the Average
average = x/totalNumberOfElements
#output for average
print('Average =', average)


#Number 2
#for loop to find the largest number in a list of intergers
list = [15,42,73,29,91,50]


#variable to store largest number
largestNumber =list[0]

#using for loop to find the largest number
for y in list[1:]:
    if y > largestNumber:
        largestNumber = y
print('The Largest Number is :', largestNumber)


#Number 3
#use while loop to filter out the even numbers from a list of integers
mylist = [12,17,24,29,36,43,50]

#Initialize an empty list to store even numbers
even_numbers = []

#Initialize index for while loop
n = 0
while n < len(mylist):
    #Check if the number is even
    if mylist[n] % 2 == 0:
         # Append even number to even_numbers list
        even_numbers.append(mylist[n]) 
    #Move to the next element in the list
    n+= 1  

#Print the even numbers found
print("Even numbers in the list:", even_numbers)



#Number 4
def is_odd(number):
    # Check if the number is odd
    return number % 2 != 0

# Continuously prompt the user for input until a valid number is provided
while True:
    user_input = input("Enter a number (enter 'exit' to exit): ")

    # Check if the user wants to exit
    if user_input.lower() == 'exit':
        print("Exiting the program.")
        break
    
    # Check if the input is a valid integer
    if user_input.isdigit():
        num = int(user_input)
        if is_odd(num):
            print(f"{num} is an odd number.")
        else:
            print(f"{num} is not an odd number.")
    else:
        print("Invalid input. Please enter a valid integer number.")



    