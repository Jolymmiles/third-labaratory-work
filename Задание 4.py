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
