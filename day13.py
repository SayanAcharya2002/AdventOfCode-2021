#!/usr/bin/python3
import collections as clc
import sys
# import matplotlib.pyplot as plt

file_name=sys.argv[1]
file=open(file_name,"r")
coun=clc.Counter()
all_lines=file.readlines()
index=0
for i in all_lines:
  i=i.strip("\n")
  index+=1
  if len(i)==0:
    break
  x,y=map(int,i.split(','))
  coun.update([(x,y)])

fold_inst=[]
for _i in range(index,len(all_lines)):
  _i=all_lines[_i].strip('\n')
  demark=_i.find('=')
  fold_inst.append((_i[demark-1],int(_i[demark+1:])))

#reading done

for i in fold_inst:
  num=i[1]
  check=-1
  if i[0].upper()=='X':
    check=0
  else:
    check=1

  for j in list(coun.keys()):
    if j[check]>num:
      val=[(1-check,j[1-check]),(check,2*num-j[check])]
      val=sorted(val,key=lambda x:x[0])
      coun.update({(val[0][1],val[1][1]): coun.get(j)})
      del coun[j]
  # print(coun)
  # print(len(coun.keys())) #uncomment this line and the next one to get the 1st ans
  # break
# print(coun)
x_arr=[]
y_arr=[]

pic_len_x=0
pic_len_y=0
for i in coun.keys():
  pic_len_x=max(pic_len_x,i[0])
  pic_len_y=max(pic_len_y,i[1])
l=[]
pic_len_y+=1
pic_len_x+=1
for i in range(pic_len_y):
  l.append([' ']*pic_len_x)

for _i in coun.keys():
  x_arr.append(_i[0])
  y_arr.append(_i[1])
  l[_i[1]][_i[0]]='#'

# plt.scatter(x_arr,y_arr,)
# plt.show()

l=[''.join(i) for i in l]
print(*l,sep="\n")


#code => EPLGRULR
