#!python3

"""
Create a function called distance()
Input is 2 tuples, that each contain an (x,y) coordinate.
Return value is the distance between the (x,y) coordinates.
Note that the coordinates should be signed (positive or negative) floats
(2 points)
"""
import math

def distance(tup1,tup2):

    answer = round(math.sqrt((float(tup1[0])-float(tup2[0]))**2 + (float(tup1[1])-float(tup2[1]))**2),3)
    return answer

x = distance((2,4),(6,3))
print(x)
y = distance((-3,2.2),(1,2))
print(y)