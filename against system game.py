
import random
print("press s for sun w for water and g for gun ")
ls = ["s" , "w" , "g"]


chance=0
computer_score=0
human_score=0
while(chance < 10):

    a = input("entre your guess")
    computer_choice = random.choice(ls)
    if a=="q":
        print("invalid input")


    elif a=="s" and computer_choice=="g":
        print("computer choice is :" , computer_choice)
        print("your choice:" , a )
        print("your score 0 computer score 1 " , "\n")
        computer_score = computer_score + 1
        chance = chance + 1
    elif a == "s" and computer_choice == "w":
        print("computer choice is :", computer_choice)
        print("your choice:", a )
        print("your score 0 computer score 1 " , "\n")
        computer_score = computer_score + 1
        chance = chance + 1
    elif a == "g" and computer_choice == "w":
        print("computer choice is :", computer_choice)
        print("your choice:", a )
        print("your score 0 computer score 1 " , "\n")
        computer_score = computer_score + 1
        chance = chance + 1
    elif a == "g" and computer_choice == "s":
        print("computer choice is :", computer_choice)
        print("your choice:", a )
        print("your score 0 computer score 1 " , "\n")
        computer_score = computer_score + 1
        chance = chance + 1
    elif a == "w" and computer_choice == "g":
        print("computer choice is :", computer_choice)
        print("your choice:", a )
        print("your score 0 computer score 1 " , "\n")
        computer_score = computer_score + 1
        chance = chance + 1
    elif a=="w" and computer_choice=="s":
        print("computer choice is :", computer_choice)
        print("your choice:", a )
        print("your score 0 computer score 1 " , "\n")
        computer_score = computer_score + 1
        chance = chance + 1
    elif a=="w" and computer_choice=="w":
        print("computer choice is :", computer_choice)
        print("your choice:", a)
        print("your score 1 computer score 0 " , "\n")
        human_score=human_score+1
        chance = chance + 1
    elif a=="s" and computer_choice=="s":
        print("computer choice is :", computer_choice)
        print("your choice:", a )
        print("your score 1 computer score 0 " , "\n")
        human_score = human_score + 1
        chance = chance + 1
    elif a=="g" and computer_choice=="g":
        print("computer choice is :", computer_choice)
        print("your choice:", a )
        print("your score 1 computer score 0 " , "\n")
        human_score = human_score + 1
        chance = chance + 1

        if chance > 10:
            print("chances ended")
            break

else:
    pass

print("computer score is :" , computer_score)
print("human score is:" , human_score)

if computer_score > human_score:
    print("computer wins")

else:
    print("human wins")
