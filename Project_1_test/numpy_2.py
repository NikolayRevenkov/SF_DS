import numpy as np
a = np.int8(25)
#print(a)
# 25
#print(type(a))
#print(np.iinfo(np.int64))
#print(*sorted(map(str, set(np.sctypeDict.values()))), sep='\n')
a=-456
b=np.uint8(a)
#print(b)
arr=np.linspace(-6,21,60, endpoint=False)
arr2=np.arange(0,9)
arr3=arr2.reshape((3,3))
print(arr3)