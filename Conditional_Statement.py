#Vote count or not
age = int(input("Age : "))
if(age >= 18):
    print("Vote counted...")
elif(age < 18):
    print("Vote not counted! ")
    print("Underage...")
else:
    print("Not valid...")

#Trafic light
light = input("light color :")
if(light == "red"):
    print("Stop")
elif(light == "Green"):
    print("Go")
elif(light == "Yellow"):
    print("look")
else:
    print("light is broke")

# Grade of Student
marks =int(input("marks : "))
if(marks >= 90):
    print("A+")
elif(marks >= 80 and marks <90): 
    print("A")
elif(marks >=70 and marks < 80):
    print("B+")
elif(marks>=60 and marks <70):
    print("C+")
elif(marks>=50 and marks <60):
    print("C")
else:
    print("fail")


# practice
A = int(input("A : "))
G = input("M/F : ")
if((A==1 or A==2) and G == "M"):
    print("fee is 100")
elif(A==3 or A==4 or G == "F"):
    print("fee is 200")
elif(A==5 and G == "M"):
    print("fee is 300")
else:
    print("no fee")

#single line If/Ternary Operator

#<var> = <var1> if <condition > else <var2>

food = input("food : ")
eat = "Yes" if food == "Cake" else "no"
print(eat)

#<statement1_print> if <condition> else <statement2_print>

food = input("food :")
print("sweet") if food == "cake" or food == "jalebi" else print("not sweet")


#Clever if/ Ternary Operator

#<var> = (false_val,true_val)[<condition>]

age = int(input("age :"))
vote = ("yes","no") [age < 18]
print(vote)

sal = float(input("age : "))
tax = sal*(0.1,0.2)[sal<=50000]
print(tax)

