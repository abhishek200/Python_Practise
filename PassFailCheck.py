grade1 = int(input('Enter the 1st grade: '))
grade2 = int(input('Enter the 2nd grade: '))
averagegrade = int((grade1+grade2)/2)

if averagegrade >= 1 and averagegrade <=48:
    print("Fail")
elif averagegrade >= 49 and averagegrade <=50:
    print("Borderline")
else:
    print("Pass")