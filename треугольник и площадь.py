A=list(map(int,input().split()))
A.sort()
s=0
S1=[]
for i in range(len(A)-2):
    if A[i]+A[i+1]>A[i+2]:
        p=(A[i]+A[i+1]+A[i+2])/2
        s=(p*(p-A[i])*(p-A[i+1])*(p-A[i+2]))**0.5
        S1.append(s)
        
print(max(S1))
