import datetime
def gettime():
    return datetime.datetime.now()
room = [101,102,103,104,105]
eroom= []
i=0
while i==0:

    print("Available room:- ")
    print(room)
    print("Engaged room")
    print(eroom)
    print("What do you want to do? \n Press 1.Info  2.Entry  3.Delete entry  4.Exit")
    in1=int(input())
    if in1==1:
        in2=int(input("Enter room no:- "))
        if in2==101:
            with open("101.txt") as a:
                b = a.read()
                print(b)
                in444=input()
        elif in2==102:
            with open("102") as a:
                b = a.read()
                print(b)
                in444 = input()
        elif in2==103:
            with open("103.txt") as a:
                b = a.read()
                print(b)
                in444 = input()
        elif in2==104:
            with open("104.txt") as a:
                b = a.read()
                print(b)
                in444 = input()

        elif in2==105:
            with open("105.txt" , "r+") as a:
                b = a.read()
                print(b)
                in444 = input()


    elif in1==2:
        print("Rooms available:- ")
        print(room)
        in9=int(input("Enter the room no."))
        if in9==101 :
            with open("101.txt" , "r+") as a:
                in10=input("Enter residents name:- ")
                in11=input("Enter number of days :- ")
                a.write("Name:- "+in10+"\nCheck in date and time "+str([str(gettime())])+ "\nNumber of days :-" +in11)
                room.remove(101)
                eroom.insert(0,101)
                in444 = input()
                # print(eroom)
                # a.write("Number of days:- "+in11)
        elif in9==102 :
            with open("102" , "r+") as a:
                in10=input("Enter residents name:- ")
                in11=input("Enter number of days :- ")
                a.write("Name:- "+in10+"\nCheck in date and time "+str([str(gettime())])+ "\nNumber of days :-" +in11)
                room.remove(102)
                eroom.insert(1,102)
                in444 = input()

        elif in9==103 :
            with open("103.txt" , "r+") as a:
                in10=input("Enter residents name:- ")
                in11=input("Enter number of days :- ")
                a.write("Name:- "+in10+"\nCheck in date and time "+str([str(gettime())])+ "\nNumber of days :-" +in11)
                room.remove(103)
                eroom.insert(2,103)
                in444 = input()
    # print(room)

        elif in9==104 :
            with open("104.txt" , "r+") as a:
                in10=input("Enter residents name:- ")
                in11=input("Enter number of days :- ")
                a.write("Name:- "+in10+"\nCheck in date and time "+str([str(gettime())])+ "\nNumber of days :-" +in11)
                room.remove(102)
                eroom.insert(1,104)
                in444 = input()

        elif in9==105 :
            with open("105.txt" , "r+") as a:
                in10=input("Enter residents name:- ")
                in11=input("Enter number of days :- ")
                a.write("Name:- "+in10+"\nCheck in date and time "+str([str(gettime())])+ "\nNumber of days :-" +in11)
                room.remove(105)
                eroom.insert(1,105)
                in444 = input()

    elif in1==3:
        in20=int(input("Which room entry you want to delete ? "))
        if in20==101:
            if 101 in eroom :
                with open("101.txt", "w") as a:
                    a.write("No data available")

                print("Sucessfully deleted")
                eroom.remove(101)
                room.insert(0, 101)
                in444 = input()
            else:
                print("No data available")
                in444 = input()
        elif in20==102:
            if 102 in eroom :
                with open("102", "w") as a:
                    a.write("No data available")

                print("Sucessfully deleted")
                eroom.remove(102)
                room.insert(1, 102)
                in444 = input()
            else:
                print("No data available")
                in444 = input()
        elif in20 == 103:
            if 103 in eroom:
                with open("103.txt", "w") as a:
                    a.write("No data available")
                    eroom.remove(103)
                    room.insert(2,103)

                print("Sucessfully deleted")
                in444 = input()
            else:
                print("No data available")
                in444 = input()

        elif in20 == 104:
            if 1041 in eroom:
                with open("104.txt", "w") as a:
                    a.write("No data available")

                print("Sucessfully deleted")
                eroom.remove(104)
                room.insert(3, 104)
                in444 = input()
            else:
                print("No data available")
                in444 = input()

        elif in20 == 105:
            if 105 in eroom:
                with open("105.txt", "w") as a:
                    a.write("No data available")

                print("Sucessfully deleted")
                eroom.remove(105)
                room.insert(4, 105)
                in444 = input()
            else:
                print("No data available")
                in444 = input()

    elif in1==4:
        print("Good bye")
        exit()
