
'''
name = input("Enter your name: ")  
print("Hello, " + name + "!")'
age = 19
print(f"My name is {name} and I am {age} years old.")

'''
import pdb

def divide(a, b):
    pdb.set_trace()  # Debugging starts here
    return a / b

divide(10, 0)  # This will trigger an error

