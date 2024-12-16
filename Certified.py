#coursework and attendance
course_work_score = float(input("enter course_work_score: "))
if course_work_score >= 17.5:
   print("you are allowed to do the exam")
   attendance = float(input('enter the attendance: '))
   if attendance >= 75:
       print("you are allowed to do the exam")
       exam_mark = float(input("enter the exam mark: "))
       if exam_mark >= 17.5:
         print("Congratulations you have been promoted to year 1 semester 2")
       else: 
           print("Sorry, you have not been promoted")
            
   else: 
       print("you are not allowed to do exam")   
           
    
else: 
    print("sorry, you are adviced to retake this course")