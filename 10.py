"""Count Prime Scanner

A banking system checks account numbers.

Write a program to:

- Count zero digits
- Find sum of digits
- Add zero count and sum
- Multiply by smallest digit
- Check whether final result is Prime or Not

Input:
908406

Output:
Zero Count = 2
Sum = 27
Smallest Digit = 0
Final Result = 0
Not Prime"""

#___________________________________________
import math
n = int(input("Enter n: "))
temp = n
count = 0
Digit_sum = 0
smallest = 9

while n>0:
  d= n%10
  if d == 0:
     count+= 1
  Digit_sum = Digit_sum+d
  if d<smallest:
     smallest = d
  n =n//10


print("Zero count:",count)
print("sum:",Digit_sum)
print("smallest: ",smallest)

final_result = temp*smallest
print("Final result: ",final_result)


#check prime
if final_result<1:
  print("Not Prime")
else: 
  i =2
  while i<=int(math.sqrt(final_result)):
     if final_result%i == 0:
        print("Not Prime")
        break
     i += 1
  else:
     print("Prime")







