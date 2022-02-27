user_input = input("please enter your Operation(Convert radians to degrees (radian) or Convert degrees to radians(degree): ")

if user_input == "radian":
    radian = int(input("please enter the angel(radian): "))
    degree = (radian * 180 )/3.14
    print("degree = ",degree)
elif usert_input == "degree":
    degree = int(input("please enter the angel(radian): "))
    radian = (degree * 3.14 )/180
    print("radian = ",radian)
else:
    print("you entered wrong Operation")

    
    
