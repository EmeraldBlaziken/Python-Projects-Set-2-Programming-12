while True:
    print("You will have to answer 5 of my questions.")

    #I see you are digging deep into the code of this project
    #Well, there are some eastereggs hidden within the questions

    gamemode = input("Would you like to play? (yes/no): ").lower()

    if gamemode != "yes":
        quit()
    
    score = 0

    print("First question: ")
    question = input("How many days are in a year?: ").lower()
    if question == "365" and "three hundred sixty five":
        print("Surprised that you answered that one right")
        score += 1
    else:
        print("You got it wrong, dumbass!")


    print("Second question: ")
    question = input("What colour do most fire trucks have?: ").lower()
    if question == "red":
        print("Alright, you got that one right.")
        score += 1
    else:
        print("You got it wrong, dumbass!")


    print("Third question: ")
    question = input("What is the most docile animal in the world?: ").lower()
    if question == "capybara" and "capybaras":
        print("You got this one right. I bet you won't get the next one.")
        score += 1
    else:
        print("You got it wrong, dumbass!")


    print("Fourth question: ")
    question = input("A Volkswagen Karmann Ghia has no radiatior, why?: ").lower()
    if question == "idk" and "i don't know" and "dunno" and "how should i know" and "i dunno" and "don't know":
        print("Yeah, I don't know why either. We'll skip on that one then...")
        score += 1
    elif question == "air cooled" and "because it's air cooled" and "because air cooled" and "that's because it's air cooled":
        print("Congratulations, you found one of the eastereggs! Not really surprised as you just looked it up I bet.")
        score += 2
    else:
        print("You got it wrong, dumbass!")


    print("Last question: ")
    question = input("do grass grows?: ").lower()
    if question == "yes":
        print("You are not as dumb as I thought you will be!")
    elif question == "birds fly":
        print("Sun shines and brother, I hurt people. I'm a force of nature!")
        print("If you were from where I was from, you'd be dead!")
        score += 2
    
    print("You finished my little questionnaire!")
    print("You finished " + str(score) + " points out of 5!")

    if score < 5:
        print("not a perfect score, but you got it anyway! Not everyone's perfect.")
    elif score == 5:
        print("Nice, you got all of them correct, you deserve a pat on the back!")
    elif score > 5:
        print("GODLIKE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    
    





