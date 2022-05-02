from ast import If


num1 = int(input("SISESTAGE NUMBER *1* :"))
num2 = int(input("SISESTAGE NUMBER *2* :"))

type = input('''
PLEASE INSERT AN TYPE OF CALCULATION
+  ADDITION
-  SUBTRACTION
*  MULTIPLY
/  DIVIDE
''')


if type == '+':
    print("{} + {} =".format(num1, num2))
    print(num1 + num2)
elif type == '-':
    print("{} - {} =".format(num1, num2))
    print(num1 - num2)
elif type == '*':
    print("{} * {} =".format(num1, num2))
    print(num1 * num2)
elif type == '/':
    print("{} / {} =".format(num1, num2))
else:
    print("YOU DIDNT CHOOSE ANY CALCULATION TYPE")