number= int(input("Enter a number: "))
factorial=1

if number==0 or number==1:
    factorial =1
elif number>2:
    for i in range(1,number+1):
        factorial=factorial*i
else:
    print("Enter a valid number")

print("Factorial of {} is :{}".format(number,factorial))
