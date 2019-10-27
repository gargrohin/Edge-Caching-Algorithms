import os
import random

size_kb=[]
for x in range(60):
    size_kb.append(random.randint(1024,5*1024))
print(sum(size_kb)/1024)
for x in range(100):
    size_kb.append(random.randint(50,150))
print(sum(size_kb)/1024)
for x in range(570):
    size_kb.append(random.randint(150,1024))
print(sum(size_kb)/1024)

random.shuffle(size_kb)
name=0
for size in size_kb:
    name=name+1
    with open(str(name),'wb') as fout:
        fout.write(os.urandom(size*1024))
