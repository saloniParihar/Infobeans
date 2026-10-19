import math

def perfect_number():
       num = int(input("Enter number to check it is perfect or not: "))
       sum_ = 0
       for i in range(1,num):
              if num % i == 0:
                      sum_ += i
       if sum_ == num:
           return f"{num} is a perfect number"
       else:
           return f"{num} is not a perfect number" 


def prime_no():
       num = int(input("Enter number to check whether it is prime or not: "))
       if num <0:
          return f"{num} is not a prime number"
         
       else:
           for i in range(2,int(math.sqrt(num))+1):
                 if num % i == 0:
                      return f"{num} is  not a prime number"
                      break
                       
           return f"{num} is a prime number"  

def reverse_no():
         rev = 0
         num = int(input("Enter number to reverse: "))
         while num>0:
               digit =num%10
               rev = (rev*10)+digit
               num //= 10
         return rev

def factorial_no():
       num = int(input("Enter number to find factorial: "))
       factorial = 1
       for i in range(1,num+1):
              factorial *= i
       return factorial 

def factors():
      num = int(input("Enter number to find:"))
      fact = []
      for i in range(1,num+1): 
           if num%i == 0:
             fact.append(i)
      return fact        
    

def display():
     
      print("Choose one choice from the menu")
      print("""

   MENU

1. Check Perfect Number
2. Check Prime Number
3. Find Reverse of a Number
4. Calculate Factorial
5. Display Factors of a Number
6. Exit """)


while True:
      display()
      choice = int(input("\nEnter your choice:"))
      match choice :
               case 1:
                   print(perfect_number())
               case 2:
                   print(prime_no())
               case 3:
                   print(reverse_no())
               case 4:
                   print(factorial_no())
               case 5: 
                   print(factors())
               case 6:
                   print("Exiting...")
                   break
               case _:
                   print("Invalid! Enter your choice first")

 
      print("-------------------------------------------------")         
      ch = input("Do you want to continue or not(YES/NO)").lower()
      if ch == "yes":
           continue
      elif ch == "no":
            print("Thank you")
            break
      else:
            print("Invalid")
            print("Enter your choice")
           






























