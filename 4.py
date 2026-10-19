"""4. Prime Security Code Checker – Advanced

A high-security lab accepts only prime numbered access codes.

When a user enters a number, the software must:

- Check whether number is prime
- If prime, print next immediate prime number
- If not prime, print previous immediate prime number

Write a program using loops only.

Input:
29

Output:
Prime Number
Next Prime = 31"""
#___________________________________
import math
n = int(input("Enter n:"))
prev = n

if n<1:
   print("not Prime number")
else:
  i = 2
  while i<= int(math.sqrt(n)):
     if n%i == 0:
       print("not prime")
       break
     i = i+1
  else:
     print("prime number")

num = n+1
while True:
 count = 0
 for i in range(1,num +1):
     if num%i == 0:
       count +=1
 
 if count == 2:
     print("Next Prime: ",num)
     break

 num += 1
 
print("previous Prime", prev)

else:
    while True :
         i = 2
         while i<= math.sqrt(n): 
               if n%i == 0:
               break
         else:
             print("previous Prime number is ",n)
             flag = 1
         if flag == 1: 
             break
























   


  
   




