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
        in2=input("Enter room no:- ")

        with open(in2) as a:
            b = a.read()
            print(b)
            in444=input()



    elif in1==2:
        print("Rooms available:- ")
        print(room)
        in9=input("Enter the room no.")

        with open(in9 , "r+") as a:
                in10=input("Enter residents name:- ")
                in11=input("Enter number of days :- ")
                a.write("Name:- "+in10+"\nCheck in date and time "+str([str(gettime())])+ "\nNumber of days :-" +in11)
                room.remove(int(in9))
                eroom.insert(1,int(in9))
                in444 = input()

    elif in1==3:
        in20=input("Which room entry you want to delete ? ")

        if int(in20) in eroom :
            with open(in20, "w") as a:
                a.write("No data available")

                print("Sucessfully deleted")
                eroom.remove(int(in20))
                room.insert(0, int(20))
                in444 = input()
        else:
                print("No data available")
                in444 = input()

    elif in1==4:
        print("Good bye")
        exit()
