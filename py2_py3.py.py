# Division operator
# print function
# Unicode
# xrange
# Error Handling
# _future_ module

# the operator / returns a float value if one of the arguments is a float(py2)
print 5/2
print -5/2
print 5.0/2
print -5.0/2


# Python 2.7
2
-3
2.5
-2.5
# Python 3

print (5/2)
print (-5/2)
print (5.0/2)
print (-5.0/2)

2.5
-2.5
2.5
-2.5

#  In Python 3, ‘/’ operator does floating point division for both int and float arguments.

print (5//2)
print (-5//2)
print (5.0//2)
print (-5.0//2)
#output

2
-3
2.0
-3.0
# Behavior of “//” is same Python 2 and Python 3
###############################

print 'Hello, I"m in python2'      # Python 3.x doesn't support 
  
print('Hello, I"m in python3') 
# print is func in python 3 but an expression in python2

##############################
  
for x in xrange(1, 5):  
  
    print(x) 
  
    
  
for x in range(1, 5):  
  
    print(x)
  
    
  
'''  
  
Output in Python 2.x  
  
1 2 3 4 1 2 3 4  
  
    
  
Output in Python 3.x  
  
NameError: name 'xrange' is not defined  
  
''' 

###################

# There is a small change in error handling in both versions. In python 3.x, ‘as’ keyword is required.

try:  
  
    trying_to_check_error  
  
except NameError, err:  
  
    print err, 'Error Caused'   # Would not work in Python 3.x  

try:  
  
     trying_to_check_error  
  
except NameError as err: # 'as' is needed in Python 3.x  
  
     print (err, 'Error Caused')  
  