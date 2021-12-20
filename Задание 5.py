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
