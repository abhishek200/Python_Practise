''' A Simple Mensuration Calculator to:
    1. Find perimeter of a Circle, a rectangle or a square
    2. Find area of a Circle, rectangle or square
'''
# defining functions  
def p_circle(radius):  
    ''' Takes radius as parameter and prints its
        circumference.
    '''
    para = 2 * 3.14 * radius  
    print("Circumference of Circle:", para)  
  
def p_rectangle(height, width): 
    ''' Takes height and width of a rectangle as
        parameter and prints its Perimeter.
    ''' 
    para = 2 * (height + width)  
    print("Perimeter of Rectangle:", para)  
  
def p_square(side):  
    ''' Takes side of the square and
        prints its Perimeter.
    '''
    para = 4 * side  
    print("Perimeter of Square:", para)  
  
def a_circle(radius):
    ''' Takes radius of the circle and
        Prints it's area.
    '''  
    area = 3.14 * radius * radius  
    print("Area of Circle:", area)  
  
def a_rectangle(height, width):  
    ''' Takes height and width as parameter
        and prints it's area.
    '''
    area = height * width  
    print("Area of Rectangle:", area)  
  
def a_square(side):  
    ''' Takes side of a square as parameter
        and prints it's area.
    '''
    area = side * side  
    print("Area of Square:", area)  
    
 
  
# printing the starting line  
print("WELCOME TO A SIMPLE MENSURATION PROGRAM")  
  
# creating options  
while True:  
    print("\nMAIN MENU")  
    print("1. Calculate Perimeter")  
    print("2. Calculate Area")  
    print("3. Exit")  
    choice1 = int(input("Enter the Choice:"))  
  
    if choice1 == 1:  
        print("\nCALCULATE PERIMETER")  
        print("1. Circle")  
        print("2. Rectangle")  
        print("3. Square")  
        print("4. Exit")  
        choice2 = int(input("Enter the Choice:"))  
  
        if choice2 == 1:  
            radius = int(input("Enter Radius of Circle:"))  
            p_circle(radius)  
              
        elif choice2 == 2:  
            height = int(input("Enter Height of Rectangle:"))  
            width = int(input("Enter Width of Rectangle:"))  
            p_rectangle(height, width)  
              
        elif choice2 == 3:  
            side = int(input("Enter Side of Square:"))  
            p_square(side)  
  
        elif choice2 == 4:  
            break  
              
        else:  
            print("Oops! Incorrect Choice.")  
      
    elif choice1 == 2:  
        print("\nCALCULATE AREA")  
        print("1. Circle")  
        print("2. Rectangle")  
        print("3. Square")  
        print("4. Exit")  
        choice3 = int(input("Enter the Choice:"))  
  
        if choice3 == 1:  
            radius = int(input("Enter Radius of Circle:"))  
            a_circle(radius)  
              
        elif choice3 == 2:  
            height = int(input("Enter Height of Rectangle:"))  
            width = int(input("Enter Width of Rectangle:"))  
            a_rectangle(height, width)  
              
        elif choice3 == 3:  
            side = int(input("Enter Side of Square:"))  
            a_square(side)  
  
        elif choice3 == 4:  
            break  
              
        else:  
            print("Oops! Incorrect Choice.")  
      
    elif choice1 == 3:
        break
    else:  
        print("Oops! Incorrect Choice.")