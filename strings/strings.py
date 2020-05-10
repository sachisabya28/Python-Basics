print("Today is a good day to learn Python")
print('Python is fun')
print("Python's string are easy to use")
print('We can even include "quotes" in strings')
print("hello" + " world")
greeting = "Hello"
name = "Tim"
print(greeting + name)

# if we want a space, we can add that too
print(greeting + ' ' + name)


age = 24
print(age)

print(type(greeting))
print(type(age))

age_in_words = "2 years"
print(name + f" is {age} years old")
print(type(age))

print(f"Pi is approximately {22 / 7:12.50f}")
pi = 22 / 7
print(f"Pi is approximately {pi:12.50f}")


#Strings - indexing 
a = "Cisco Switch" 
a.index("i")

#Strings - character count 
a = "Cisco Switch" 
a.count("i")

#Strings - finding a character 
a = "Cisco Switch"
a.find("sco")

#Strings - converting the case 
a = "Cisco Switch"

a.lower() #lowercase 
a.upper() #uppercase


#Strings - checking whether the string starts with a character 
a = "Cisco Switch" 
a.startswith("C")


#Strings - checking whether the string ends with a character 
a = "Cisco Switch" 
a.endswith("h")


#Strings - removing a character from the beginning and the end of a string 
a = " Cisco Switch " 
a.strip() #remove whitespaces


b = "$$$Cisco Switch$$$" 
b.strip("$") #remove a certain character


#Strings - removing all occurences of a character from a string 
a = " Cisco Switch "

a.replace(" ", "") #replace each space character with the absence of any character

#Strings - splitting a string by specifying a delimiter; the result is a list 
a = "Cisco,Juniper,HP,Avaya,Nortel" #the delimiter is a comma
a.split(",")


#Strings - inserting a character in between every two characters of the string / joining the characters by using a delimiter

a = "Cisco Switch"
"_".join(a)

capitalize() #Capitalizes first letter of string.
lstrip() #Removes all leading whitespace in string
rstrip() #Removes all trailing whitespace of string
swapcase() #Inverts case for all letters in string
title() #Returns "titlecased" version of string, that is, all words begin with uppercase and the rest are lowercase.
isalnum() #Returns true if string has at least 1 character and all characters are alphanumeric and false otherwise.
isalpha() #Returns true if string has at least 1 character and all characters are alphabetic and false otherwise.
isdigit() #Returns true if string contains only digits and false otherwise.
islower() #Returns true if string has at least 1 cased character and all cased characters are in lowercase and false otherwise.


a = "Cisco" 
b = "2691" 
print(a + b)
#Strings - repetition / multiplying a string 
a = "Cisco" a * 3


#Strings - checking if a character is or is not part of a string 
a = "Cisco" 
"o" in a 
"b" not in a

#Strings - formatting v2 
"Cisco model: {}, {} WAN slots, IOS {}".format("2600XM", 2, 12.4) 
"Cisco model: {0}, {1} WAN slots, IOS {2}".format("2600XM", 2, 12.4)


#slicing:

string1 = "Hello I'm string used for slicing example use me"
string1[5:15]  #slice starting at index 5 up to but NOT including, index 15

string1[5:] #slice starting at index 5 up to the end of the string
string1[:10] #slice starting at the beginning of the string up to, but NOT including, index 10
string1[:] #returns the entire string
string1[-1] #returns the last character in the string
string1[-2] #returns the second to last character in the string 
string1[-9:-1] #extracts a certain substring using negative indexes
string1[::2] #adds a third element called step; skips every second character of the string
string1[::-1] #returns string1's elements in reverse order