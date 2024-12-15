#number10
"""name = "shantal"
 
 reverse_word = name[::-1]
print(reverse_word)"""


#number12
"""message = ("hello world!")
split= "hello world".split
reversed_word= message
return ''. join(reversed_word)"""


#number16
"""std_name = input("enter your name:")
sum_of_digits = len(std_name)
print(sum_of_digits)"""

#number18
user_name = input("enter yor user_name: "
uppercase = 0
lowercase = 0
numericvalues = 0
specialchacters = 0
for char in user_name:
    if char.isupper:
        uppercase +=1
        if char.isnumeric:
                numericvalues +=1
    elif char.islower:
        lowercase += 1
    elif char.s:
        specialcharacters+= 1
print(f"the number of lowercase is{lowercase}")
print(f"the number of uppercase is {uppercase}")
print(f"the number of numericvalues is {numericvalues}")
print(f"thenumber of specialcharacters is {specialcharacters}")
    






 
