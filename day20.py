#!/usr/bin/python3
import sys
import itertools as it
import functools as ft
import re
import math
import datetime as dt
import time

file_name=sys.argv[1]
file=open(file_name,"r")
all_lines=[i.strip('\n') for i in file.readlines()]

n=len(all_lines)-2
m=len(all_lines[2])

outside='0'
# s=set(len(i) for i in all_lines[2:])
# print(s)


direc=[(x,y) for x,y in it.product([-1,0,1],repeat=2)]
# print(direc)

mapper=lambda x:'1' if x=='#' else '0'
algo_string=''.join(map(mapper,all_lines[0]))
grid=[''.join(map(mapper,i)) for i in all_lines[2:]]

def borderize(grid:list,border):
  global n,m
  for i in range(n):
    grid[i]=border+grid[i]+border
  grid.insert(0,border*(m+2))
  grid.append(border*(m+2))
  n+=2
  m+=2

def get_val(x,y):
  within=lambda x,y: x>=0 and y>=0 and x<n and y<m  
  string=""
  for i,j in direc:
    if within(x+i,y+j):
      string+=grid[x+i][y+j]
    else:
      string+=outside
  return int(string,2)

def make_new_grid():
  new_grid=[]
  for i in range(n):
    string=""
    for j in range(m):
      string+=algo_string[get_val(i,j)]
    new_grid.append(string)
  return new_grid

borderize(grid,outside)

#for part1, how_many_times=2 and for part2, how_many_times=50
how_many_times=50

for _ in range(how_many_times):
  grid=make_new_grid()
  outside=algo_string[int(outside*9,2)]
  # print(outside)
  borderize(grid,outside)
  # print(*grid,sep='\n')
  # print("--------------")
  

print(sum(i.count('1') for i in grid))
