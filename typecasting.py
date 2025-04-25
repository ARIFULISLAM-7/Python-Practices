# typecasting = The process of converting a value of one data type to another (int to float, float to int, etc.)
# typecasting is also called type conversion
# Explicit VS Implicit typecasting
# Explicit typecasting = manually converting a value from one data type to another (int to float, float to int, etc.)

name = "Ariful"
age = 22
gpa = 3.14
student = True

print(type(name))
print(type(age))  
print(type(gpa))  
print(type(student)) 

print(float(age))
print(type(float(age)))  
# Explicit typecasting (int to float)
print(int(gpa))  
# Explicit typecasting (float to int)
print(type(int(gpa)))  

print(str(student)) 
# Explicit typecasting (bool to str)
print(type(str(student)))

age = bool(age)
print(age)
print(type(age))
# Explicit typecasting (int to bool)
# 0 = False, 1 = True

is_student = 0
is_student = bool(is_student)
print(is_student)

# Implicit typecasting = automatically converting a value from one data type to another (int to float, float to int, etc.)
a = 5
b = 8
c= a/b
print(c)