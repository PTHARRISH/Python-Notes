# Task 1 : print 1 to 100 exclude [32,77,86]
x=[i for i in range(1,101) if i not in [32,77,86]]
print(x)


x[:]=range(1,101) 
x.remove(32)
x.remove(77)
x.remove(86)
print(x)