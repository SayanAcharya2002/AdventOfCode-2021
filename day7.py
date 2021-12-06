import collections as clc
mappa=clc.Counter(map(int,input().split(',')))
index=0
length=256 #put 80 here for the first part
old_len=6
new_len=old_len+2

for i in range(length+1):
  if mappa.get(i-1) is not None:
    mappa.update({i+old_len:mappa.get(i-1),i+new_len:mappa.get(i-1)})
    del mappa[i-1]
print(sum(mappa.values()))
