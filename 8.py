"""8. Largest Smallest Sum Prime Checker

A number analyzer finds largest and smallest digit.

Write a program to:

- Find largest digit
- Find smallest digit
- Find sum of both
- Check whether sum is Prime or Not

Input:
57294

Output:
Largest = 9
Smallest = 2
Sum = 11
Prime"""

import math
n = int(input("Enter n: "))
largest = 0
smallest = 9

while n>0:
  d = n%10
  if d >largest:
     largest = d
  if d < smallest:
     smallest = d
  n = n//10

digit_sum = largest+smallest
print("Largest: ",largest)
print("Smallest: ",smallest)
print("Sum: ",digit_sum)

temp = digit_sum
if temp<1:
   print("not Prime")
else:
   i = 2
   while i<=int(math.sqrt(temp)):
       if  temp % i == 0:
           print("Not Prime")
           break
       i+=1
   else:
       print("Prime Number")


