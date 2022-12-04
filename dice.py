import random


def start():
    print('''\033[1;32;40m$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\033[0;0m
        \033[0;31;40m
          ______     __    ____    _______
         ||     \    ||   /    \  ||
         ||      \   ||  |        ||
         ||       |  ||  |        ||_____
         ||       |  ||   \       ||
         ||______/  _||_   \___/  ||_______\033[0;0m
         \n\033[1;32;40m$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\033[0;0m
        ''')
    print('\nGuess a number between 1 and 12')
    print('If your number matches the sum of the dice roll you win \033[0;31;40mx2\033[0;0m your wager.')
    print('If your number matches one of the dice you win \033[0;31;40mx1.5\033[0;0m your wager.')
    print('if your number matches both dice you win \033[0;31;40mx3\033[0;0m your wager.')
    print('\n')
    money = float(input('Deposit: $'))
    main(money)


def main(money):
    if money == 0:
        print("You're broke")
        start()
    wager = float(input('\nWager: $'))
    if wager > money:
        print("You don't have enough money!")
        main(money)
    guess = int(input('Your guess: '))
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    print('Roll: ' + str(dice1) + ' | ' + str(dice2))
    if int(guess) == dice1 + dice2:
        winnings = wager * 2
        print('\033[0;31;40mYou Win!\033[0;0m ' + str(winnings))
        money = money + wager * 2
    elif int(guess) == dice1:
        if int(guess) == dice2:
            winnings = wager * 3
            print('\033[0;31;40mYou Win!\033[0;0m ' + str(winnings))
            money = money + wager * 3
        else:
            winnings = wager * 1.5
            print('\033[0;31;40mYou Win!\033[0;0m ' + str(winnings))
            money = money + wager * 1.5
    elif int(guess) == dice2:
        winnings = wager * 1.5
        print('\033[0;31;40mYou Win!\033[0;0m ' + str(winnings))
        money = money + wager * 1.5
    else:
        print('You lose')
        money = money - wager
        if money == 0:
            print("\nYou're broke\n")
            start()
    print('Your money: ' + str(money))
    again = input('\nPlay again? y/n ')
    if again == 'y':
        main(money)
    elif again == 'n':
        print('\nThanks for playing!')
        exit()


start()
