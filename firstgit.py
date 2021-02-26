# we make here program for simple calculator in python


while True:

    print("enter your choice :\n"
          "1. addition \n"
          "2. subtraction \n"
          "3. multiplication \n"
          "4. division \n"
          "5. exit \n")
    var = int(input())
    if var == 5:
        print(" thanks for using the python calculator")
        break
    print("enter the first no : ")
    var1 = int(input())
    print("enter the second no : ")
    var2 = int(input())
    if var == 1:
        print("sum of ", var1, " and ", var2, " is ", var1 + var2)
    elif var == 2:
        print("subtraction of ", var1, " and ", var2, " is ", var1 - var2)
    elif var == 3:
        print("multiplication of ", var1, " and ", var2, " is ", var1 * var2)
    elif var == 4:
        print("division of ", var1, " and ", var2, " is ", var1 / var2)
    else:
        print("invalid input")

    print(" \n")