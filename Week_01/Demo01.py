# Python Calculator 
# Operator =input("Enter Operator (+  -  *  /)")
# num1=float(input("Enter First Number : "))
# num2=float(input("Enter Second Number : "))

# if Operator== "+":
#     result=num1+num2
#     print("Result : " , result)
# elif Operator == "-":
#     result=num1-num2
#     print("Result : " ,  result)
# elif Operator == "*":
#     result=num1*num2
#     print("Result : " , result)
# elif Operator == "/":
#     result=num1/num2
#     print("Result : " , result)
# else:
#     print( f"{Operator} is not valid Operators ")


#using switch case 
# keepRuning=True
# while(keepRuning):
    
#     print("1. Addition  ")
#     print("2. Subtraction ")
#     print("3. Multiplication")
#     print("4. Division")
#     print("5. Integer Division")
#     print("6. Exit")
#     choice=int(input("Choose your Option "))
#     x=float(input("Enter First Number :  "))
#     y=float(input("Enter Second Number :  "))
#     match choice:
#         case 1:
#             result= x+y
#             print("Result : ", result)
           
#         case 2:
#             result =x-y
#             print("Result : ", result)
            

#         case 3 :
#             result =x*y
#             print("Result : ", result)
            
#         case 4:
#             result= x/y
#             print("Result : ", result)
            
#         case 5:
#             result=x//y 
#             print("Result : ",result )
            
#         case 6:
#             keepRuning=False    
            
#         case _:
#             print(" Please choose valid option ") 
             

cord=(10,20)
x,y=cord
print(x)
print(y)

my_list=[10,20,20,20,30,40,50]
print(my_list)
print(set(my_list))


from ..PythonLab.greet import greeting,afternoonGreeting
print(greeting("ayan"))



