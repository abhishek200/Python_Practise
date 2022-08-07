
firstname = "Varinder"
nameEntered = input("What's your name? ")

lengthfirstname = len(firstname)
lengthnameEntered = len(nameEntered)

if lengthfirstname ==lengthnameEntered:
    i = 0
    chk = 0
    while i<lengthfirstname:
        if firstname[i] != nameEntered[i]:
            chk = 1
            break
        i = i+1
    if chk==0:
        print("\nyes, that's me")
    else:
        print("\nno, that's not me")
else:
    print("\nno, that's not me")