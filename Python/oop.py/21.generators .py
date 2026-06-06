def generator():
    for i in range(5):
        yield i
   

gen = generator()
for j in gen:
    print(j)