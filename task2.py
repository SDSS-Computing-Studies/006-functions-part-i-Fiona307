#!python3
"""
##### Task 2
Create a function called largest.
The input is a list.
The return value is the largest value in the list
(2 points)
"""
List = []
List.append(input())
List.sort()
def largest(List):
    answer = List[-1]
    return answer
x = largest(List)
print(x)