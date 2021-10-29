i=18
e=5
while(1):
    print("You have ",e,"chances left")
    in1=int(input("Enter the number:- \n"))
    if in1<=12:
        print("Your number is smaller \nTry again!")
    elif in1>=23:
        print("Your number is very large")
    elif 22>=in1>=20:
        print("You are close, decrease slowly")
    elif 12<in1<17:
        print("You are close, increase slowly")
    elif in1==17 or in1==19:
        print("You are very close ")
    elif in1==18:
        print("Hurrah !!! You gussed the number ")
        break
    e=e-1
    if e==0:
        print("Game Over")
        break
