print("Array Traversal in Python Using an NumPy Library")
from numpy import *
try:
    myarray=array(input("Enter elements separated by spaces: ").split(),int)
except:
    print("Invalid input. Please enter integers separated by spaces.")
    
print("Array elements are:",myarray)