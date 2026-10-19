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










































