# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

day = int(input('Enter the day of the week: '))
if day >= 6:
    print('Yes')
else:
    print('No')