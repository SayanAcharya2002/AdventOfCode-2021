#!/usr/bin/python3
import sys
import collections as clc

file_name=sys.argv[1]
file=open(file_name,"r")
lines=file.readlines()
s=lines[0].strip("\n")
lines=lines[2::] #skipping the first two lines
mappa={}
for i in lines:
  i=i.strip('\n')
  KEY=i[:2:]
  VALUE=i[-1]
  mappa[KEY]=VALUE


extremity=s[0]+s[-1]
total=clc.Counter()
for i in range(len(s)-1):
  total[s[i:i+2]]+=1

def new_map(total:clc.Counter,mappa:dict):
  temp=clc.Counter()
  for i in total.items():
    if mappa.get(i[0]) is None:
      temp.update(i)
      break
    new=[{i[0][0]+mappa[i[0]]:i[1]},{mappa[i[0]]+i[0][1]:i[1]}]
    for j in new:
      temp.update(j)
  return temp

def get_all(total:clc.Counter,extremity:str):
  ans=clc.Counter()
  for i in total.items():
    ans[i[0][0]]+=i[1]
    ans[i[0][1]]+=i[1]
  ans[extremity[0]]+=1
  ans[extremity[1]]+=1
  return ans

iter_no=40
for i in range(iter_no):
  total=new_map(total,mappa)
ans=get_all(total,extremity)

full=ans.most_common()
# print(full)
print((full[0][1]-full[-1][1])//2)
