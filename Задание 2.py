A = False
B = True
C = False
print('1)', A and B or not A and C)
print('2)', A and C or A and not B)
print('3)', A and C or not A and not C)
print('4)', A and (C or not B) and not C)
