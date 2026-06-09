lst1 = [1,2,3,4]
lst2 = [3,4,5,6]

result =[]
for i in lst1:
    
    if i in lst2:
        result.append(i)
print(result)