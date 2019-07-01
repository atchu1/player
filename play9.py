x,y=input().split(" ")
x=int(x)
y=int(y)    
start=0
for i in range(x,y+1):
    if(i>1):
        for j in range(2,i):
            if(i%j==0):
                break
        else:
           start=start+1
print(start)
