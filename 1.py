<<<<<<< HEAD
"""Task:
Write a Python program to sort the employee records using a lambda expression.

Input:
employees = [("Rahul", 45000), ("Amit", 30000), ("Neha", 55000), ("Priya", 40000)]

Output:
[('Amit', 30000), ('Priya', 40000), ('Rahul', 45000), ('Neha', 55000)] """

"""n = int(input("Enter no of employee: "))
emp = []

for i in range(n):
    name = input(f"Enter {i+1} emp name: ")
    salary = int(input(f"ENter {i+1} emp salary: "))

    emp.append((name,salary))

emp.sort(key=lambda x:x[1])
print(emp)"""

#__________________________________________________________________________

"""Output Format:
Display the updated salaries of all eligible employees after adding a 10% bonus.

Sample Input:
Enter the number of employees:
6

Enter the salaries:
35000 50000 62000 45000 70000 55000

Sample Output:
Eligible Employees' Updated Salaries:
55000.0 68200.0 77000.0 60500.0
'''
def bonus (i):
    return (i/10)+i"""


"""def bonus(i):
     return (i/10)+i

l = list(map(int,input("Enter salary: ").split()))


salaryfilter = list(filter(lambda x: x>=50000,l))
result = map(bonus,salaryfilter)

print(list(result))"""

#1500 2500 1800 3000 4500 1200

"""def discount(i):
    return i-(i/5)

l = list(map(int,input("Enter price : ").split()))

salaryfilter = list(filter(lambda x:x>=2000,l))

result = list(map(discount,salaryfilter))


print(list(result))"""

#65 80 92 74 88 76 55 95

def scholarship(i):
      return i + 5


l= list(map(int,input("Enter student marks: ").split()))
markfilter = list(filter(lambda x: x>= 75,l))

print(markfilter)
result = list(map(scholarship,markfilter))


result.sort(key=lambda x: x,reverse = True)

print(result)







































=======
"""1. Prime Security Code Checker

A high-security research lab uses numeric passcodes to unlock restricted doors. To improve security,
 only prime numbers are accepted because they have exactly two factors and are harder to predict using common patterns.

When an employee enters a code, the system must verify whether the number is prime. If yes, access is granted; otherwise, access is denied.

Write a program to check whether the entered number is Prime or Not Prime.

Input:
29

Output:
Prime Number"""
#______________________________
import math
n = int(input("Enter n:"))

if n <1:
  print("Not Prime")
else:
  i = 2
  while i<=int(math.sqrt(n)): 
     if n%i == 0:
        print("Not Prime")
        break
     i = i+1
  else:
    print("Prime")
>>>>>>> 2ddaf0f7384ccb26d9d69b93f0ec3057ecd5b94e



