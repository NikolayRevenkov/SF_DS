from collections import deque
from typing import Deque
k=0
n=1
def skoba(stroka):
    sk=deque()
    k=len(stroka)
    t=False
    m=0
    l=0
    for n in stroka:
        if n==')':
            sk.pop()
            m=+1
        if n=='(':
            sk.append(n)
            l=+1 
        n=+1        
    if m==l:
        t=True
    return(t)
r=input("Vvedi skobki")
print(skoba(r))
