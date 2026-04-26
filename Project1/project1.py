name= input("Hey type your name: ")
print("Hello"+ name + "Welcome to my game!")

should_we_play=input("Do you want to Play?").lower()

if should_we_play=="yes" or should_we_play=="y":
    print("We are gonna Play!")
    weapon=input("Choice a weapon (sword/axe) or none : ").lower()
    direction= input("Do you want to go left or right? (left/right)").lower()

    if direction=="left":
        print("Okay we went left and fell of a cliff,Game over, try again")
    elif direction=="right":
        choice=input("Okay, you now see a bridge , do you want to swim under it or cross it? (swim/cross)").lower()

        if choice=="swim":   
            print("You got eaten by an alligator, you die , the end!")
            exit()
            
        elif (choice=="cross") and (weapon=="sword"):
            print("You just killed an alligator, now you can keep weapon and swim")
        else:
            print("Sorry wrong input Try again!")
        print("Now you are in Final Level")
        next_level=input("Now do you want to go left or right?(left /right)").lower()

        if next_level=="left" :
            print("Chose wrong direction Try Again ")  
        elif next_level=="right":
            choice=input("Okay, now you see a tree , do you want to climb on tree or cut it? (climb/cut)").lower()
            if choice=="climb" and weapon=="sword":
                print("You get bitten by snake, you die, Game over, Try again")
            elif choice=="cut" and weapon=="sword":
                print("You killed a snake and won game ! CONGRATULATIONS... 🎉⭐")  

    else:
        print("Sorry not a valid reply, you die!")
else:
    print("We are NOT Playing...")


