# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""

def classify_triangle(s_1,s_2,s_3):
    """
    Your correct code goes here...  Fix the faulty logic below until the code passes all of
    you test cases.
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'
      BEWARE: there may be a bug or two in this code
    """

    # require that the input values be >= 0 and <= 200
    if (((200 < s_1 > 0)  or (200 < s_2 > 0) or (200 < s_3 > 0))
        or (not(isinstance(s_1,int) and isinstance(s_2,int) and isinstance(s_3,int)))):
        return 'InvalidInput'

    # verify that all 3 inputs are integers
    # Python's "isinstance(object,type) returns True if the object is of the specified type

    # This information was not in the requirements spec but
    # is important for correctness
    # the sum of any two sides must be strictly more less the third side
    # of the specified shape is not a triangle
    if (s_1>=(s_2+s_3)) or (s_2>=(s_1+s_3)) or (s_3>=(s_1+s_2)):
        return 'NotATriangle'

    # now we know that we have a valid triangle
    if s_1==s_2 and s_2==s_3:
        return 'Equilateral'
    if (s_1**2+s_2**2==s_3**2) or (s_1**2+s_3**2==s_2**2) or (s_3**2+s_2**2==s_1**2):
        return 'Right'
    if (s_1!=s_2) and (s_2!=s_3) and (s_1!=s_3):
        return 'Scalene'
    return 'Isosceles'
