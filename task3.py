#!python3
"""
Create a function called perimeter()
The input is a list.
The return value is the sum of all the numbers in the list
added together
(2 points)
"""

def perimeter(List):
    a = 0
    count = len(List)
    for i in range(0,count):
        x = List[i]
        y = x + a
        a = y
    return y

p = perimeter([5,2,6])
print(p)

q = perimeter([9,8,6,5.5])
print(q)