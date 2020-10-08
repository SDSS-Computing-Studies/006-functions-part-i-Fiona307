#!python3
"""
NOTE:
If you complete this extension, call your teacher over to have it assessed


Create a program to determine the solutions for a quadratic equation
in the format ax^2 + bx + c = 0
A key is the discriminant: b^2 - 4 * a * c
If the discriminant is negative, there are no solutions
If the discriminant is zero, there is only 1 solution
If the discriminant is positive, there are 2 solutions

If the discriminant is a perfect square, then the equation can
be factored

If the discriminant is non zero, the solutions are:
x = (-b + sqrt(b^2 - 4 * a * c)) / 2a
x = (-b - sqrt(b^2 - 4 * a * c)) / 2a

Assignment criteria:
Create a program that inputs 3 float values: a, b, c
function numSolutions(a,b,c) returns an integer with the number of solutions
function solutions(a,b,c) returns a tuple with the solutions (note that if 1 solution,
then both solutions will be the same)

If there are no solutions:
output is: "There are no real solutions"

If there is one solution:
output is "There is 1 solution, x=??"

If there are two solutions:
output is: "The solutions are x=?? and x=??"
"""
import math

def numSolutions(a,b,c):
    # inputs:
    # float a
    # float b
    # float c
    # Description:
    # Calculate the discriminant of the equation
    discriminant = float(b)**2 - 4*float(a)*float(c)
    # return 0, 1 or 2
    if discriminant < 0:
        return 0
    elif discriminant == 0:
        return 1
    else:
        return 2

def solutions(a,b,c):
    #inputs:
    # float a
    # float b
    # float c
    # Desription:
    # Calculate the solutions
    x = (-float(b) + math.sqrt(float(b)**2 - 4*float(a)*float(c)))/(2*float(a))
    y = (-float(b) - math.sqrt(float(b)**2 - 4*float(a)*float(c)))/(2*float(a))
    # return tuple of float solution1 and float solution2
    solution = (x,y)
    return solution

def title():
    # inputs none
    # return str of All the title and instructions on one line
    title = "This program is used to find the solution of a quadratic equation in the format ax^2 + bx + c = 0."
    instruction = "3 float values: a, b, c were entered in."
    return title + " " + instruction

def main(a,b,c):
    # Display Title and Instructions
    print( title() )
    # Your code and function calls should go here
    num = numSolutions(a,b,c)
    if num == 0:
        print("There are no real solutions")
    if num == 1:
        solution = solutions(a,b,c)
        print("There is 1 solution, x =" + str(solution[0]))
    if num == 2:
        solution = solutions(a,b,c)
        print("THe solutions are x =" + str(solution[0]) + " and x =" + str(solution[1]))

main(2,2,2)