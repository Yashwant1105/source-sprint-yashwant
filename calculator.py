a = eval(input("Enter the number: "))
b = eval(input("Enter another number: "))
print("1. Sum\n 2.Subtraction\n 3.Multiplication\n 4.Division")
choice = int(input("Enter the operation you want to perform:"))
if choice === 1:
    print(a+b)
elif choice == 2:
    print(a-b)
elif choice == 3:
    print(a*b)
elif choice == 4:
    print(a/b)
else:
    print("Enter valid option!")
    