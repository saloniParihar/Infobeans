"""=====================================================================
QUESTION 2: STUDENT RESULT PROCESSING
=====================================

A training institute wants to manage student records using NamedTuple.

Fields:
roll_no, name, course, marks

Requirements:

1. Read N student records from the user and store them in a list of NamedTuples.

---

2. Display all student details.

---

3. Find and display the topper of the class.

---

4. Count and display the number of students scoring above 80 marks.

---

5. Calculate and display the average marks.

---

6. Accept a course name from the user and display all students enrolled in that course.

---

Test Case:

Input:
Enter number of students: 4

1 Ravi Python 85
2 Anjali Java 78
3 Karan Python 92
4 Pooja Testing 88

Enter course: Python

Expected Output:
Topper:
3 Karan Python 92

Students Above 80:
3

Average Marks:
85.75

Students in Python Course:
1 Ravi Python 85
3 Karan Python 92"""

#=====================================================================
from collections import namedtuple


student = namedtuple("student",["r_no","name","course","marks"])
n = int(input("Enter number of student: "))
list=[]
for i in range(n):
     print(f"Enter student {i+1} Detalis ") 
     r_no = input("Enter roll_no      :")
     name = input("Enter name         :")
     course = input("Enter courses    :")
     marks = input("Enter marks       :")
     list.append(student(r_no,name,course,int(marks)))
     print(f"Students {i+1} details  stored >>>")
     print()

print(list)
print("All Student Details")

count = 1
for i in list:
      print(f" {count}th student details")
      print(f"roll_no  : {i.r_no}")
      print(f"name     : {i.name}")
      print(f"course   : {i.course}")
      print(f"marks    : {i.marks}")

      count += 1
      print()

max = list[0]
for i in list:
   if i.marks > max.marks:
         max= i

print("Topper")
print(f"marks    : {max.marks}")
print()

print(f"Students who got above 80")
count = 0
for i in list:
   if i.marks > 80:
       count += 1
print(count)

sum = 0
for i in list:
    sum += i.marks

avg = sum/n
print(f"average : {avg}")

c = input("Enter course: ")
print("Students course")
for i in list:
     if i.course == c:
        print(f"roll_no   :{i.r_no})
        print(f"roll_no   :{i.name})
        print(f"roll_no   :{i.course})
        print(f"roll_no   :{i.marks})
    

   



 

      

      


































