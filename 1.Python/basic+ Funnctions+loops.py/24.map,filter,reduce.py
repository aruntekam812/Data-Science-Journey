#map 

# def cube(x):
#     return x * x * x

# l =[1,2,3,4,5,6,7,2,]

# newl=list(map(cube,l))

# print(newl)

#filter

# def filter_function(a):
#     return a>3
# newnewl = list(filter(filter_function,l))
# print(newnewl)


#reduce

from functools import reduce

numbers =[1,2,3,4,5]
sum = reduce(lambda x,y:x+y,numbers )
print(sum)