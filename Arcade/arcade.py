#  $$$$$\            $$\                                  $$$$$$\  $$\ $$\
# $$  __$$\           $$                                 $$  __$$\ $$ |\__|
# $$ /  \__| $$$$$$\  $$$$$$$\  $$\   $$\  $$$$$$\        $$ /  $$ |$$ |$$\
# $$ |$$$$\ $$  __$$\ $$  __$$\ $$ |  $$ |$$  __$$\       $$$$$$$$ |$$ |$$ |
# $$ |\_$$ |$$ /  $$ |$$ |  $$ |$$ |  $$ |$$ |  \__|      $$  __$$ |$$ |$$ |
# $$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |            $$ |  $$ |$$ |$$ |
# \$$$$$$  |\$$$$$$  |$$ |  $$ |\$$$$$$  |$$ |            $$ |  $$ |$$ |$$ |
#  \______/  \______/ \__|  \__| \______/ \__|            \__|  \__|\__|\__
import random

def adventure():
    Intro = int(input("""You see a castle, Would you like to Enter?
                        1 - Yes
                        2 - No"""))

    if Intro == 1:
        input("""As you enter the castle, a wizard appears. The wizard offers you a special potion.
    As you reach for his hand, he quickly waves his Staff and he steals your possessions from you pocket!
    He disappears into another part of the castle. You must find him!
    Press Enter to Continue your Quest.""")
        room1 = int(input("""You walk around to find him, but you fail.
    You are met by a guard in the Main Hall!
    Would you like to:
    1 - Flee
    2 - Fight with your sword
    3 - Pursuade"""))
        if room1 == 1:
            input("""The Guard runs after you and you are thrown in the Dungeon!
    Press Enter to Quit.""")
        elif room1 == 2:
            input("You killed the guard!\nPress Enter to Continue") #
            room2 = int(input("""After a battle with the guard, You walk in a room near the Entrance of the castle
    You are in the Weapons and Armory room!
    You are met by a Knight!
    Do you want to:
    1 - Flee
    2 - Fight with your sword
    3 - Pursuade to Let you go"""))
            if room2 == 1:
                input("""You try to run away but the Knight Catches you, and Kills you!
    Looks like its the end of your quest!
    Press Enter to Quit.""")
            elif room2 == 2:
                input("""You were unable to kill the guard because of his tough armor!
    The knight takes you to the guards and you are thrown straight to the Dungeon
    Press Enter to Quit.""")
            elif room2 == 3:
                input("The Knight sees your reason and feels bad for you, and lets you go!\nPress Enter to Continue")
                room3 = int(input("""When you get out of the Weapons and Armory room, you feel hungrey.
    So you head to the Kitchen to see whats cooking.
    When you get there you see a Fat Goblin holding 2 Giant cooking knives!
    What do you want to do?:
    1 - Flee
    2 - Fight with your Sword
    3 - Make fun of his gargantuan stomach"""))
                if room3 == 1:
                    input("""You flee for your life, and the fat goblin races after you.
    Luckily the fat goblin wasn't very fast and you were able to run out of the castle.
    When you looked back the doors of the castle were closed!
    Looks like your Quest is over!
    Press Enter to Quit.""")
                elif room3 == 2:
                    input("""You fight the Jumbo goblin till he is in pieces.
    You place his chopped up parts into a boiling pot and
    becomes a tasty stew.
    Press Enter to Continue""")
                    room4 = int(input("""After a delicous meal of goblin stew, you enter the dining room to see
    if that wretched wizard is hanging out. You don't see him but you are met with Royal guards.
    What would you like to do?:
    1 - Flee
    2 - Fight with your sword
    3 - Make a threat"""))
                    if room4 == 1:
                        input("""You Flee and one of the royal guards throw their spear at you
    and you are killed on the spot!
    Please Press Enter to Quit.""")
                    elif room4 == 2:
                        input("""You take out your sword and lunge for one of them, they see that you are
    well trained and they flee the scene.
    Press Enter to Continue""")
                        room5 = int(input("""After the royal guards flee the scence, you see the kings throne room
    and you hope the wizard is there possibly talking to the king. When you enter, all
    you see is an Angry King staring staight at you. Apparently you have walked right
    into a very important meeting.
    What would you like to do?:
    1 - Flee
    2 - Fight with your Sword
    3 - Pursuade
    4 - Make fun of the King"""))
                        if room5 == 1:
                            input("""You flee from the king but apparently the king is an
    all star athlete in track. He captures you and gives you to the guards.
    You are sent straight to the dungeon.
    Press Enter to Quit.""")
                        elif room5 == 2:
                            input("""You attempt to fight the king with your sword, but he is a master
    swords man. He stabs you with his sword but doesn't finish you off, until
    you are sent to the chopping block.
    Press Enter to Quit""")
                        elif room5 == 3:
                            input("""You try to pursuade the king into letting you go,
    but he just slaps, and the noise attracted some guards that
    escorted you to the dragons pit.
    Press Enter to Quit.""")
                        elif room5 == 4:
                            input(""""You make fun of the king, but you immediatly regret your
    decision, because the king starts crying. This brings the attention of
    the whole guard army. Right as the guards are about to shoot you with
    their crossbows, the King stops them and thanks you for your feedback.
    Press Enter to Continue""")
                            room6 = int(input("""After your lucky decision of making fun of the king,
    you go to check your room to see if the wizard is going through your stuff.
    When you enter to your suprise you find NOBODY!
    What do you want to do?:
    1 - Go back outside"""))
                            if room6 == 1:
                                input("""You go out side of your room and you want to check
    if the wizard could be torturing the prisoners.
    Press Enter to Continue""")
                                room7 = int(input("""You enter the dungeon with caution. After
    5 seconds prior to when you entered, your are caught by a
    Dungeon Guard!
    What do you want to do?:
    1 - Flee
    2 - Fight with you sword
    3 - Pursuade to leave you alone"""))
                            if room7 == 1:
                                input("""You run for you life as the dungeon guards chase you.
    Right as you think you can get out of the dungeon, you are hit
    by a giant hammer. You might be stuck in the Dungeon for awhile.
    Press Enter to Quit""")
                            elif room7 == 2:
                                input("""You take out your sword and you fight the tough
    dungeon guard. It was a tough fight but you managed to beat him
    Press Enter to Continue""")
                                room8 = int(input("""After a tough battle with the dungeon guard,
    you go see if the wizard is with his pet dragon. You go to the Dragon
    pit and you see a dragon ten stories tall.
    What do you want to do?:
    1 - Flee
    2 - Fight with sword
    3 - Give affection and become friends"""))
                                if room8 == 1:
                                    input("""You attempt to run away from the dragon, but the dragon
    used its fire breath and you were burnt to crisp. On the plus side
    you made a great BBQ for the dragon.
    Press Enter to Quit""")
                                elif room8 == 2:
                                    input("""You try to take your sword out, but before you know it
    you are already in the dragon's stomach.
    Press Enter to Quit.""")
                                elif room8 == 3:
                                    input("""You remember watching Donkey making friends with a dragon
    in Skrek and you attempt to do the same thing. Luckily for you it worked.
    Press Enter to Continue""")
                                    room9 = int(input("""After befriending a dragon, you remember that you
    haven't checked the liberary. When you get there, you find the professor
    and you remember that you haven't returned your last books that were due
    about 8 years ago.
    What do you want to do?:
    1 - Flee
    2 - Attack with your sword
    3 - Make fun of the Professor's new pair of glasses"""))
                                    if room9 == 1:
                                        input("""You run away from the professor, he runs after you screaming and
    yelling, but all the people that were in the liberary tackled him because
    of the racket he was making.
    Press Enter to Continue""")
                                        room10 = int(input("""Forgetting all of that had just happened, you
    walk around thinking where else the wizard could be. After walking
    around for about 10 minutes you see a room called the Alchemy Room.
    Surely you haven't seen this room before, so you are tempted to
    enter it to see what is on the other side. When you enter the room
    you see the Wizard!
    What do you want to do?:
    1 - Flee
    2 - Fight with sword
    3 - Pursuade"""))
                                        if room10 == 1:
                                            input("""You flee the scene because you see that he has grown more
    powerful than you last saw him. He shoots you with a spell that
    vaporized you.
    Press Enter to Quit.""")
                                        elif room10 == 2:
                                            input("""You see that the wizard has grown much stronger than
    when you last saw him, but you have gone through many trials
    and obsticles, and you too have gotten stronger. You take out
    your sword and you both fight more approxiematly 2 days. In the
    end you won! You defeated the wizard and you got you stolen
    property back and you take all his possesions.
    Press Enter to Quit.""")
                                            input("""Great Job! You have beat the Game!""")
                                        elif room10 == 3:
                                            input("""You pursuade the wizard to give you your things back, but
    he refuses and he right then he turns you into a cockroach and
    squashed you.
    Press Enter to Quit.""")
                                    elif room9 == 2:
                                        input("""You attack the professor with your sword, but now that
    you have killed the professor, it has attracted the attention of
    hundreds of people that are in the liberary. Unfortunatly for you
    the people in the library are wizards, knights, and marksmen in
    training. You didn't survive very long.
    Press Enter to Quit.""")
                                    elif room9 == 3:
                                        input("""You make fun of the professor's new glasses. The professor
    punches you so hard that you are knocked out. The guards throw you
    into the water out side that castle and you are eaten by hungry
    alligators.
    Press Enter to Quit.""")

                            elif room7 == 3:
                                input("""You try to pursuade the dungeon guard to leav you alone
    but he just laughs at you and locks you into the dungeon.
    Press Enter to Quit.""")

                    elif room4 == 3:
                        input("""You threaten the Royal guards that if they stand in your way
    they will be vaporized on the spot they stand. They stare at you for
    a minute and then they burst out laughing at you and they grab you and
    they throw you in the dungeon.
    Press Enter to Quit.""")


                elif room3 == 3:
                    input("""You make fun of his massive stomach and he gets mad, he charges at you, tackels
    you. He then places your body into a boiling pot. You become the king's royal dinner.
    Press Enter to Quit. """)
        elif room1 == 3:
            input("""As you explain to the guard about you situation, another guard comes from the back and picks
    you up. You have been thrown into the dungeon!
    Press Enter to Quit.""")
    elif Intro == 2:
        input("""You walk away...To be Continued
    Press Enter to Quit.""")




