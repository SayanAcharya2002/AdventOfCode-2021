#part 1
import io
import collections as clc

file=io.FileIO("input.txt","r")
l=[]
x=[2,4,3,7]
s=clc.Counter()
for i in file:
  i=str(i,"utf-8")
  l.append(list(map(lambda x:len(x.strip()),i.split('|')[1].split(' '))))
# print(l)
for i in l:
  s.update(i)
count=sum(map(lambda x:s[x],x))
print(count)

#part 2
import io
import itertools as it

file = io.FileIO("input.txt", "r")
org = ['a', 'b', 'c', 'd', 'e', 'f','g']
mapping = {
    'abcefg': 0,
    'cf': 1,
    'acdeg': 2,
    'acdfg': 3,
    'bcdf': 4,
    'abdfg': 5,
    'abdefg': 6,
    'acf': 7,
    'abcdefg': 8,
    'abcdfg': 9,
}
train_data = []
test_data = []
tot=0
for i in file:
    i = str(i, "utf-8").strip()
    # print(len(i[0][-1]))
    arr = i.split('|')
    train_data.append(arr[0].strip().split(' '))
    test_data.append(arr[1].strip().split(' '))
    tot+=1
ans=0
# print(tot)
# print(train_data)
# print(test_data)
for index in range(0,tot):
  for i in it.permutations(org):
      mappa = dict(zip(org, i))  # fake->real
      new_train = [mapping.get(''.join(sorted(''.join(map(lambda x:mappa[x],j)))))  for j in train_data[index]]
      new_test = [mapping.get(''.join(sorted(''.join(map(lambda x:mappa[x],j)))))  for j in test_data[index]]
      
      if None not in new_train and None not in new_test:
        val=int(''.join(map(str,new_test)))
        # print(new_test)
        ans+=val
        break
      
print(ans)
