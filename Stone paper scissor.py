import random

lst =["Stone","Paper","Scissor"]
print("Hello dear gamer!!\n There will be 10 rounds between you and computer",
      "\nThose with maximum point will win\n Press :-\n",
      "1. Stone \n2. Paper \n3. Scissor")

hp=0
cp=0
i=0
while i<10:
      choice = random.choice(lst)
      in1=int(input("Your choice :- "))


      if choice=="Stone" and in1==1 :
            print("Computer's choice is",choice)
            print("Your choice is Stone\n")
            print("There is a tie")
            print("Computer point", cp, "Your Point", hp)
            i+=1
            print("Rounds=",i)

      elif choice=="Paper" and in1==2 :
            print("Computer's choice is", choice)
            print("Your choice is Paper\n")
            print("There is a tie")
            print("Computer point", cp, "Your Point", hp)
            i += 1
            print("Rounds=", i,"\n")


      elif choice=="Scissor" and in1==3 :
            print("Computer's choice is", choice)
            print("Your choice is Scissor\n")
            print("There is a tie")
            print("Computer point", cp, "Your Point", hp)
            i += 1
            print("Rounds=", i,"\n")

# wins statement
      elif choice=="Stone" and in1==3:
            print("Computer's choice is", choice)
            print("Your choice is Stone\n")
            print("Computer wins")
            cp=cp+1
            print("Computer point",cp,"Your Point",hp)
            i += 1
            print("Rounds=", i,"\n")

      elif choice=="Scissor" and in1==2:
            print("Computer's choice is", choice)
            print("Your choice is Paper\n")
            print("Computer wins")
            cp=cp+1
            print("Computer point",cp,"Your Point",hp)
            i += 1
            print("Rounds=", i,"\n")

      elif choice=="Paper" and in1==1:
            print("Computer's choice is", choice)
            print("Your choice is Stone\n")
            print("Computer wins")
            cp=cp+1
            print("Computer point",cp,"Your Point",hp)
            i += 1
            print("Rounds=", i,"\n")

      elif choice=="Stone" and in1==2:
            print("Computer's choice is", choice)
            print("Your choice is Paper\n")
            print("You won")
            hp=hp+1
            print("Computer point",cp,"Your Point",hp)
            i += 1
            print("Rounds=", i,"\n")

      elif choice=="Paper" and in1==3:
            print("Computer's choice is", choice)
            print("Your choice is Scissor\n")
            print("You won")
            hp=hp+1
            print("Computer point",cp,"Your Point",hp)
            i += 1
            print("Rounds=", i,"\n")

      elif choice=="Scissor" and in1==1:
            print("Computer's choice is", choice)
            print("Your choice is Stone\n")
            print("You won")
            hp=hp+1
            print("Computer point",cp,"Your Point",hp)
            i += 1
            print("Rounds=", i,"\n")

      elif cp>=6 :
            print("Game Over. Computer won")
            break
      elif hp>=6:
            print("Hurray!!! You won")
            break


if hp>cp:
      print("Hurray!!! You won the game\n")

elif cp>hp:
      print("Computer won the game\n")