def blackjack():
        # in deck of cards there are 52 Cards
    # 4 Suites but suit does not matter in blackjack therefore each suite will have following cards.

    cards = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11]
    random.shuffle(cards)
    print("The Whole Deck of shuffled Cards")
    print(cards)

    # Ace can be 11 or 1
    # J, Q, K are set to 10
    # the rest of the cards 2 - 10 are set to their face value

    # This function will figure aut the total deciding if Ace is 1 or 11
    def total(hand):
        aces = hand.count(11)
        t = sum(hand)
        if t > 21 and aces > 0:
            while aces > 0 and t > 21:
                t -= 10
                aces -= 1
                return t

    #set score to zero.
    c_score = 0
    p_score = 0

    p_hand = []
    p_hand.append(cards.pop())
    p_hand.append(cards.pop())
    print("Player's Cards:")
    print(p_hand)

    player_total = sum(p_hand)
    if player_total > 21:
        print ("The player is busted")
    elif player_total == 21:
        print ("BLACKJACK")
    elif player_total < 17:
        p_hand.append(cards.pop())
        print(p_hand)
        player_total = sum(p_hand)
        print (player_total)
        if player_total > 21:
            print ("The player is busted")

    c_hand = []
    c_hand.append(cards.pop())
    c_hand.append(cards.pop())
    print("Computer's Cards:")
    print(c_hand)

    Comp_total = sum(c_hand)
    if Comp_total > 21:
        print ("The computer is busted")
        exit()
    elif Comp_total == 21:
        print ("BLACKJACK! Computer won")
    elif Comp_total < 17:
        c_hand.append(cards.pop())
        print(c_hand)
        Comp_total = sum(c_hand)
        print (Comp_total)

    if player_total == 21:
        print("Player wins")
        p_score += 1
        print (p_score)
    if player_total <= 20:
        if player_total > Comp_total:
            print("Player wins")
            p_score += 1
            print (p_score)
    elif player_total == Comp_total:
        print("It's a Draw")
    else:
        print("Computer Wins")
        c_score += 1
        print (c_score)



