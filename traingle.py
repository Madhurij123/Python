s1=int(input("Enter the first side of traingle="))
s2=int(input("Enter the second side of traingle="))
s3=int(input("Enter the third side of traingle="))

if s1 == s2 and s2 == s3:
    print("equilateral")
elif s1 == s2 or s2 == s3:
    print("Scalene traingle")
else:
    print("Isosceles traingle")
