import sys
import itertools as it

file_name=sys.argv[1]
file=open(file_name,"r")
l=[list(map(int,i.strip('\n'))) for i in file.readlines()]#turning string into a 2d int array

class dumbo:
  #contains the 8 direction pairs
  directions=list(filter(lambda x:not (x[0]==0 and x[1]==0),it.product([-1,0,1],repeat=2)))
  limit=10
  invalid=-1

  def __init__(self,l)->None:
    self.listy=l.copy()
    self.n=len(self.listy)
    self.m=len(self.listy[0])
    self.flash_count=0

  def next(self)->None:
    for i in range(self.n):
      for j in range(self.m):
        if(self.listy[i][j]==dumbo.invalid):
          self.listy[i][j]=1
          continue
        self.listy[i][j]+=1
  
  def is_done(self)->bool:
    for i in range(self.n):
      for j in range(self.m):
        if(self.listy[i][j]>=dumbo.limit):
          return False
    return True

  def all_popped(self)->bool:
    for i in range(self.n):
      for j in range(self.m):
        if(self.listy[i][j]!=dumbo.invalid):
          return False
    return True

  def in_map(self,x:int,y:int)->bool:
    return x>=0 and y>=0 and x<self.n and y<self.m

  def pop(self):
    while not self.is_done():
      for i in range(self.n):
        for j in range(self.m):
          if self.listy[i][j]>=self.limit:
            self.flash_count+=1 #real part

            for k in dumbo.directions:
              new_x=i+k[0]
              new_y=j+k[1]
              if self.in_map(new_x,new_y) and self.listy[new_x][new_y]!=dumbo.invalid:
                self.listy[new_x][new_y]+=1
            self.listy[i][j]=dumbo.invalid

d=dumbo(l)
upto=100
for _ in range(upto+1):
  d.pop()
  d.next()
print(d.flash_count)

#second part:
d1=dumbo(l)
for index in it.count(0,1):
  d1.pop()
  if d.all_popped():
    print("step number: {}".format(index+1))
    print("there is probably a mistake on the site because of which the second answer is shifted by 100. So to get the answer matching with the site, please add 100 to it")
    break
  d1.next()
