#!/bin/python3

mystr = 'outside hello world'

def main_function():
  mystr = 'Hello world'
  print('mystr = %s' % mystr)
  return

main_function()
print('global: mystr = %s' % mystr)


