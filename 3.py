"""3. Composite Number Detector

A product testing company labels batch numbers as risky if they have more than two factors. Such numbers are known as composite numbers and indicate repeated grouping patterns.

The quality control officer enters a batch number, and the software checks whether it is Composite or Not.

Write a program to check whether a number is Composite or Not.

Input:
12

Output:
Composite Number"""
#______________________________________________
n = int(input("Enter n: "))
count = 0

for i in range(1, n+1):
  if n%i == 0:
     count = count + 1
  
  
if count > 2:
    print("Composite number")
   
else:
    print("Not Composite number")
  
