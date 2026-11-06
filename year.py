yr=int(input("Enter a year="))
if yr % 4==0:
    if yr % 100==0:
        if yr % 400==0:
            print(f"{yr} is century leap year")
        else:
            print(f"{yr}leap year but not century leap")
    else:
        print(f"{yr} leap year")
else:
    print(f"{yr} not leap yar")

