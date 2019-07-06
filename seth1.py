from collections import Counter
h = input()
v = [i for in input().split()]
t = Counter(v)
r =[]
for i, j in t.items():
  if j > 1:
    r.append(i)
if r:
  r.sort()
  print(' '.join(r))
else:
  print('unique')
  
             
    
   
