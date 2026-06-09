list = [1,2,4,65,3,57,4,7,43,1,23,4,5,6,7,8,9]
even =[]
odd=[]

for num in list:
    if num % 2 ==0:
        even.append(num)
    else:
        odd.append(num)
print(even,odd)