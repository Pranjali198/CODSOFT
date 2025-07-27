print("""================WELCOME TO THE CALCULATOR==========================
       1-> If you want to find addition of two numbers.
       2-> If you want to find subtraction of two numbers.
       3-> If you want to find multiplication of two numbers.
       4-> If you want to find division of two numbers.
       5-> If you want to find floor division of two numbers.
       6-> If you want to find modulus of two numbers.
       7-> If you want to find power of a number.
      """)
while True:
    operation=int(input("Enter the operation you want to perform --> "))
    x=int(input("Enter the first number--> "))
    y=int(input("Enter the second number--> "))
    if operation==1:
        z=x+y
        print("The addition of two number is : ",z)
    elif operation==2:
        z=x-y
        print("The subtraction of two number is : ",z)
    elif operation==3:
        z=x*y
        print("The multiplication of two number is : ",z)
    elif operation==4:
        z=x/y
        print("The division of two number is : ",z)
    elif operation==5:
        z=x//y
        print("The floor division of two number is : ",z)
    elif operation==6:
        z=x%y
        print("The modulus of two number is : ",z)
    elif operation==7:
        z=x**y
        print("The power of a number is : ",z)
    else:
        print("SORRY! BUT  INVALID CHOICE")
    print("PRESS y if you want to continue\nPRESS n if you want to exit")
    choice=input("Do you want to perform more operations-->")
    if choice=='n':
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print("THANK YOU!! FOR USING CALCULATOR")
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        break
