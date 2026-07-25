# String text ko store karti hai
name = "Sushant"

print(name)
print(type(name))


# Dono valid hain

name1 = "Sushant"
name2 = 'Sushant'

print(name1)
print(name2)





# Triple quotes se multiple lines likh sakte hain

message ="""" 
hello 
sushant 
babu
"""

print(message)




#String Indexing
name = "Python"

# Index 0 se start hota hai
print(name[0])   # P
print(name[1])   # y
print(name[2])   # t
print(name[3])   # h
print(name[4])   # o
print(name[5])   # n



#6. Negative Indexing
name = "Python"

# Last character se count hota hai

print(name[-1])   # n
print(name[-2])   # o
print(name[-3])   # h




#7. String Slicing
name = "Python"

# Start : End
# End include nahi hota

print(name[0:3])   # Pyt
print(name[2:5])   # tho
print(name[:4])    # Pyth
print(name[3:])    # hon






# #8. Length of String
# name1 = "Sushant"

# # len() total characters batata hai
#  print(len(name1)



      


#9. String Concatenation
first = "Sushant"
last = "Yadav"

# Do strings ko jodna

full = first + " " + last

print(full)







#10. String Repetition
# String ko repeat karna

print("Python " * 3)

# Output

# Python Python Python




#11. Upper Case
name = "python"

print(name.upper())

# Output
# PYTHON







#12. Lower Case
name = "PYTHON"

print(name.lower())

# Output
# python


# 13. Capitalize
name = "python"

print(name.capitalize())
# Output
# Python



#14. Title
name = "learn python programming"

print(name.title())
# Output
# Learn Python Programming



#15. Replace
sentence = "I love Java"
# Java ko Python se replace karna
print(sentence.replace("Java", "Python"))

# Output
# I love Python




#16. Find
text = "Hello Python"

# Python kis index se start hua

print(text.find("Python"))
# Output
# 6




# 17. Count
# text = "banana"

# # a kitni baar hai

# print(text.count("a"))

# Output

# 3
# 18. Startswith
# text = "Python"

# print(text.startswith("Py"))

# Output

# True
# 19. Endswith
# text = "Python"

# print(text.endswith("on"))

# Output

# True
# 20. Strip
# text = "   Python   "

# # Extra spaces remove karega

# print(text.strip())
# 21. Split
# text = "Python Java C++"

# # Space ke basis par list ban jayegi

# print(text.split())

# Output

# ['Python', 'Java', 'C++']
# 22. Join
# languages = ["Python", "Java", "C++"]

# # List ko string banana

# print(" | ".join(languages))

# Output

# Python | Java | C++
# 23. f-String ⭐ (Bahut Important)
# name = "Sushant"
# age = 21

# # Variables ko string ke andar use karna

# print(f"My name is {name} and I am {age} years old.")

# Output

# My name is Sushant and I am 21 years old.
# 24. Escape Characters
# print("Hello\nPython")   # New line

# print("Hello\tPython")   # Tab

# print("He said \"Hello\"")   # Double quote print karna
# 25. String is Immutable ⭐⭐⭐
# name = "Python"

# # Ye error dega
# # name[0] = "J"

# # Naya string banana padega
# name = "J" + name[1:]

# print(name)

# Output

# Jython
# Practice Questions
# Q1.
# name = "Programming"

# # P print karo
# # g print karo
# # Last character print karo
# Q2.
# text = "I Love Python"

# # Upper
# # Lower
# # Replace Python with Java
# Q3.
# first = "Sushant"
# last = "Yadav"

# f-string se Full Name print karo
# 📌 Aaj ke liye yaad rakhne wale methods
# ⭐ Interview ke liye yaad rakho
# len() → Length
# type() → Data Type
# upper() → Uppercase
# lower() → Lowercase
# capitalize() → First letter capital
# title() → Every word capital
# replace() → Replace text
# find() → Index of substring
# count() → Count occurrences
# startswith() → Starts with?
# endswith() → Ends with?
# strip() → Remove extra spaces
# split() → String → List
# join() → List → String
# Indexing → Single character access
# Slicing → Part of string
# f-string → String formatting
# String is Immutable → Original string cannot be modified

