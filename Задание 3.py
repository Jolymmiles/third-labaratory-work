A = False
B = False
C = True
print('a)', (not A or not B) and not C)
print('b)', (not A or not B) and (A or B))
print('c)', A and B or A and C or not C)
