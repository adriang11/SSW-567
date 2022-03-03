# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from triangle import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classify_triangle(3,4,5),'Right','3,4,5 is a Right triangle')
    def testRightTriangleB(self): 
        self.assertEqual(classify_triangle(5,3,4),'Right','5,3,4 is a Right triangle')
    def testRightTriangleC(self): 
        self.assertEqual(classify_triangle(7,24,25),'Right','7,24,25 is a Right triangle')
    def testRightTriangleD(self): 
        self.assertEqual(classify_triangle(25,7,24),'Right','25,7,24 is a Right triangle')
        
    def testEquilateralTrianglesA(self): 
        self.assertEqual(classify_triangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
    def testEquilateralTrianglesB(self): 
        self.assertEqual(classify_triangle(8,8,8),'Equilateral','8,8,8 should be equilateral')

    def testScaleneTrianglesA(self): 
        self.assertEqual(classify_triangle(12,13,15),'Scalene','12,13,15 should be Scalene')
    def testScaleneTrianglesB(self): 
        self.assertEqual(classify_triangle(7,3,9),'Scalene','7,3,9 should be Scalene')
    
    def testIsoscelesTrianglesA(self): 
        self.assertEqual(classify_triangle(8,8,3),'Isosceles','8,8,3 should be Isosceles')
    def testIsoscelesTrianglesB(self): 
        self.assertEqual(classify_triangle(6,4,6),'Isosceles','6,4,6 should be Isosceles')
    
    def testInvalidInputA(self): 
        self.assertEqual(classify_triangle(500,10,50),'InvalidInput','500,10,50 should be InvalidInput')
    def testInvalidInputB(self): 
        self.assertEqual(classify_triangle(6,4.75,6),'InvalidInput','6,4.75,6 should be InvalidInput')
    
    def testNotATriangleA(self): 
        self.assertEqual(classify_triangle(80,4,6),'NotATriangle','80,4,6 should be NotATriangle')
    def testNotATriangleB(self): 
        self.assertEqual(classify_triangle(3,98,6),'NotATriangle','3,98,6 should be NotATriangle')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

