list =[4,6,37,9,2,0,1,4,9]
seen = set()
result=[]
for num in list:
    if num not in seen:
        
        result.append(num)
        seen.add(num)
print(result)
