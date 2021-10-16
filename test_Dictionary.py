import math

student={}

while True:
   ans=str(input('You want to add data? y or n: '))
   if ans=='y':
        id_std=str(input('Put ID Student: '))
        name_std=str(input('Put your name'))
        student[id_std] = name_std
        i+=1
        continue
   else:
       print(student)
       break




