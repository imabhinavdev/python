import datetime


def gettime():
    return datetime.datetime.now()
def hms():
    in1=input("Hello Boss, what you want to do?\nPress \nL for log\nR for retrieve\n")
    in2=int(input("What do you want to edit?\nPress\n1.Exercise\n2.Diet\n"))
    if in1=='L' or in1=='l':
        in3=int(input("Whom do you want to edit?\nPress\n1. Harry\n2. Rohan\n3. Rahul\n"))


        if in3==1 and in2==1:
            def two():

                with open("harryex.txt","r+") as a:
                    in4=input("Enter exercise:\n")
                    a.write(str([str(gettime())])+ in4)
            two()
            in11=input("Do you want to add more ? [1.Yes & 2.No]")
            if in11==1:
                if in11 == 1:
                    while (in11 < 2):
                        two()



        elif in3==1 and in2==2:
            with open("harryd.txt","r+") as b:
                in5=input("Enter diet:\n")
                b.write(str([str(gettime())]),":"+in5)

        elif in3==2 and in2==1:
            with open("rohanex.txt","r+") as b:
                in5=input("Enter exercise:\n")
                b.write(str([str(gettime())]), ":"+in5)

        elif in3==2 and in2==2:
            with open("rohand.txt","r+") as b:
                in5=input("Enter diet:\n")
                b.write(str([str(gettime())]), ":"+in5)
        elif in3==3 and in2==1:
            with open("rahulex.txt","r+") as b:
                in5=input("Enter exercise:\n")
                b.write(str([str(gettime())]) ,":"+in5)
        elif in3==3 and in2==2:
            with open("rahuld.txt","r+") as b:
                in5=input("Enter diet:\n")
                b.write(str([str(gettime())]), ":"+in5)
    elif in1=='R' or in1=='r':
        in6 = int(input("Whom do you want to edit?\nPress\n1. Harry\n2. Rohan\n3. Rahul\n"))
        if in6==1 and in2==1:
            with open("harryex.txt") as x:
                y=x.read()
                print(y)
        elif in6==1 and in2==2:
            with open("harryd.txt") as x:
                y=x.read()
                print(y)
        elif in6==2 and in2==1:
            with open("rohanex.txt") as x:
                y=x.read()
                print(y)
        elif in6==2 and in2==2:
            with open("rohand.txt") as x:
                y=x.read()
                print(y)
        elif in6==3 and in2==1:
            with open("rahulex.txt") as x:
                y=x.read()
                print(y)
        elif in6==3 and in2==2:
            with open("rahuld.txt") as x:
                y=x.read()
                print(y)
hms()
in7=int(input("Do you want to repeat?\n Press\n1.Yes\n2.No\n"))
if in7==1:
    in8=1
    while(in8<2):
        hms()
        in8=int(input("Do you want to repeat?\n Press\n1.Yes\n2.No\n"))
else:
    exit()
