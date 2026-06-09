# time=int(input("enter your time:"))
# if(time>4 and time<12):
#     print("Good morning")
# elif(time>=12 and time<16):
#     print("Good afternoon")
# elif(time>=16 and time<20):
#     print("Good evening")
# else:
#     print("Good night")


import time

t = time.strftime('%H:%M:%S')
HOUR = int(time.strftime('%H')) 

print(HOUR)


if(HOUR>0 and HOUR<12):
    print("Good morning")
elif(HOUR>=12 and HOUR<16):
    print("Good afternoon")
if(HOUR>=16 and HOUR<20):
    print("Good evening")
else:
    print("good night")
