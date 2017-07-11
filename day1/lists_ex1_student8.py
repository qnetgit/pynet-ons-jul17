#!/usr/bin/env python
from __future__ import print_function

my_list = ['hullo', 'whatsup', 'someone', 'howelse', 'later']
my_list.append('whatev')
my_list.append('abc')
print(my_list.pop(0))

print("Length of list: {}".format(len(my_list)))
my_list.sort()
print(my_list)
