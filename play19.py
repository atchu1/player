num1=int(input())
for i in range(2,num1+1):
  if(num1%i==0):
    t1=0
    for s in range(2,i+1):
      if(i%s==0) and (s!=i):
          t1=1
          break
    if(t1==0):
print(i,end=" ")
