def classify_triangle(a, b, c):
    if(a == b and a == c):
        result = "Equilateral"
    elif(a==b or a==c or b==c):
        result = "Isosceles"
    else:
        result = "Scalene"
    if((a*a+b*b)==c*c):
        result = result + " and Right"
    print(result)
    return result

if __name__ == "__main__":
    a, b,c = input("Enter three side lengths: ").split()
    
    classify_triangle(int(a),int(b),int(c))

