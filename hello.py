# importing functions:
# from filename_without_dot_py import function_name


a = 28  # int
b = 1.5 # float
c = "Hello"    # str
d = 'Hello, Multiverse!'    # str
e = True    # bool
f = None    # NoneType, absence of something    

def get_square(x):
    return x * x

print(d)
name = input("Name? ")
print(c + ", " + name + "!")   
print(f"{c}, {name}!")

# name[0] is the 1. character of the string name

print(f"The 1. character of the name is: {name[0]}")

# looping:

print("characters in the name you gave:")
for character in name:
    print(character)

print()

n = int(input("Enter some number: "))
if n == 0:
    print(str(n) + " is zero")
elif n > 0:
    print(str(n) + " is positive")
else:
    print(str(n) + " is negative")

print("more names:")

# list:
names = ["Bruce", "Roy"]

names.append("Rob")

print(names)

names.sort()

print("more names, sorted and one by one:")

for aname in names:
    print(aname)

# looping 1:
print("again by looping the list index:")

for i in [0,1,2]:
    print(f"names[{i}] : {names[i]}")

# tuple: the values will not change but the combination is relevant:
coordinates_xyz = (1.0, 3.0, 7.0)

# list: sequence of mutable values
# tuple: sequence of immutable values
# set: collection of unique values, not ordered
# dict: collection of key-value pairs : lookup

print("tuple coordinates_xyz: ")
print(coordinates_xyz)

# create an empty set s:
s = set()

# add elements to the set s
s.add(1)
s.add(2)
s.add(3)

s.add(3) # no change, 3 already in the set s

print("set s:")
print(s)
# > {1, 2, 3}

s.remove(2)

print(s)
# > {1, 3}

# len gives the number of elements in a data structure:

print(f"The set s has {len(s)} elements")

# looping 2:

for i in range(0,8):
    print(f"{i} squared: {get_square(i)}")

# dict:

q_to_b = { "excellent": "Weatherby", "2. best" : "Tikka", "3. best" : "Sako", "4. best": "Remington" }

for key in q_to_b.keys():
    print(f"{key} => {q_to_b[key]}")

q_to_b["4. best"] = "Ruger"     # overwrite value of a key

for key in q_to_b.keys():
    print(f"{key} => {q_to_b[key]}")

