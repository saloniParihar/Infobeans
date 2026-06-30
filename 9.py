"""Even Odd Difference Prime System

A smart scanner counts even and odd digits.

Write a program to:

- Count even digits
- Count odd digits
- Find difference
- Check whether difference is Prime or Not

Input:
123456

Output:
Even Count = 3
Odd Count = 3
Difference = 0
Not Prime"""
#________________________________________
import math
n = int(input("Enter n: "))
even = 0
odd = 0
while n>0:
  d= n%10
  if d%2 == 0:
     even = even+1
  else:
     odd = odd+1
  n= n//10
print("Even count: ",even)
print("odd count: ",odd)


if even > odd:
  diff = even-odd
else: 
  diff = odd-even

print("Difference:", diff)

num = diff
if num<1:
   print("Not Prime")
else:
  i = 2
  while i < int(math.sqrt(n)):
      if num%i == 0:
         print("not Prime")
         break
      i += 1
  else:
     print("Prime")
      
    


     



