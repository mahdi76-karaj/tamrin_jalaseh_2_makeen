the_side_of_triangle_1= int(input("please enter the side of triangle: "))
the_side_of_triangle_2= int(input("please enter the side of triangle: "))
the_side_of_triangle_3= int(input("please enter the side of triangle: "))

if (the_side_of_triangle_1+the_side_of_triangle_2)> the_side_of_triangle_3 and (the_side_of_triangle_1+the_side_of_triangle_3)> the_side_of_triangle_2 and (the_side_of_triangle_2+the_side_of_triangle_3)> the_side_of_triangle_1 :
    print("yes it can be triangle")
else:
    print("no it cann't be triangle")
