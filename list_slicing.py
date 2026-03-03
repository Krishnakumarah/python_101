lst=input().split(",")
n=len(lst)
if n==1:
    print(lst)
elif n%2==0:
    print([lst[n//2]],[lst[n//2+1]])
else :
    print([lst[n//2-1]],[lst[n//2]],[lst[n//2+1]])
    
    