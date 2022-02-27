user_input = input(" Which area and environmnt do you want to calculate (equilateral triangle,rectangle or square: ")

if user_input == "equilateral":
        the_side_of_the_triangle = int(input("Please enter the side of an equilateral triangle(cm):"))
        area = the_side_of_the_triangle *(the_side_of_the_triangle*3.4) / 2
        environment = the_side_of_the_triangle * 3
        print("the area of triangle is: ",area)
        print("the  enviroment of triangle is: ",environment)

elif user_input == "rectangle":
        the_side_of_Square=int(input("please enter the side of square: "))
        environment= 4 * the_side_of_Square
        area = the_side_of_Square * the_side_of_Square
        print("the environment of square is : ",environment)
        print("the area if square is = ",area)
elif user_input == "square":
        the_side_of_Square=int(input("please enter the side of square: "))
        environment= 4 * the_side_of_Square
        area = the_side_of_Square * the_side_of_Square
        print("the environment of square is : ",environment)
        print("the area if square is = ",area)
else:
    print("you entered wrong input")
    
    
