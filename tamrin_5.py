#برنامھ ای بنویسید کھ یک عدد از کاربر بگیرد و محیط و مساحت متساوی الاضلاع را حساب کند
the_side_of_the_triangle = int(input("Please enter the side of an equilateral triangle(cm):"))

area = the_side_of_the_triangle *(the_side_of_the_triangle*3.4) / 2

environment = the_side_of_the_triangle * 3

print("the area of triangle is: ",area)

print("the  enviroment of triangle is: ",environment)
