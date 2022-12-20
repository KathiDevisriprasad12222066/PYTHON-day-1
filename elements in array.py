from functools import reduce
arr1=[5,7,8,12,2,9,15,19]

y=reduce(lambda x,y:x+y,arr1)
print(y)