print("Hello World")

a = 8
b = str(a) # a but type should be string

t = type(b)
print(t)

#------------------------ Input -------------------------------------
# Use int function because it takes numbers in form of string and concatinate it.

c = int(input("Enter number 1: "))
d = int(input("Enter number 2: "))

print(c + d)

#---------------------- Strings --------------------------------------

name = "Hoorain"
slice = name[0 : 4]  # Last index is not included
print(slice)


#---------------------- Slicing with skip value ----------------------

word = "amazing"
print(word[1 : 6 : 2])   # returns "mzn"