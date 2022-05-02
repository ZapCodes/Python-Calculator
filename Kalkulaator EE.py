


num1 = int(input("Sisesta esimene numbri paar või number: "))
num2 = int(input("Sisesta teine numbri paar või number: "))

lahendus = input('''
PALUN VALIGE LAHENDUS TÜÜP:
+  LIITMINE
-  LAHUTAMINE
*  KORRUTAMINE
/  JAGAMINE
''')



if lahendus == '+':
    print('{} + {}'.format(num1, num2))
    print(num1 + num2)
elif lahendus == '-':
    print('{} - {}'.format(num1, num2))
    print(num1 + num2)
elif lahendus == '*':
    print('{} * {}'.format(num1, num2))
    print(num1 * num2)
elif lahendus == '/':
    print('{} / {}'.format(num1, num2))
    print(num1 / num2)
else:
    print("TE POLE VALINUD LAHENDUST")
 
 









