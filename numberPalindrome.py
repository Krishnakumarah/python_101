x=1221

def reversed(x):
 revers=0
 while x!=0:
  last=x%10
  revers=revers*10+last
  x=x/10
print(revers)
  
reversed(x)
