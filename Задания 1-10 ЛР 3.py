# Задание 1
X = True
Y = False
Z = False
print('A)', X or not Y or Z)
print('B)', X and Y and Z)
print('C)', X and Y and not Z)
print('D)', not X or Y or not Z)

# Задание 2
A = False
B = True
C = False
print('1)', A and B or not A and C)
print('2)', A and C or A and not B)
print('3)', A and C or not A and not C)
print('4)', A and (C or not B) and not C)

# Задание 3
A = False
B = False
C = True
print('a)', (not A or not B) and not C)
print('b)', (not A or not B) and (A or B))
print('c)', A and B or A and C or not C)

# Задание 4
A = int(input())
B = int(input())
C = int(input())
if (A >= 100) and (B >= 100):
    print('а) True')
else:
    print('a) False')
if (A % 2 == 0) or (B % 2 == 0):
    print('б) True')
else:
    print('б) False')
if (A >= 0) or (B >= 0):
    print('в) True')
else:
    print('в) False')
if (A % 3 == 0) and (B % 3 == 0) and (C % 3 == 0):
    print('г) True')
else:
    print('г) False')
if (((A < 50) and (B > 50) and (C > 50)) or
        ((A > 50) and (B < 50) and (C > 50)) or
        ((A > 50) and (B > 50) and (C < 50))):
    print('д) True')
else:
    print('д) False')
if (A <= 0) or (B <= 0) or (C <= 0):
    print('д) True')
else:
    print('д) False')

# Задание 5
X = int(input())
Y = int(input())
Z = int(input())
if (X % 2 != 0) and (Y % 2 != 0):
    print('a) True')
else:
    print('a) False')
if (X < 20 and Y > 20) or (X > 20 and Y < 20):
    print('b) True')
else:
    print('b) False')
if (X == 0) or (Y == 0):
    print('c) True')
else:
    print('c) False')
if (X < 0) and (Y < 0):
    print('d) True')
else:
    print('d) False')
if (((X % 5 == 0) and (Y % 5 != 0) and (Z % 5 != 0)) or
        ((X % 5 != 0) and (Y % 5 == 0) and (Z % 5 != 0)) or
        ((X % 5 != 0) and (Y % 5 != 0) and (Z % 5 == 0))):
    print('e) True')
else:
    print('e) False')
if (X > 100) or (Y > 100) or (Z > 100):
    print('f) True')
else:
    print('f) False')

# Задание 6
A = int(input())
if A % 2 == 0 or A % 3 == 0:
    print('a) True')
else:
    print('a) False')
if (A % 3 != 0) and (A % 10 == 0):
    print('b) True')
else:
    print('b) False')

# Задание 7
print('x1')
x1 = int(input())
print('x2')
x2 = int(input())
print('x3')
x3 = int(input())
print('x4')
x4 = int(input())
print('x5')
x5 = int(input())
print('x6')
x6 = int(input())
print('x7')
x7 = int(input())
X = (x1 and (not x1 and not x2) and x3 and not x4 and x5 and not x6 and x7)
if X == 1:
    print('True')
else:
    print('False')

# Задание 8
n = int(input())
print('Ответ', 2 ** n)

# Задание 9
import random

x1 = random.randint(0, 1)
x2 = random.randint(0, 1)
x3 = random.randint(0, 1)
x4 = random.randint(0, 1)
x5 = random.randint(0, 1)
x6 = random.randint(0, 1)
print('1)', (x1 and x2) or (x3 and x4) or (x5 and x6))
print('2)', (x1 and x3) or (x4 and x5) or (x6 and x2))
print('3)', (x1 and x4) or (x2 and x5) or (x6 and x3))
print('4)', (x1 and x5) or (x2 and x3) or (x6 and x4))

# Задание 10
print('x1')
x1 = int(input())
print('x2')
x2 = int(input())
print('x3')
x3 = int(input())
print('x4')
x4 = int(input())
print('x5')
x5 = int(input())
print('x6')
x6 = int(input())
print('x7')
x7 = int(input())
print('x8')
x8 = int(input())
print('x9')
x9 = int(input())
print('x10')
x10 = int(input())
print('1)', (x1 or not x2) and (x3 or not x4) and x5 and not x6 and x7 and x8 and not x9 and x10)
print('2)', (x1 and not x2) or (x3 and not x4) or x5 or not x6 and x7 or x8 or not x9 or x10)
print('3)', (not x1 and x2) or (not x3 and x4) or not x5 or x6 or not x7 or not x8 or x9 or not x10)
print('4)', (not x1 or x2) and (not x3 or x4) and not x5 and x6 and not x7 and not x8 and x9 and not x10)
