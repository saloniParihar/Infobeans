def display():
    print("*"*30)
    print("\nStudent Result System")
    print("*"*30)

    print()

    print("\nChoose your choice from the menu: ")


    print("""
          
1. Add Student Details
2. Calculate Total Marks
3. Calculate Percentage
4. Find Grade
5. Display Complete Result
6. Find Highest Subject Mark
7. Find Lowest Subject Mark
8. Exit
""")

    
def add():
      print("Add student details")
      print()

      name = input("Enter name: ")
      roll_no = int(input("Enter roll no: "))

      marks = []
      for i in range(5):
              mark = int(input(f"Enter mark {i+1} :"))
              marks.append(mark)

      studentDB.append(name)
      studentDB.append(roll_no)
      studentDB.append(marks)

      print("Student Details saved successfully...")

def total(studentDB):
         sum = 0
         for i in studentDB[2]:
                sum += i
         return sum

def percent():     
     return (total(studentDB)/500)*100

def high(studentDB):
       max = 0
       for i in studentDB[2]:
            if i > max:
                max = i
       return max

def low(studentDB):
      min = float("inf")
      for i in studentDB[2]:
          if i<min:
             min = i
      return min

def Grade():
      result = percent()
      if 90 < result<=100:
            return "A+"
      elif 80 < result <= 90:
            return "A"
      elif 70 <result <= 80:
            return "B"
      elif 60 <result <= 70:
            return "C"
      elif 50 < result <= 60:
            return "D"
      else:
            return "Fail"

def displayresult(studentDB):
        print("\n"+"*"*30)
        print("---Result Card----")
        print("*"*30)
        

        print(f"Name         :  {studentDB[0]}")
        print(f"Roll_no      :  {studentDB[1]}")
        print("marks")

        for i in range(len(studentDB[2])):
                print(f"Marks {i+1}: {studentDB[2][i]}")

        print(f"Total        : {total(studentDB)}")
        print(f"Percent      : {percent()}%")
        print(f"Grade        : {Grade()}")
        print(f"Highest mark : {high(studentDB)}")
        print(f"Lowest mark  : {low(studentDB)}")

studentDB = []

while True:
         display()
         
         choice = int(input("\nEnter your choice: "))
         
         match choice:
               case 1:
                    add()
               case 2:
                    print(f"\nTotal Marks :{total(studentDB)}")

               case 3:
                    print(f"\npercentage : {percent()}%")
               case 4:
                    print(f"\nGrade      : {Grade()}")
               case 5:
                    displayresult(studentDB)
               case 6: 
                    print(f"Highest Marks: {high(studentDB)}") 
               case 7: 
                    print(f"\nLowest Mark  : {low(studentDB)}")
               case 8:
                    print("\nExisting...")
                    break
               case _:
                     print("\nInvalid choice ")
                     print("\nEnter right choice from the Menu")
                     
                    

         ch = input("Do you want to Continue(YES/NO):").lower()

         if ch == "yes":
             continue

         elif ch == "no":
             print("Thank you")
             break

         else:
            print("Invalid choice")              




















          












            


      


 
























     
            
    
      
   




    
    
    