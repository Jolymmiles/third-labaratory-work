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
