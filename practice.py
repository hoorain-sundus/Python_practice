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

#---------------------- String Methods -----------------------------------

print(word.count("a"))
print(word.replace("a","r"))
print(word.endswith("ing"))
print(word.startswith("ama"))
print(word.upper())
print(word.lower())
print(word.capitalize())


#------------------------------- List in python ---------------------------------------
l1 = [5, 8, 1, 20, 4, 6, 8]

l1.sort()
print(l1)

l1.reverse()
print(l1)

l1.insert(3, 40)
print(l1)

l1.pop(4)
print(l1)

l1.append(100)
print(l1)

print(l1.count(8))

l1.remove(1)
print(l1)

# -------------------- Tuples ---------------------------------------------

t = (1, 23, 89, 100, 45, "Anaya", False)

print(type(t))

print(t.index(100))
print(t.count(89))

tuple1 = (1, 2,  3)
tuple2 = (4, 5, 6)

print(min(tuple1))   #output [1]
print(max(tuple1))   #output [3]


#---------------------------- Concatenation -------------------------------

concatenated = tuple1 + tuple2
print(concatenated)

repeated = tuple1 * 4
print(repeated)

a, b, c = tuple1
print(a, b, c)       #Tuples can be unpacked into individual variable.


print(3 in tuple1)   # check if an item exist in tuple


#-------------------------------- Dictionary ----------------------------------------

marks = {
    "Ayesha" : 55,
    "Amna" : 70,
    "Fatima" : 68
}

print(marks)
print(type(marks))
print(marks["Ayesha"])

print(marks.items())
print(marks.keys())
print(marks.values())

marks.update({"Ayesha" : 23,"Aiman" : 75})
print(marks)