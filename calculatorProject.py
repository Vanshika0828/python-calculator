def calculator():
    print("=== calculator ===")

    while True:
        a=float(input("Enter first number:"))
        b=float(input("Enter second number:"))

        print("\n1.Add\n2.subtract\n3.multiply\n4.divide")
        choice=input("Enter choice:")

        if choice=='1':
          print("Result:",a+b)
        elif choice=='2':
          print("Result:",a-b)
        elif choice=='3':
          print("Result:",a*b)
        elif choice=='4':
          if b!=0:
             print("Result:",a/b)
          else:
             print("Cannot divide by zero")
        else:
            print("invalid choice")

        again=input("Do you want to continue?(y/n):")

        if again.lower()!='y':
            break
calculator()
                    
        
