# marks =[1,2,3,"Arun",True]
# print(marks)
# print(type(marks))
# print(marks[1])
# print(marks[4])
# print(len(marks))
# print(marks[(len(marks))-2])
# print(marks[1:4])
# print(marks[1:4:2])



# if "2" in marks:

    
#     print("yes")
# else:
#     print("no")





# LIST COMPRESHION

list = [ i for i in range(11)]
print(list)



list = [i for i in range(10) if i%2==0 ]
print(list)




#remove excercise
list = ["arun","anish","ankush","amit","rohan"]
for l in list:
    if "a" in l:
        list.remove(l)
print(list)

