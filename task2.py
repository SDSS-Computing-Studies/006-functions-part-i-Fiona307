#!python3
"""
##### Task 2
Create a function called largest.
The input is a list.
The return value is the largest value in the list
(2 points)
"""
List = []
def largest(List):
    num = int(input("Enter the length of the list:"))
    for i in range(0,num):
        b = float(input("Enter the number in the list:"))
        List.append(b)
    List.sort()
    answer = List[-1]
    return answer
x = largest(List)
print(x)