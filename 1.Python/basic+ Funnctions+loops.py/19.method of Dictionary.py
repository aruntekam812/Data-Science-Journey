#update()

d1 = { 1:10,2:20,3:30}
d2 = {4:40,5:50}
d1.update(d2)
print(d1)



#clear()

d1 = { 1:10,2:20,3:30}
d1.clear()
print(d1)


#pop()


d1 = { 1:10,2:20,3:30}
print(d1.pop(2))


#popitem()


d1 = { 1:10,2:20,3:30}
# print(d1.popitem())
d1.popitem()
print(d1)