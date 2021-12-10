import math

l=list(map(int,input().split(',')))
l.sort()
size=len(l)

#for the first one median will give the best value. in case of 2 medians anything between the two medians will give the best result
x=l[len(l)//2]
ans=0
for i in l:
  ans+=abs(i-x)
print(x)
print(ans)

#for the second part the mean will give the best value. now i tried on the 2 sides to see on which side, the best value is
x1=math.ceil(sum(l)/size)
x2=math.floor(sum(l)/size)
print(x1)
print(x2)

ans1=0
ans2=0
for i in l:
  val1=abs(i-x1)
  val2=abs(i-x2)
  ans1+=(val1*(val1+1))/2
  ans2+=(val2*(val2+1))/2
print(ans1,ans2)
