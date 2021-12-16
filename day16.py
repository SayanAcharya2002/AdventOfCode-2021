#!/usr/bin/python3
import sys
import itertools as it
import functools as ft

file_name=sys.argv[1]
file=open(file_name,"r")
line=file.readline().strip("\n")

class code:
  mappa=dict([(str(i),bin(i)[2:].zfill(4)) for i in range(0,10)]+[(chr(65+i-10),
  bin(i)[2:].zfill(4)) for i in range(10,16)])
  len_mappa={0:15,1:11}

  def __init__(self,string:str)->None:
    self.string=code.make_bin(string)
    self.ver=[]
  
  def run(self):
    return self.parse_string(0)[0]


  @staticmethod
  def make_bin(string:str)->str:
    ans=""
    for i in string:
      ans+=code.mappa[i]
    return ans
 
  def parse_literal(self,p):
    ans=""
    for i in it.count(p,5):
      if self.string[i]=='0':
        ending=i+5
        break
    for i in range(p,ending,5):
      ans+=self.string[i+1:i+5]
    return ans,ending

  @staticmethod
  def take_action(listy:list,id:int):#does the op. Notice that id==4 is purposefully not given
    if id==0:
      return sum(listy)
    elif id==1:
      return ft.reduce(lambda x,y:x*y,listy)
    elif id==2:
      return min(listy)
    elif id==3:
      return max(listy)
    elif id==5:
      return int(listy[0]>listy[1])
    elif id==6:
      return int(listy[0]<listy[1])
    elif id==7:
      return int(listy[0]==listy[1])


  def parse_string(self,p): #returns the value of the parsing operation and the position from where to read next
    version=self.string[p:p+3]
    p+=3
    id=int(self.string[p:p+3],2)
    p+=3
    self.ver.append(version)

    if id==4:
      lit,p=self.parse_literal(p)
      return int(lit,2),p #this is the most basic(root level) return
    
    len_id=int(self.string[p])
    p+=1
    value=int(self.string[p:p+code.len_mappa[len_id]],2)
    p+=code.len_mappa[len_id]

    listy=[]
    if len_id==0:
      upto=p+value
      while p!=upto:
        val,p=self.parse_string(p)
        listy.append(val)
    else:
      for _ in range(value):
        val,p=self.parse_string(p)
        listy.append(val)
    ans=code.take_action(listy,id)
    return ans,p

runner=code(line)
val=runner.run()
print("ans 1:",sum(map(lambda x:int(x,2),runner.ver)))
print("ans 2:",val)
