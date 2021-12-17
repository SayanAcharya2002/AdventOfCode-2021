#!/usr/bin/python3
import sys
import itertools as it
import functools as ft
import re
import math

#i solved this problem with  an exhausted mind. So it could be that there are some sloppy bugs in the code. Please let me know about that.

#special note: if you are unlucky enough to get a range like : -20...30 for the x coordinate then simply run this algo twice like: for abs(-1) to abs(-20) and 
#then from 0 to 30. This way you will cover both ranges. I did not implement that part as my input was not like that.




def format_string(string:str,pat:str):
  val=re.fullmatch(pat,string)
  if val is None:
    raise BaseException("Pattern or String messed up")
  else:
    return list(map(int,val.groups()))

file_name=sys.argv[1]
file=open(file_name,"r")
l=format_string(file.readline().strip("\n"),r"[a-zA-Z: =]*([+-]?\d+)\.{2}([+-]?\d+),[a-zA-Z =]*([+-]?\d+)\.{2}([+-]?\d+)")


points=[(l[0],l[1]),(l[2],l[3])]
# points=[(217,240),(-126,-69)]
# points=[(20,30),(-10,-5)]
print(points)
ans=0
s=set()
def non_stall():
  global ans
  best=0
  for i in range(points[0][1]+1):
    for j in range(i):
      # diff_x=i**2-j**2
      diff_x=((i+1)*i-(j+1)*j)//2
      if diff_x>=points[0][0] and diff_x<=points[0][1]:
        k=i-j
        low_lim=math.ceil((points[1][0]+k*(k-1)/2)/k)
        up_lim=math.floor((points[1][1]+k*(k-1)/2)/k)
        if low_lim>up_lim:
          continue
        # ans+=up_lim-low_lim+1
        s.update([(i,j) for j in range(low_lim,up_lim+1)])
        y=up_lim
        k=min(k,y)
        best=max(best,int((2*k*y-k*(k-1))/2))
  return best

def stall():
  best=0
  global ans
  for i in it.count(0):
    if i*(i+1)>2*points[0][1]:
      break
    elif i*(i+1)<2*points[0][0]:
      continue
    # print("here",i)
    for k in range(i,max(abs(points[1][1]),abs(points[0][1]))*10):
      
      low_lim=math.ceil((points[1][0]+k*(k-1)/2)/k)
      up_lim=math.floor((points[1][1]+k*(k-1)/2)/k)
      # print(low_lim,up_lim,k)
      if low_lim>up_lim:
        continue
      # ans+=up_lim-low_lim+1
      # s.add((i,range(low_lim,up_lim+1)))
      s.update([(i,j) for j in range(low_lim,up_lim+1)])
      y=up_lim
      k=min(k,y)
      # print(y,k)
      best=max(best,int((2*k*y-k*(k-1))/2))
  return best

print(max(non_stall(),stall()))
print(len(s))

