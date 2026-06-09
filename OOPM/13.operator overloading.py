# class vector:
#     def __init__(self,i,j,k):
#         self.i=i
#         self.j=j
#         self.k=k
#     def show(self):
#         print(f"{self.i}i + {self.j}j + {self.k}k")

#     def __add__(self,x):
#         print(f"{self.i +x.i}i + {self.j+x.j}j + {self.k+x.k}k")



# v1= vector(1,2,3)
# v1.show()

# v2= vector(2,3,4)
# v2.show()

# print(v1+v2)


class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def show(self):
       
        print(f"{self.x} + {self.y}")

    def __add__(self,other):

        print(f"{self.x+other.x} + {self.y+other.y}")


p1 = point(10,10)
p1.show()
p2= point(20,20)
p2.show()

print(p1 + p2)