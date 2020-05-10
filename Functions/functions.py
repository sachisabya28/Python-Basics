# A simple Python function to check 
# whether x is even or odd 
def evenOdd( x ): 
    if (x % 2 == 0): 
        print "even"
    else: 
        print "odd"
  
# Driver code 
evenOdd(2) 
evenOdd(3) 

##############################
# Here x is a new reference to same list lst 
def myFun(x): 
   x[0] = 20
  
# Driver Code (Note that lst is modified 
# after function call. 
lst = [10, 11, 12, 13, 14, 15]  
myFun(lst); 
print(lst)  


############################
def myFun(x): 
  
   # After below line link of x with previous 
   # object gets broken. A new object is assigned 
   # to x. 
   x = [20, 30, 40] 
  
# Driver Code (Note that lst is not modified 
# after function call. 
lst = [10, 11, 12, 13, 14, 15]  
myFun(lst); 
print(lst)  

###############################
def python_food():
    width = 80
    text = "Spam and eggs"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)

################################
def centre_text(*args, sep=' '):
    text = ""
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text)) // 2
    return " " * left_margin + text

##############################



def swap(x, y): 
    temp = x; 
    x = y; 
    y = temp; 
  
# Driver code 
x = 2
y = 3
swap(x, y) 
print(x) 
print(y) 

##############################
# with open("centred", mode='w') as centred_file:

# call the function
# s1 = centre_text("spam and eggs")
# print(s1)
# s2 = centre_text("spam, spam and eggs")
# print(s2)
# s3 = centre_text(12)
# print(s3)
# s4 = centre_text("spam, spam, spam and spam")
# print(s4)
# s5 = centre_text("first", "second", 3, 4, "spam", sep=":")
# print(s5)

with open("menu", "w") as menu:
    s1 = centre_text("spam and eggs")
    print(s1, file=menu)
    s2 = centre_text("spam, spam and eggs")
    print(s2, file=menu)
    print(centre_text(12), file=menu)
    print(centre_text("spam, spam, spam and spam"), file=menu)
    s5 = centre_text("first", "second", 3, 4, "spam", sep=":")
    print(s5, file=menu)
