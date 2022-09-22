# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
#                                                        not(X or Y or Z) = notX and notY and notZ

x = int(input('x = '))
y = int(input('y = '))
z = int(input('z = '))

expression1 = not(x or y or z)
expression2 = not x or not y or not z
print(expression1 == expression2)