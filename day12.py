#!/usr/bin/python3
import sys
import collections as clc

file_name=sys.argv[1]
file=open(file_name,"r")

edge=clc.defaultdict(set)
biggie=dict()

def calc_biggie(big:dict,x:str)->None:
  if big.get(x) is None:
    big[x]=(x==x.upper())

for i in file.readlines():
  i=i.strip("\n")
  a,b=i.split('-')
  calc_biggie(biggie,a)
  calc_biggie(biggie,b)

  if a=='start':
    edge[a].add(b)
  elif b=='end':
    edge[a].add(b)
  else:
    edge[a].add(b)
    edge[b].add(a)

ans=[]
temp_l=[]
temp_s=set()

print("For the first answer put token=False before calling the path")
print("For the second answer put token=True before calling the path")


token=True

def path(x:str)->None:
  global token
  if x=="end":
    ans.append(temp_l.copy())
    return
  for i in edge[x]:
    if i=="start":
      continue
    if not biggie[i] and i in temp_s:
      if token:
        token=False
        temp_l.append(i)
        path(i)
        temp_l.pop()
        token=True
      continue
    if not biggie[i]:
      temp_s.add(i)
    temp_l.append(i)
    path(i)
    if not biggie[i]:
      temp_s.remove(i)
    temp_l.pop()

temp_l.append("start")
temp_s.add("start")
print(f"token currently set to: {token}")

path("start")

print(len(ans))
# for index in range(len(ans)):
#   print(f"index: {index}.")
#   print(ans[index])
