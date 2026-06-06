# for k in range(5):
#     print(k+1)
#     if(k==3):
#         print("this is special")


# for k in range(1,10):
#     print(k)
#     if(k==3):
#         print("this is special")

# # 3 parameter of range() function
# for k in range (1,12,3):
#     print(k)



# #while loop

# i = 0
# while(i<5):
#     print(i)
#     i=i+1
# print("it's done")


# i = 0
# while(i<=5):
#     print(i)
#     i=i+1
# print("it's done")





#decrement while loop
# count = 5
# while(count>0):
#     print(count)
#     count=count-1


#else with while loop

# count = -5
# while(count>0):
#     print(count)
#     count=count-1
# else:
#     print("i am in else")

# for i in range(1,10001):
#     print('❤️')
#     print(i)



#OTP GENERATOR

import random

otp = random.randint(10,1000000)

print("your OTP is :",otp)

entered_otp = int(input("enter the number"))
while(entered_otp!=otp):
    print(" otp wrong try again")
    otp = random.randint(10,1000000)

    print("your otp is :",otp)

    entered_otp = int(input("enter the number"))


if(entered_otp==otp):
    print("otp succsess")