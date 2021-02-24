# main program which imports the other one called 'my_module.py'

import sys
from my_module import divide
import libs.mylib


print(sys.path) # displays directories where Python is going to look for when importing modules. add new one in cmd line with $export PYTHONPATH = <python path>
print(divide(9,3))
print(__name__)
print(sys.modules) # see what is imported
