# tup = (1,2,3,4,5)
# res =tup.count(5)
# print(res)
# print(tup[1:3])
# print(tup[0:4:2])
# print(tup)

#modification in tupple through list 

a = (1,2,3,4,5,)
temp =list(a)
temp.append(100)
temp.pop(2)
temp[0]=500
a = tuple(temp)
print(a)
