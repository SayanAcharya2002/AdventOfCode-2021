#!/usr/bin/python3
import heapq as hp
import sys

#the basic idea is to use Dijkstra to get the shortest path to the last point
#for the second part just expand the graph before solving

file_name=sys.argv[1]
file=open(file_name,"r")
grid=[list(map(int,i.strip('\n'))) for i in file.readlines()]
n=len(grid)
EXPAND=1

def expand_grid(grid,EXPAND:int):
  n=len(grid)
  new_grid=[]
  for i in range(n*EXPAND):
    new_grid.append([0]*(n*EXPAND))
  for _i in range(n):
    for _j in range(n):
      new_grid[_i][_j]=grid[_i][_j]
      for i in range(EXPAND):
        for j in range(EXPAND):
          new_grid[n*i+_i][n*j+_j]=new_grid[_i][_j]+i+j
          if new_grid[n*i+_i][n*j+_j]>9:
            new_grid[n*i+_i][n*j+_j]-=9
  return new_grid

def make_string(d:int,x:int,y:int):
  LENGTH=10
  return f"{str(d).zfill(LENGTH)},{x},{y}"
def parse_string(string):
  return map(int,string.split(','))
def within_map(x,y,EXPAND):
  return x>=0 and y>=0 and x<(n*EXPAND) and y<(n*EXPAND)

hippy=[make_string(0,0,0)]
direc=[(0,1),(0,-1),(1,0),(-1,0)]

distance=[]
visited=[]
infy=int(1e9)

for i in range(n*EXPAND):
  distance.append([infy]*n*EXPAND)
  visited.append([False]*n*EXPAND)
distance[0][0]=0

#set this EXPAND to 5 in order to solve the second part
grid=expand_grid(grid,EXPAND)

while len(hippy)!=0:
  d,x,y=parse_string(hp.heappop(hippy))
  # print(d,x,y)
  if visited[x][y]:
    continue
  visited[x][y]=True
  for i,j in direc:
    if within_map(x+i,y+j,EXPAND):
      if distance[x+i][y+j]>distance[x][y]+grid[x+i][y+j]:
        distance[x+i][y+j]=distance[x][y]+grid[x+i][y+j]
        hp.heappush(hippy,make_string(distance[x+i][y+j],x+i,y+j))
print(distance[-1][-1])
