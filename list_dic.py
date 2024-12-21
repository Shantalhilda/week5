
#NO4
# create the list
"""list=[10,50,2,19,14]
smallest_number=min(list)
# print statment
print("the smallest number in the list is :",smallest_number)

#NO3
#the largest number
list =[10,50,2,19,14]

largest_number=max(list)
print("thelargest number is :",largest_number)

#NO1
#summing up all items in a list
list=[2,7,10,11]
#sum of all the iteams 
sum=sum(list)
print("the sum of the items is :",sum)


#NO2
#a program to multiply alll the items in a list 
list=[2,5,7,2]
#multiplying all the items 
product=1
for i in list:
    product*=i
    print(" the multiplication of all numbers is ",product)
    
#NO7
# removing duplicat from a list 
list=[17,12,1,14,15,17,1]







#no 8
# fnding out ifthe list is empty
list=[]
if not list:
    print("empty list ")
else:
    print("list is not empty")
    
#NO 9
#copying a list 
list=[7,8,9,4,6]
#use .copy() 
# copying the list 
copy_list=list.copy()
print(" the copy list ",copy_list)

#NO 22
#adding  a list to secind list
list1=[2,3,4,5]
list2=[6,7,8,9]
# add the two list
list2.append(list1)
print("list 2 after appand",list2)

#NO23
#selecting of a random item from a list
list=[10,12,3,6]
_number = random.randint(list)
print("the random item in the list"),random_number


#NO 24 
#finding the second smallest number 
list=[10,2,4,15]
#organise the list in assending order
organised_list=sorted(list)

#get the second smallest num
second_smallest=organised_list[1]
print("the second smallest number is :",second_smallest)


#dectionary 
#no 3 
dict={'a':1,'b':3,}
key='b'
#find outif the key is n the dict
if key in dict:
    print(f"the {key}is in the dictionary")
else:
    print(f"the {key } is not in the dictionary")
    
#NO4
#using loops for dictionaries 
dict={'a':2,'b':3,'c':4}
for key,value in dict.item():
    print(f"the key{key},value:{value}")
    
    
# TUPLES
#NO 1
# creating a tuple 
tuple=(1,4,6,8)
print(tuple)

#NO2 
# tuple with diffrent elements
tuple=(2,"shantal",2.2)
print(tuple) 


#SETS 
#NO1 
# creating  a set
set={1,2,3,4,5,6,}
print(set)"""

#NO 2 
set={1,3,7,10}
for i in set:
    print(i)