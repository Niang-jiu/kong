# day2
# print("Day 2: 30 Days of python programming")
# first_name = "Jiu"
# last_name = "Niang"
# full_name = "Jiu Niang"
# country = "love"
# city = "like"
# age = 520
# year = 1314
# is_married = False
# first_name, last_name, full_name, country, city, age, year, is_married = "Jiu", "Niang", "Jiu Niang", "love", "like", 520, 1314, False
# print(type(first_name))
# print(len(first_name))
# print(len(last_name))
# num_1 = 5
# num_2 = 4
# variable_total = num_1+num_2
# print(variable_total)
# diff = num_1 - num_2
# print(diff)
# product = num_1*num_2
# print(product)
# division = num_2/num_1
# print(division)
# remainder = num_2 % num_1
# print(remainder)
# exp = num_1**num_2
# print(exp)
# floor_division = num_2//num_1
# print(floor_division)
# r = 30
# area_of_circle = r**2*3.14
# print(area_of_circle)
# circumference = 2*r*3.14
# print(circumference)
# rad = float(input("enter the radius"))
# area_of_circle2 = rad**2*3.14
# print(area_of_circle2)

# day 3
# age = int(19)
# height = float(170)
# a=1+1j
# base = float(input("base"))
# height2 = float(input("height"))
# print("area=",0.5*base*height2)
# side_a = float(input("side_a"))
# side_b = float(input("side_b"))
# side_c = float(input("side_c"))
# print("perimeter=",side_a+side_b+side_c)
# length = float(input("length="))
# width = float(input("width"))
# print("area=",length*width," perimeter=",2*(length+width))
# radius = float(input("radius"))
# print("area=",radius**2*3.14," circumference=",2*3.14*radius)
# print("slope of y=2x+2 is",2/1)
# print("slope2 = ",(10-2)/(6-2), "Euclidean distance = ",(10-2)**2+(6-2)**2)
# x = input("x")
# y=x**2+6*x+9
# print(len("python")!=len("dragon"))
# print("on" in "dragon" and "on" in "python")
# print("jargon" in "I hope this course is not full of jargon.")
# print("on" not in "dragon" and "on" not in "python")
# length = float(len("python"))
# string = str(length)
# print(type(length)," ",length,type(string), " ", string)
# a = int(input("print an natural number"))
# print("even" if a%2==0 else "odd")
# print(7//2==int(2.7))
# print(5//2==int(2.7))
# print(type("10")==type(10))
# print(int(float("9.8"))==10)
# hours = float(input("hours"))
# rph = float(input("rate per hour"))
# print("your weekly earning is %f",hours*rph)
# years = float(input("enter number of years you have lived"))
# print("you have lived for %.2f seconds",years*365*24*60*60)
# i = 1
# while(i<=5):
#     print(i,"1",i,i*i,i*i*i)
#     i+=1
# for k in range(1,6):
#     print(k,1,k,k*k,k*k*k)
# j = 1
# while(j<=5):
#     print(j,1,j,j*j,j*j*j, sep="")
#     j+=1
# for l in range(1,6):
#     print(f"{l}1{l}{l*l}{l*l*l}")

# day 4

# a,b,c,d = "Thirty", "Days", "Of", "Python"
# e=a+" "+b+" "+c+" "+d
# print(e)
# g = ["Thirty","Days","Of","Python"]
# h = " ".join(g)
# print(h)
# i,j,k,l = "Thirty","Days","Of","Python"
# m = f"{i} {j} {k} {l}"
# print(m)
# a,b,c = "Coding","For","All"
# d = a+" "+b+" "+c
# e = ["Coding","For","All"]
# g = " ".join(e)
# h = f"{a} {b} {c}"
# print(d,g,h,sep="\n")
company = "Coding Of All"
# print(company)
# print(len(company))
# print(company.upper())
# print(company.lower())
# print(company.capitalize())
# print(company.title())
# print(company.swapcase())
# print(company.split())
# print(company.split()[0])
# print(company.replace("Coding","Python"))
# a = "Coding"
# print(company.find("Coding"))
# print(company.index(a))
# py = "python for everyone"
# print(py.replace("everyone","all"))
# print(company.split())
# many = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
# print(many.split(", "))
# code = "coding of all"
# print(code[0])
# print(code[-1])
# print(code[len(code)-1])
# print(code[10])
# name = "Python For Everyone"
# acronym = " ".join(word[0].upper() for word in name.split())
# print(acronym)
# name2 = "coding for all"
# acronym2 = ",".join(word[0].upper() for word in name2.split())
# print(acronym2)
code = "Coding For All"
print(code.index("C") == 0)
print(code.index("F") == 0)
print(code.startswith("C"))
print(code.rfind("i"))
sen = "You cannot end a sentence with because because because is a conjunction"
print(sen.find("because"))
print(sen.rindex("because"))
start = sen.find("because because because")
stop = start + len("because because because")
phrase = sen[start:stop]
print(phrase)
print(code.startswith("Coding"))
print(code.endswith("coding"))