s1=int(input("Enter subject marks1="))
s2=int(input("Enter subject marks1="))
s3=int(input("Enter subject marks1="))
s4=int(input("Enter subject marks1="))
s5=int(input("Enter subject marks1="))

total = s1 + s2 + s3 + s4 + s5 / 100
per = total *  100

if per >= 90:
    print("Grade A")
elif per >= 80:
    print("Grade B")
elif per >= 70:
    print("Grade C")
elif per >= 60:
    print("Grade D")
elif per >= 40:
    print("Grade E")
elif per < 40:
    print("Fail...")
else:
    print("Enter valid number")