print('hello world')
print("hello world")
print("hello \nworld")
print("hello \tworld")
print('length=',len('hello'))     # len returns the length of the string
mystring="python"       # assigning value python to variable mystring
print(mystring)         # it returns python
# Indexing
print('the element at Index[0]=',mystring[0])      # it returns 'p' because P is at 0
print('the element at Index[3]=',mystring[3])      # it returns 'h'
# Slicing
print('the elements starting at Index[0] and it goes upto Index[4]',mystring[0:4])  
                        # it returns 'pyth'In slicing it goes upto but not include
print('start at Index[3] and goes upto Index[5]',mystring[3:5])    # it returns 'ho'
print(mystring[::2])    # it returns 'pto'