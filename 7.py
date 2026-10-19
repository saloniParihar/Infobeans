
""" Prime Sum Lucky Number

A lottery app checks if sum of digits is prime.

Write a program to:

- Find sum of digits
- If prime print Lucky Number
- Else Normal Number

Input:
4528

Output:
Sum = 19
Lucky Number"""
#___________________________
import math
n = int(input("Enter n: "))
sum = 0
while n>0:
   d=n%10
   sum = sum+d
   n = n//10
print("Sum= ", sum)

num= sum
if num<=1:
   print("Normal number")
else:
  i = 2
  while i<=int(math.sqrt(num)):
    if num%i == 0:
       print("Normal number")
       break
    i = i+1
  else:
      print("Lucky number")

  
    
     