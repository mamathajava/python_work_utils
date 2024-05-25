# creating function
'''def func():
    print("hello world")
    return
#print(type(func))
# invoking the function
func()'''

def func(n):
    res = (n * (n+1)) / 2
    return res

rrrr=func(4)
print(rrrr)

# advantage of type hints
a: int = 10
b: int = 20
print(a+b)


def evenodd(x):
    if (x % 2 == 0):
        print('even')
    else:
        print('odd')
evenodd(2)
evenodd(3)

def student(firstname, lastname):
    print(firstname, lastname)
student(firstname='greeks', lastname='practice')


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(4))


# Pass by Reference and Pass by Value
def myFun(x):
    x[0] = 20


# Driver Code (Note that lst is modified
# after function call.
lst = [10, 11, 12, 13, 14, 15]
myFun(lst)
print(lst)

def sum_of_squares(n : int):
    sum = (n * (n+1) * (2 * n) +1) / 6
    print(sum)
    return sum
sum_of_squares(4)

def my_func(food):
    #fruits=['aaple','banana','cherry']
    for x in food:
        print(x)
fruits=['aaple','banana','cherry']
my_func(fruits)



