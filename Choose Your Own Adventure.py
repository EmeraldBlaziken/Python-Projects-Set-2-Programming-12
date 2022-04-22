from tkinter.messagebox import YES


name = input("What's your name, lone traveller?: ")
while name == "":
    print("Don't be shy, tell me your name.")
    name = input("What's your name, lone traveller?: ")


print("Welcome", name, "!")
print("I shall give you an allowance of $1500. Make sure to spend it wisely.")
print("You only have 3 lives so be very decisive!")

money = 1500
lives = 3
kills = 0
score = 0

destination = input("After giving your name and receiving your allowance, you find 2 paths that each lead to different places, which one would you go LEFT or RIGHT?: ").lower()
if destination == "":
    print("Tell me where you want to go")
    destination = input("After giving your name and receiving your allowance, you find 2 paths that each lead to different places, which one would you go LEFT or RIGHT?: ").lower()
while destination != "left" and "right":
    print("I don't think you can go there.")
    destination = input("After giving your name to that unoriginal buffoon, you find 2 paths that each lead to different places, which one would you go LEFT or RIGHT?: ").lower()

    
if destination == "left":
    destination2 = input("The left path lead you to a fine looking town with a peaceful civilization. You see a SALOON, and, a STORE, which one would you like to visit?: ").lower()


    if destination2 == "saloon":
        print("You walked into the town's saloon. The place seems to be filled with very mean people. They seemed menacing at first but, they seem pretty chill.")
        decision = input("You took a seat. As you took a seat, the bartender asked you for a drink, would you buy one for $3?: ").lower()

        if decision == "yes":
            money -= 3
            print("BALANCE: " + str(money))
            print("You decided to buy a drink and drank the whole bottle in one chug. The drink was extremely strong that you passed out for only a minute.")
            print("The bartender decided to drag you out of his saloon and left you in the middle of the town.")
            destination2_fromSaloon = input("The saloon seemed to be a fine establishment! Would you like to walk into the STORE or visit the BROTHEL?: ")
        elif decision == "no":
            print("BALANCE: " + str(money))
            print("You politely declied the bartender's offer to buy a drink from him.")
            print("It's starting to get very boring in there so you peacefully walked out of the premises.")
            destination2_fromSaloon = input("The saloon seemed to be a fine establishment! Would you like to walk into the STORE or visit the BROTHEL?: ")

            if destination2_fromSaloon == "store":
                print("You walked into a general store. The store sells some fine items, goods, and provisions in high quality.")
                purchase = input("There are three things the store sells that might help you in your adventure. Would you buy some ASSORTED GOODS ($5), a HUNTING KNIFE($25), or a CASE OF ALCOHOL?: ").lower()
                if purchase == "assorted goods" and "goods":
                    money -= 5
                    print("BALANCE: " + str(money))
                    print("You successfully purchased some assorted goods. I am sure it will be a great benefit to your adventures!")
                if purchase == "hunting knife" and "knife":
                    money -= 25
                    print("BALANCE: " + str(money))
                    print("A hunting knife! That would certainly help you out in your adventure. I could say it's a must-have!")

                rob = input("You know, you could use some extra cash. You could rob the store clerk. Would you do it? (YES/NO):").lower()
                if rob == "yes":
                    money += 50
                    lives -= 1
                    kills += 1
                    score += 100
                    print("BALANCE: " + str(money))
                    print("You decided to point the gun at the store clerk and forced them to give them all their money.")
                    print("The clerk also pulled out a gun. They got a lucky hit on you, but you managed to shoot them to the head, immediately killing them")
                    print("LIVES: " + str(lives))
                    print("KILLS: " + str(kills))
                    destination2_fromSaloonStore = input("Would you like to visit the BROTHEL, or WALK AROUND and SOCIALIZE?: ")

                elif rob == "no":
                    print("BALANCE: " + str(money))
                    print("You thanked the clerk for their service, and peacefully exited their store.")
                    print("You obtained your needs, but there are more things this town offers.")
                    destination2_fromSaloonStore = input("Would you like to visit the BROTHEL, or WALK AROUND and SOCIALIZE?: ")

            

        
        

    
    if destination2 == "store":
        print("You walked into a general store. The store sells some fine items, goods, and provisions in high quality.")
        purchase = input("There are three things the store sells that might help you in your adventure. Would you buy some ASSORTED GOODS ($5), a HUNTING KNIFE($25), or a CASE OF ALCOHOL?: ").lower()
        if purchase == "assorted goods" and "goods":
            money -= 5
            print("BALANCE: " + str(money))
            print("You successfully purchased some assorted goods. I am sure it will be a great benefit to your adventures!")
        if purchase == "hunting knife" and "knife":
            money -= 25
            print("BALANCE: " + str(money))
            print("A hunting knife! That would certainly help you out in your adventure. I could say it's a must-have!")

        rob = input("You know, you could use some extra cash. You could rob the store clerk. Would you do it? (YES/NO):").lower()
        if rob == "yes":
            money += 50
            lives -= 1
            kills += 1
            score += 100
            print("BALANCE: " + str(money))
            print("You decided to point the gun at the store clerk and forced them to give them all their money.")
            print("The clerk also pulled out a gun. They got a lucky hit on you, but you managed to shoot them to the head, immediately killing them")
            print("LIVES: " + str(lives))
            print("KILLS: " + str(kills))
            destination2_fromStore = input("We could visit the SALOON, or the BROTHEL. Which one would you want to go?: ")
            
            if destination2_fromStore == "saloon" and "Saloon":
                print("You walked into the town's saloon. The place seems to be filled with very mean people. They seemed menacing at first but, they seem pretty chill.")
                decision = input("You took a seat. As you took a seat, the bartender asked you for a drink, would you buy one for $3?: ").lower()

                if decision == "yes":
                    money -= 3
                    print("BALANCE: " + str(money))
                    print("You decided to buy a drink and drank the whole bottle in one chug. The drink was extremely strong that you passed out for only a minute.")
                    print("The bartender decided to drag you out of his saloon and left you in the middle of the town.")
                    destination2_fromSaloon = input("The saloon seemed to be a fine establishment! Would you like to walk into the STORE or visit the BROTHEL?: ")

                elif decision == "no":
                    print("BALANCE: " + str(money))
                    print("You politely declied the bartender's offer to buy a drink from him.")
                    print("It's starting to get very boring in there so you peacefully walked out of the premises.")
                    destination2_fromSaloon = input("The saloon seemed to be a fine establishment! Would you like to visit the BROTHEL, or WALK AROUND and SOCIALIZE?: ")


        elif rob == "no":
            print("BALANCE: " + str(money))
            print("You thanked the clerk for their service, and peacefully exited their store.")
            print("You obtained your needs, but there are more things this town offers.")
            destination2_fromStore = input("We could visit the SALOON, or the BROTHEL. Which one would you want to go?: ")

            if destination2_fromStore == "saloon" and "Saloon":
                print("You walked into the town's saloon. The place seems to be filled with very mean people. They seemed menacing at first but, they seem pretty chill.")
                decision = input("You took a seat. As you took a seat, the bartender asked you for a drink, would you buy one for $3?: ").lower()

                if decision == "yes":
                    money -= 3
                    print("BALANCE: " + str(money))
                    print("You decided to buy a drink and drank the whole bottle in one chug. The drink was extremely strong that you passed out for only a minute.")
                    print("The bartender decided to drag you out of his saloon and left you in the middle of the town.")
                    destination2_fromSaloon = input("The saloon seemed to be a fine establishment! Would you like to visit the BROTHEL, or WALK AROUND and SOCIALIZE?: ")
                elif decision == "no":
                    print("BALANCE: " + str(money))
                    print("You politely declied the bartender's offer to buy a drink from him.")
                    print("It's starting to get very boring in there so you peacefully walked out of the premises.")

                    
    


            


    











    