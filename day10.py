import sys
import collections as clc

#reading from file
file_name=sys.argv[1]
file=open(file=file_name)
l=[i.strip("\n") for i in  file.readlines()]

#stack
class stack:
  def __init__(self) -> None:
    self.__st=clc.deque()
  def push(self,x) -> None:
    self.__st.append(x)
  def pop(self):
    if len(self.__st)==0:
      raise MemoryError("Nothing to pop")
    return self.__st.pop()
  def __len__(self)->int:
    return self.__st.__len__()

mapping={
  ')':3,
  ']':57,
  '}':1197,
  '>':25137,
}
open_close_map={
  '(':')',
  '[':']',
  '{':'}',
  '<':'>',
}

mappa=dict(zip(mapping.keys(),range(1,5)))

def complete_rest_stack(st:stack)->str:
  string=""
  while(st.__len__()!=0):
    val=st.pop()
    string+=open_close_map[val]
  return string

def compute_score(string:str)->int:
  magic_number=5
  score=0
  for  i in string:
    score*=magic_number
    score+=mappa[i]
  return score



ans1=0
index=0
s=set()
scores=[]

for string in l:
  st=stack()
  in_index=0
  for i in string:
    if(i in open_close_map.keys()):
      st.push(i)
    else:
      if len(st)==0:
        continue
      val=st.pop()
      if open_close_map[val]!=i:
        ans1+=mapping[i]
        s.add(index)# need for the second part

        # print(i,index,val,in_index)
        break
    in_index+=1
  if(in_index==len(string) and st.__len__()!=0):#means incomplete lines
    scores.append(compute_score(complete_rest_stack(st)))#completes the stack and calcultes score
  index+=1

print(ans1)

scores.sort()

print(scores[(len(scores)-1)//2])#an artistic way of getting the median
