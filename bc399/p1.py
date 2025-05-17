def dist(n,s,t):
  s1 = list(s) 
  t1 = list(t)
  d = 0
  for c1, c2 in zip(s1,t1):
    if c1 != c2:
      d += 1
  return d

n = int(input())
s = input()
t = input()
print(dist(n,s,t))
