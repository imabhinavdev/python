import datetime
def gettime():
    return datetime.datetime.now()

room = [101,102,103,104,105]

print("What do you want to do?\n Press \n1.Info\n2.Entry")
in1=int(input())
if in1==1:
    in2=int(input("Enter room no:- "))
    if in2==101:
        with open("101.txt") as a:
            b = a.read()
            print(b)
    elif in2==102:
        with open("102.txt") as a:
            b = a.read()
            print(b)
    elif in2==103:
        with open("103.txt") as a:
            b = a.read()
            print(b)
    elif in2==104:
        with open("104.txt") as a:
            b = a.read()
            print(b)

    elif in2==105:
        with open("105.txt" , "r+") as a:
            b = a.read()
            print(b)


elif in1==2:
    print("Rooms available:- ")
    print(room)
    in9=int(input("Enter the room no."))
    if in9==101 :
        with open("105.txt" , "r+") as a:
            in10=input("Enter residents name:- ")
            in11=input("Enter number of days :- ")
            a.write("Name:- "+in10+"\nCheck in date and time "+str([str(gettime())])+"\nNumber of days :-"+in11)
            room.remove(101)
            # a.write("Number of days:- "+in11)

print(room)

