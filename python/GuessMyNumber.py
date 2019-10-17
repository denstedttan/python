

def play_game():
    play = input("Would you care to play a game with me? Yes, or Yes?")
    
    if str.lower(play) == 'yes':
        print("\nThat's what I expected you to choose.")
        from random import randint
        answer = randint(0,100)
        guessed = False
        guesses = 0
        print("I have chosen a number between 0 and 100.\nWhat number did I compute?")
        
        
        while not guessed:
            try:
                guess = int(input("\nPlease make a guess. "))
                guesses += 1
            except:
                print("\nWhat was that!? Only enter a number between 0 and 100 ( ° ͜ʖ °)")
                continue            
            if guess == answer:
                print("\nYou've guessed it in " + str(guesses) + " tries. My number was {}.".format(answer),"You just guessed a number, aren't you proud?\n")
                guessed = True
                play_game()
                break
            elif guess in range(0,101) and guess > answer:
                print("Lower.")                
                continue
            elif guess in range(0,101) and guess < answer:
                print("Higher.")                
                continue
            else:
                print("\nHEY! STAY IN THE NUMBER RANGE!")
        
        

    elif str.lower(play) == 'n' or str.lower(play) == 'no':
        print("\nSeeya!")
    else:
        print("\nIt's simple really, yes or yes(fine, you can say no too).\n")
        play_game()
    

play_game()