def rps():
    print('Let us play Rock, Paper Scissors!')
    print ('Game of chance 1=Rock, 2=Paper, 3=Scissor')
    print ('Type 5 to quit')

    user_score = 0
    computer_score = 0
    tie = 0

    while 1:
        computer=random.randint(1,3);
        user=int(input("""Please enter number 1 = Rock, 2 = Paper, 3 = Scissors: """))

    ###Computer
    ##    if computer == 1:
    ##        print("computer=1")
    ##    elif computer == 2:
    ##        print("computer=2")
    ##    elif computer == 3:
    ##        print("computer=3")
    ##
    ###User
    ##    if user == 1:
    ##        print("user=1")
    ##    elif user ==2:
    ##        print("user=2")
    ##    elif user ==3:
    ##        print("user=3")

        if computer==user:
            print ('Tie!!!')
            tie += 1

        if user==1 and computer==2:
            print ('Paper covers Rock, You lose')
            computer_score += 1

        if user==1 and computer==3:
            print ('Rock beats Scissors!You Win!!')
            user_score +=1

        if user==2 and computer==1:
            print ('Paper Covers Rock, You Win!!! :(')
            user_score +=1

        if user==2 and computer==3:
            print ('Scissors Cuts Paper, You lose ')
            computer_score +=1

        if user ==3 and computer ==1:
            print("Rock beats scissors, You lose")
            computer_score +=1

        if user ==3 and computer==2:
            print("Scissors cuts paper, You Win!!")
            user_score +=1


        if user==5:
            break
            if user_score > computer_score:
                print("You Won! Great Job")
            elif user_score < computer_score:
                print("You Lost! Maybe Next Time!")

        print("computer score =",+ computer_score)
        print("user score =",+ user_score)
        print("tie =",+ tie)
        print("Games Played=",user_score + computer_score + tie)


        print ('Thanks for playing the game')





def guessgame():
    num = random.randint(1,100)

    ##guess = input("Guess a number between 0 and 100")
    ##tries = int(guess)
    tries = 0
    y = 0

    while y != num:
        y = int(input("What number am I thinking of?"))
        tries += 1
        if y < num:
            print ("Higher")
        if y > num:
            print ("Lower")
        elif y == num:
            print("You got the number")

    print("It took you",+ tries,"Try(s)!")






choice = 0
while choice != "5":
    choice = int(input("""Welcome to Gohur's Arcade!
What Game Would you like to play?
1 - Adventure
2 - BlackJack
3 - Rock Paper Scissors
4 - Guessing Game
5 - Quit"""))
    if choice == 1:
        adventure()
    elif choice ==2:
        blackjack()
    elif choice == 3:
        rps()
    elif choice == 4:
        guessgame()
    elif choice == 5:
        break
