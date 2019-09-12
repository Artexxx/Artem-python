m = int(input("write m->"))
n = int(input("write n->"))
a = int(input("write a->"))
x=0
while x == 0:
    x = a % m
    a += 1
while y == 0:
    y = a // n
print(max(x, y))

"""N = int(input('N'))                
b = 0                              
for i in range(N):                 
    a = int(input('a'))            
    b = b + a                      
if b % 7 == 0:                     
    print("yes")                   
else:                              
    print("yes")                   
                    """