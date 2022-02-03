from hw1 import classify_triangle

def test():
    assert classify_triangle(1,1,8) == "Isosceles"
    assert classify_triangle(2,7,3) == "Scalene"
    assert classify_triangle(8,6,7) == "Scalene"
    assert classify_triangle(7,7,7) == "Equilateral"
    assert classify_triangle(17,144,145) == "Scalene and Right"
    assert classify_triangle(444,444,444) == "Equilateral"
    assert classify_triangle(9,1,1) == "Isosceles"
    assert classify_triangle(4,2,0) == "Scalene" 
    assert classify_triangle(7,24,25) == "Scalene and Right"

if __name__ == "__main__":
    test()