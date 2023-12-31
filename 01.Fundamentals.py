import sys


#! [Alert: Deprecated method, do not use]  
#? [Query or question: Should this method be exposed in the public API?]  
#// [CommentedOut: Do not use] 
#todo [Refactor: this method so that it conforms to the API. Create some test cases]   
#* [Important: information is highlighted] 


# ===========================================================
#                       Python Syntax                  
# ===========================================================

def main():
    i = 1
    max = 10
    while (i < max):
        print(i)
        i =i + 1
        
main()



# ===========================================================
print(); print ("===" * 35) ; print()                   
# ===========================================================


import keyword

print(keyword.kwlist)

"""
['False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 'async', 'await', 
'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 
'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 
'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']  
"""


# ===========================================================
print(); print ("===" * 35) ; print()                   
# ===========================================================

s = 'This is a string'
print(s)

s = "Another string using double quotes"
print(s)

s = ''' string can span
        multiple line '''
print(s)


# ===========================================================
print(); print ("===" * 35) ; print()                   
# ===========================================================




# ===========================================================
#                    Python Variables                  
# ===========================================================
print()

message = 'Hello, World!'
print(message)

message = 'Good Bye!'
print(message)


# ===========================================================
print(); print ("===" * 35) ; print()                   
# ===========================================================


# ===========================================================
#         Introduction to Python string                 
# ===========================================================
print()

message = 'This is a string in Python'
print(message)

message = "This is also a string"
print(message)

message = "It's a string"
print(message)


message = '"Beautiful is better than ugly.". Said Tim Peters'
print(message)


message = 'It\'s also a valid string'
print(message)

message = r'C:\python\bin'
print(message)



# ===========================================================
print(); print ("===" * 35) ; print()                   
# ===========================================================


help_message = '''
Usage: mysql command
    -h hostname     
    -d database name
    -u username
    -p password 
'''

print(help_message)

# ===========================================================
print(); print ("===" * 35) ; print()                   
# ===========================================================


name = 'John'
message = f'Hi {name}'
print(message)


# ===========================================================
print(); print ("===" * 35) ; print()                   
# ===========================================================


greeting = 'Good ' 'Morning!'
print(greeting)


# ===========================================================
print(); print ("===" * 35) ; print()                   
# ===========================================================


greeting = 'Good '
time = 'Afternoon'

greeting = greeting + time + '!'
print(greeting)


# ===========================================================
print(); print ("===" * 35) ; print()                   
# ===========================================================

 
str = "Python String"
print(str[0])
print(str[1])

print()

print(str[-1])
print(str[-2])


# ===========================================================
print(); print ("===" * 35) ; print()                   
# ===========================================================


str = "Python String"
str_len = len(str)
print(str_len)


# ===========================================================
print(); print ("===" * 35) ; print()                   
# ===========================================================


str = "Python String"
print(str[0:2])

# ===========================================================
print(); print ("===" * 35) ; print()                   
# ===========================================================


# str = "Python String"
# str[0] = 'J'

# ===========================================================
print(); print ("===" * 35) ; print()                   
# ===========================================================


str ="Python String"
new_str = 'J' + str[1:]
print(new_str)


# ===========================================================
print(); print ("===" * 35) ; print()                   
# ===========================================================


# ===========================================================
#                    Python Numbers                
# ===========================================================

print("Python Numbers\n")

count = 10_000_000_000
print(count)



# ===========================================================
print(); print ("===" * 35) ; print()                   
# ===========================================================

# ===========================================================
#         Introduction to Python Boolean data type                
# ===========================================================

print(bool('Hi'))
print(bool(''))
print(bool(100))
print(bool(0))



# ===========================================================
print(); print ("===" * 35) ; print()                   
# ===========================================================





# ===========================================================
#               Python Type Conversion                  
# ===========================================================
print(" Python Type Conversion\n")


price = input('Enter the price ($):')
tax = input('Enter the tax rate (%):')

net_price = int(price) * int(tax) /100

print(f'The net price is ${net_price}')



# ===========================================================
print(); print ("===" * 35) ; print()                   
# ===========================================================





# ===========================================================
print(); print ("===" * 35) ; print()                   
# ===========================================================





# ===========================================================
print(); print ("===" * 35) ; print()                   
# ===========================================================





# ===========================================================
print(); print ("===" * 35) ; print()                   
# ===========================================================
