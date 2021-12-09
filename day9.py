import sys
import io
import itertools as it
import collections as clc

#file name is taken as commandline arguement

file_name=sys.argv[1]
file=io.FileIO(file_name,"r")
l=[]
for i in file:
  i=str(i,"utf-8").strip("\n")
  l.append(i)
n=len(l)
m=len(l[0])

def within_map(x,y):
  return x>=0 and y>=0 and x<n and y<m

score=0
# print(l)
pair=list(filter(lambda x:bool(x[0])^bool(x[1]),it.product([-1,0,1],repeat=2)))

for ij in it.product(range(0,n),range(0,m)):
  i=ij[0]
  j=ij[1]

  valid=True
  for p in pair:
    # print(i,j)
    if within_map(p[0]+i,p[1]+j):
      # print(l[i+p[0]][j+p[1]],l[i][j])
      if int(l[i+p[0]][j+p[1]])<=int(l[i][j]):
        valid=False
        break
  if valid:
    score+=int(l[i][j])+1
    # print(i,j)
print(score)

#part 2

invalid_char=9
mappa=[list(map(int,x)) for x in l]
# for ij in it.product(range(n),range(m)):
#   i=ij[0]
#   j=ij[1]
#   if mappa[i][j]==9:
#     mappa[i][j]=invalid_char #invalidating 9 points
# print(*mappa,sep="\n")
mappa_lens=[]
def bfs(x,y):
  q=clc.deque()
  q.append((x,y))
  bfs_size=0
  while len(q)!=0:
    tup=q.popleft()
    bfs_size+=1
    # print(tup[0],tup[1])
    for p in pair:
      if within_map(p[0]+tup[0],p[1]+tup[1]) and mappa[p[0]+tup[0]][p[1]+tup[1]]!=invalid_char:
        q.append((p[0]+tup[0],p[1]+tup[1]))
        mappa[p[0]+tup[0]][p[1]+tup[1]]=invalid_char
  mappa_lens.append(bfs_size)
for ij in it.product(range(n),range(m)):
  i=ij[0]
  j=ij[1]
  if mappa[i][j]!=invalid_char:
    mappa[i][j]=invalid_char
    bfs(i,j)
    # print(*mappa,sep="\n")
    # print("done")
    # print(mappa_lens)
mappa_lens.sort(reverse=True)
ans2=1
print(mappa_lens)
for i in range(3):
  ans2*=mappa_lens[i]
print(ans2)
