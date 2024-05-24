# Define string type variables
# Getting type and help
# using count to find occurrences
# find for a character or substring from main string
# Dealing with case of string such as lower case and upper case
# string validate functions which start with is
# check if the string contains integer

s = 'GOOD morning'
print(type(s))
sss=s.index('g')
print(sss)
aa=s.find('m')
print(aa)
capital=s.upper()
print(capital)
smaller=capital.lower()
print(smaller)
case_change=smaller.swapcase()
print(case_change)

n = '10'
new = print(n.isdigit())
print(new)
print(n)

''' replace function -- characters or substrings will be replaced with new charactes of substring 
here space was removed between string'''

name = 'sai ram'
combine_name=name.replace(' ','')
print(combine_name)
name.replace('ram','sai')
print(name.replace('ram','sai'))
name.removeprefix('sai ')
print(name.removeprefix('sai'))






