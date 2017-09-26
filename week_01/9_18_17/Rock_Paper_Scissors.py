# a program that plays rounds of Rock, Paper, Scissors
New_game = True  # Define New_game, keeps track if user wants to keep playing.
Score_p1 = 0  # Define users scores
Score_p2 = 0
while New_game:  # while loop contains game, will continue to loop while New_game is true
    ply1 = input("Player one input, Rock, Paper Scissors:\n")  # ask for the user input
    ply2 = input('Player two input, Rock, Paper Scissors:\n')
    # if ply1 or ply2 not in ['Rock', 'Paper', 'Scissors', 'rock', 'paper', 'scissors']: #  Tried to add a check,
    # but didn't get it to work
    #     print('Please input either: Rock, Paper, or Scissors')
    #     continue
    if ply2 == ply1:  # various outcomes
        print('Draw!')
        Score_p1 += 0
        Score_p2 += 0
    elif ply1 != ply2:
        if ply1 in ['Rock','rock'] and ply2 in ['Paper','paper']:
            print('Player two wins!')
            Score_p1 += 0
            Score_p2 += 1
        elif ply1 in ['Rock','rock'] and ply2 in ['Scissors','scissors']:
            print('Player one wins!')
            Score_p1 += 1
            Score_p2 += 0
        elif ply1 in ['Paper','paper'] and ply2 in ['Scissors','scissors']:
            print('Player two wins!')
            Score_p1 += 0
            Score_p2 += 1
        elif ply1 in ['paper', 'Paper'] and ply2 in ['Rock', 'rock']:
            print('Player one wins!')
            Score_p1 += 1
            Score_p2 += 0
        elif ply1 in ['Scissors', 'scissors'] and ply2 in ['Rock', 'rock']:
            print('Player two wins!')
            Score_p1 += 0
            Score_p2 += 1
        elif ply1 in ['Scissors', 'scissors'] and ply2 in ['Paper', 'paper']:
            print('Player one wins!')
            Score_p1 += 1
            Score_p2 += 0
    print('Player one score:', Score_p1,'\n''Player two score:', Score_p2)  # prints the the current score
    NG = input('Play again? (Y/N)\n')  # ask the user if they would like to keep playing
    if NG == 'N':  # if they don't want to play it update New_game to False and quits
        New_game = False
        print('Final scores:','\n''Player one score:', Score_p1, '\n''Player two score:', Score_p2)  # prints the final
        # score and de4clares the winner
        if Score_p1 > Score_p2:
            print('Player one is victorious!')
        else:
            print('Player two is victorious!')
