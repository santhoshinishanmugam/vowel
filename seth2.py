d = int(input())
j = sorted(input().split(), reverse=True)
temp=' '
for i in j:
  temp += i
print(int(temp))  
