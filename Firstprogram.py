name = "Faisal-zia"
age = 30
print("my name is:", name)
print("my age is:", age)

print(type(name))
print(type(age))

a= 2
b= 5
sum= a+b
print(sum)

a= 1000
b= 400
diff= a-b
print(diff)

# Arithmatic operators
a= 5
b= 2

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b) # remendir
print(a**b) # power

# Relational / comparison operators

a= 50
b= 20

print(a == b) # false
print(a != b) # true
print(a >= b) # true
print(a > b) # true
print(a <= b) # false
print(a < b) # false

#Assignment operators

num = 10
num += 5 #num = num + 5

print("num :", num)

num = 10
num *= 5    # same like -=, /=, %=, **=

print ("num:", num)

#Logical operators  # not, and, or

# not operator
print(not True)
print(not False)

# Always give boolen value that is not used to negate not true means its false

a = 50
b = 30

print(not True)
print(not a>b)

# And operator
val1 = True
val2 = False
print("AND operator:", val1 and val2) # true only when both val1 and val2 are true

# Or operator

print("or operator:", val1 or val2) # true even only one val is true
 
 # type conversion
a = 2 
b = 4.25

sum = a + b
print(sum) # imlicit conversion

a = int("2")
b = 4.25

sum = a + b
print(type(a))
print(sum) # type casting
