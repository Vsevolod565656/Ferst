a,b,c=map(int, input().split())
D=b**2-4*a*c

if D==0:
    x=-b/(2*a)
    print(x)
elif D>0:
    x1=-b+D**0.5/2*a
    x2=b+D**0.5/2*a
    print(x1,x2)
else:
    print("кор нет")
