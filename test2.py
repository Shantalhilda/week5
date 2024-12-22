#grading
"""std_marks = int(input("enter students marks: "))
if std_marks >= 95:
    print(f"you have A") 
elif std_marks >=80:
    print(f"you have B")
elif std_marks >= 70:
    print("you have C")
elif std_marks >= 60:
    print(f"you have a D")
elif std_marks >=55:
    print(f"you have E")
else:
    print(f"you have F")"""
    
    
#Open/close files
with open ("Shopping_list.txt","r") as f:
    content = f.read()
    print(content)
    
                