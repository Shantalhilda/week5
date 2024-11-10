#check if the temp is above 30 without else
temperature = float(int(input("enter temperature: ")))
if temperature >= 30 :
   print(f"it's a hot day in Kampala!")
 
 
 #number2
 #check if a student has passed
std_score = int(input("enter the score: "))
if std_score >= 50:
    print(f"Passed")
else:
    print(f"Failed")
 
 
 #number3
 #determine the type of weather
temperature= float(int(input("enter the temperature: ")))
if temperature > 30:
   print(f"Hot")
elif temperature >= 20 and temperature <=30:
 print(f"warm")
else:
   print(f"cool")
 
 
 #number 4
 #check if a person is eligible to vote
citizenship = input("are you a citizen? ")
if citizenship == "yes":
    age = int(input("enter your age: "))
    if age >= 18:
     print(f"you eligible to vote")
registration_status = input("are you registered? ")


#number5
#check for free delivery
total_amount_order = int(input("enter the total amount of order: "))
print(f"welcome to Mbale online store!")
paid_amount = int(input("enter the paid amount: "))
if total_amount_order < 100000:
    print(f"free delivery")
else:
    amount_delivery_fee = 5/100 * total_amount_order
    total_cost = total_amount_order + amount_delivery_fee
    if paid_amount > total_cost :
        print(f"coming right up")
    else:
        print(f"Please pay some more")
        
        
        
#NUMBER6
#transportation per trip
"""fee_per_trip =  1500
number_of_trips = 3 * 7
total_cost = fee_per_trip * number_of_trips
print(f"total cost is: {total_cost}")"""




#number7
#concatenation per trip
city1 = "Kampala"
city2 = "Entebbe"
single_string = city1 + city2
print(single_string)

#number8
word = "Uganda Martyrs University"
print(len(word.split()))


#number9
#convert to uppercase
sentence = "kampala is the capital city of uganda"
uppercase = sentence.upper()
print(uppercase)

#number10
#convert t lowercase
sentence = "The Source of the Nile "
lowercase = sentence.lower()
print(lowercase)

#number 11
#substring finder
sentence = "The Nile River is the longest river in the world"
print(sentence.replace("Nile","Vctoria"))

#number 12
#length of sentence
sentence = "Ugandan Matoke"
length_sentence = len(sentence.split())
print(f"length of sentence is{length_sentence}")

#number 13
#modulus operator
total_number_students = 45
students_no_group = total_number_students % 6
print(students_no_group)


#number 14
maizeflour_price = 2500*10 > 20000
print(maizeflour_price)


#number 15
cost = (5 * 1000) + (10 * 200) + (3 * 1500)
print(cost)







     
 