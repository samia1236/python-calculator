num_1 =float(input("enter a number: "))
operator_1 = (input("enter an operator: "))
operator_2 = (input("please enter the sec operator: "))
num_2 =float(input("enter a number: "))
num_3 =float(input("enter a number: "))
if operator_1 ==  "-" and operator_2 == "*":
   print(num_1 + num_2 * num_3)
elif operator_1 == "*" and operator_2 == "*":
    print (num_1 * num_2)
elif operator_1 == "-" and operator_2 == "+":
    print(num_3 - num_2)
else:
    print("Operator not recognised")







