#!/usr/bin/env python
from __future__ import print_function

name1 = "Student 8"
name2 = "Student 9"
name3 = "Student 10"

try:
    # PY2
    name4 = raw_input("Enter fourth name: ")
except NameError:
    # PY3
    name4 = input("Enter fourth name: ")

print()
print("{:>30}".format(name1))
print("{:>30}".format(name2))
print("{:>30}".format(name3))
print("{:>30}".format(name4))
print()
