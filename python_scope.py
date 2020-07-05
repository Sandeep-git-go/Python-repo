#!/bin/python3

mystr = 'outside hello world'

def main_function():
  mystr = 'Hello world'
  print('mystr = %s' % mystr)
  return

main_function()
print('global: mystr = %s' % mystr)

mystr = 'Global mystr'

def global_function():
    mystr = 'sub gloabl mystr'
    def local_function():
        nonlocal mystr
        mystr = 'local mystr'
        return
    local_function()
    print('sub mystr = %s' % mystr)
global_function()
print('global mystr = %s' % mystr)
