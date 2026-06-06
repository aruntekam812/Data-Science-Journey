#string methods

#1. upper()

a = " arun"
print(a.upper())

#2.lower

b = "ARUN"
print(b.lower())

# rstrip()

c ="!!Arun%%**!!"
print(c.rstrip("!,%"))

#4.replace()

d = "arun,arun"
print(d.replace("arun","top"))


#split()

e = "arun !!!! tekam"
print(e.split(" "))

# capitalize

f = "introductiON Of DS"
print(f.capitalize())

#center()

g= "welcome to hudd"
print(len(g))
print(g.center(50))

#count()
h = "arun, 555, 333, arun"
print(h.count("arun"))

#endswith()

i = "welcome to hudd"
print(i.endswith("d"))

#STARTWITH()

i = "welcome to hudd "
print(i.startswith("w"))


# find()
j = "i am arun. i am from balaghat "
print(j.find("arun"))

#idex()

#isalnum()

k = "aruntekam11"
print(k.isalnum())

#isalpha
k = "aruntekam"
print(k.isalpha())

#islower
k = "aruntekam"
print(k.islower())

#isupper
k = "WTST"
print(k.isupper())


#isprintable
k = "arun tekam\n"
print(k.isprintable())

#isspace
k = "     "
print(k.isspace()) 

#istitle
k = "Trun  Tekam"
print(k.istitle())

#swapcase
k = "Trun  Tekam"
print(k.swapcase())


#title
k = "trun  tEkam"
print(k.title())
