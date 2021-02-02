
#HEALTH CARE SOFTWARE
import datetime
def func1():
    a = datetime.datetime.now()
    return a

print("1 for Manish, 2 for Akash,3for Rohan")
n1 = int(input())
if n1 == 1:
    print("welcome Manish")
    print("press 1 for adding food and 2 for retrive")
    n2 = int(input())
    if n2==1:
        n3 = input("entre your food")
        f1=open("Manish.txt" , "a")
        a = str(str(func1())) + " " + n3 + "\n"
        print(f1.write(a))
        print("Your record is Added successfully!!!!")
        f1.close()

    elif n2==2:
        print("This is your past details")
        f1 = open("Manish.txt")
        print(f1.read())
        f1.close()

elif n1 == 2:
    print("welcome Akash")
    print("press 1 for adding food and 2 for retrive")
    n4=int(input())
    if n4==1:
        n5=input("entre your food")
        f2 = open("Akash.txt" , "a")
        b = str(str(func1())) + " " + n5+ "\n"
        print(f2.write(b))
        print("Your record is Added successfully!!!!")
        f2.close()

    elif n4==2:
        print("This is your past records")
        f2 = open("Akash.txt")
        print(f2.read())
        f2.close()


elif n1==3:
    print("welcome Rohan")
    print("press 1 for adding food and 2 for retrive")
    n6=int(input())
    if n6==1:
        n7 = input("entre your food")
        f3 = open("Rohan.txt" , "a")
        c = str(str(func1())) + " " + n7 + "\n"
        print(f3.write(c))
        print("Your record is Added successfully!!!!")
        f3.close()

    elif n6==2:
        print("This is your past records")
        f3 = open("Rohan.txt")
        print(f3.read())
        f3.close()
