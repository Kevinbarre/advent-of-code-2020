import sys

# On récupère les decks des deux joueurs
player1, player2 = sys.stdin.read().split('\n\n')

player1 = list(map(int, player1.split('\n')[1:]))
player2 = list(map(int, player2.split('\n')[1:-1]))


def play_round(deck1, deck2):
    # print("Player 1's deck: {}".format(deck1))
    # print("Player 2's deck: {}".format(deck2))
    card1, card2 = deck1.pop(0), deck2.pop(0)
    # print("Player 1 plays: {}".format(card1))
    # print("Player 2 plays: {}".format(card2))
    if card1 > card2:
        # Player 1 win
        # print("Player 1 wins the round!")
        deck1.append(card1)
        deck1.append(card2)
    else:
        # Player 2 win
        # print("Player 2 wins the round!")
        deck2.append(card2)
        deck2.append(card1)


# On joue jusqu'à ce qu'un des decks soit vide
round = 1
while player1 and player2:
    # print("-- Round {} --".format(round))
    play_round(player1, player2)
    round += 1


# print("== Post-game results ==")
# print("Player 1's deck: {}".format(player1))
# print("Player 2's deck: {}".format(player2))


def score(deck):
    return sum((i + 1) * card for i, card in enumerate(reversed(deck)))


if player1:
    print(score(player1))
else:
    print(score(player2))
