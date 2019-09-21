a=5

s="ADADA"
c=0
b=0
for sl in range(a):
    if s[sl]=='A':
        c+=1
    else:
        b+=1
if c>b:
    print("A win")
elif c<b:
    print("D win")
else:print("frendship")