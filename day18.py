#!/usr/bin/python3
import sys
import itertools as it
import functools as ft
import re
import math

class ll:
  capacity=100
  class node:
    invalid_node=-1
    def __init__(self,data=0,prev=invalid_node,next=invalid_node,bracket=0):
      self.data=data
      self.prev=prev
      self.next=next
      self.bracket=bracket

  def __init__(self):
    self.pool=set(range(ll.capacity))
    self.listy=[ll.node() for _ in range(ll.capacity+1)]
    self.head=-1
    self.tail=-1

  def read_string(self,string:str):
    string+=","
    brackets=0
    data=''
    #it totally depends on the data being consistent and correct
    for i in string:
      if i==",":
        # print(data)
        self.append(int(data),brackets)
        data=''
        brackets=0
      elif i=='[':
        brackets+=1
      elif i==']':
        brackets-=1
      else:
        data+=i

  def __str__(self):
    navig=self.head
    string=''
    while navig!=ll.node.invalid_node:
      if self.listy[navig].bracket>0:
        brackets='['*abs(self.listy[navig].bracket)
        string+=f"{brackets}{self.listy[navig].data},"
      else:
        brackets=']'*abs(self.listy[navig].bracket)
        string+=f"{self.listy[navig].data}{brackets},"
      # print(navig)
      navig=self.listy[navig].next
    return string[:-1:]
  
  def set_ends(self):
    self.listy[ll.node.invalid_node].next=self.head
    self.listy[ll.node.invalid_node].prev=self.tail

  def set_ends_reverse(self):
    self.head=self.listy[ll.node.invalid_node].next
    self.tail=self.listy[ll.node.invalid_node].prev

  def append(self,data,bracket):
    val=self.pool.pop()

    if self.head==ll.node.invalid_node:
      self.head=val
      self.tail=val

      self.listy[val].data=data
      self.listy[val].bracket=bracket
      self.listy[val].prev=ll.node.invalid_node
      self.listy[val].next=ll.node.invalid_node
    else:
      self.listy[val].data=data
      self.listy[val].bracket=bracket
      
      self.listy[val].prev=self.tail
      self.listy[val].next=ll.node.invalid_node
      self.listy[self.tail].next=val
      self.tail=val
    self.set_ends()
    # print(self.head,self.tail)

  def explode(self,val):
    if self.listy[val].prev!=ll.node.invalid_node:
      self.listy[self.listy[val].prev].data+=self.listy[val].data
    val1=self.listy[val].next
    if self.listy[val1].next!=ll.node.invalid_node:
      self.listy[self.listy[val1].next].data+=self.listy[val1].data
    
    _new=self.pool.pop()
    self.listy[_new].data=0
    self.listy[_new].prev=self.listy[val].prev
    self.listy[_new].next=self.listy[val1].next
    self.listy[_new].bracket=self.listy[val].bracket+self.listy[val1].bracket

    self.listy[self.listy[val].prev].next=_new
    self.listy[self.listy[val1].next].prev=_new

    self.pool.update([val1,val])
    self.set_ends_reverse()

  def split(self,val):
    data1=math.floor(self.listy[val].data/2)
    data2=math.ceil(self.listy[val].data/2)
    left_side=max(self.listy[val].bracket,0)
    right_side=min(self.listy[val].bracket,0)

    _new1=self.pool.pop()
    _new2=self.pool.pop()
    
    self.listy[_new1].next=_new2
    self.listy[_new1].data=data1
    self.listy[_new1].bracket=left_side+1
    
    self.listy[_new2].prev=_new1
    self.listy[_new2].data=data2
    self.listy[_new2].bracket=right_side-1

    self.listy[self.listy[val].prev].next=_new1
    self.listy[_new1].prev=self.listy[val].prev
    
    self.listy[self.listy[val].next].prev=_new2
    self.listy[_new2].next=self.listy[val].next

    self.pool.add(val)

    self.set_ends_reverse()

  def print_all(self):
    navig=self.head
    while navig!=ll.node.invalid_node:
      print(f"({self.listy[navig].data},{self.listy[navig].bracket})",end=' ')
      navig=self.listy[navig].next
    print()
    
  def take_action(self)->bool:
    # print("here")
    navig=self.head
    depth=0
    while navig!=ll.node.invalid_node:
      # print(depth)
      depth+=self.listy[navig].bracket
      assert depth<=5,f"depth is: {depth}"
      if depth>4:
        self.explode(navig)
        return True
      # elif self.listy[navig].data>9:
      #   self.split(navig)
      #   return True
      navig=self.listy[navig].next
    navig=self.head
    depth=0
    while navig!=ll.node.invalid_node:
      # print(depth)
      depth+=self.listy[navig].bracket
      assert depth<=5,f"depth is: {depth}"
      # if depth>4:
      #   self.explode(navig)
      #   return True
      if self.listy[navig].data>9:
        self.split(navig)
        return True
      navig=self.listy[navig].next
    return False
  
  def reduce(self):
    while self.take_action():
      # print(self)
      pass

class string_evalutaion:
  def __init__(self,string):
    self.string=''.join([i for i in string if i!=','])[1:-1:]
    self.p=0
  
  def evaluate(self):
    self.p=0
    return self.func()
  
  def func(self):
    forra=self.p
    val=0
    val_arr=[3,2]
    # print("forra started for:",forra)
    for i in val_arr:
      if self.string[self.p].isdigit():
        val+=i*int(self.string[self.p])
        self.p+=1
      else:
        self.p+=1
        val+=i*self.func()
    while self.p<len(self.string) and self.string[self.p]==']':
      self.p+=1
    # print("forra ended with:",val,"for:",forra)
    return val

file_name=sys.argv[1]
file=open(file_name,"r")
instr=[i.strip('\n') for i in file.readlines()]
val_string=''
ans=None
index=0
for x in instr:
  if ans is None:
    ans=ll()
    ans.read_string(x)
    # ans.print_all()
    ans.reduce()
    # ans.print_all()
  else:
    temp_string=f'[{ans.__str__()},{x}]'
    # print(temp_string)
    # break
    ans=ll()
    ans.read_string(temp_string)
    ans.reduce()
  # print(index,ans)
  index+=1

se=string_evalutaion(str(ans))
# print(len(se.string),se.string)
print(se.evaluate())

best=0
for i in range(len(instr)):
  for j in range(len(instr)):
    if i==j:
      continue
    val=f"[{instr[i]},{instr[j]}]"
    val1=ll()
    val1.read_string(val)
    val1.reduce()
    se=string_evalutaion(str(val1))
    best=max(best,se.evaluate())
print(best)
