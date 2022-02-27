num_1 = int(input("please enter a number: "))
num_2 = int(input("please enter a number: "))
num_3 = int(input("please enter a number: "))

if num_1 > num_2 and num_1 > num_3:
    print(num_1,"is the biggest number")
elif num_2 > num_1 and num_2 > num_3:
    print(num_2,"is the biggest number")
else:
    print(num_3,"is the biggest number")
    
