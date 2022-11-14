n,m,k = map(int,input().split())
l = list(map(int,input().split()))
temp = k

l.sort(reverse=True)

result = 0
for i in range(m):
    if(temp!=0):
        result+=l[0]
        temp-=1
    else:
        result+=l[1]
        temp=k


print(result)