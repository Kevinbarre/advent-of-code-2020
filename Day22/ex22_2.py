import sys

# On récupère les decks des deux joueurs
player1, player2 = sys.stdin.read().split('\n\n')

player1 = list(map(int, player1.split('\n')[1:]))
player2 = list(map(int, player2.split('\n')[1:-1]))


def play_round(deck1, deck2, previous_game_decks, round_number, game_number):
    # print("-- Round {} (Game {}) --".format(round_number, game_number))
    t = tuple(deck1), tuple(deck2)
    if t in previous_game_decks:
        # Infinite loop, player 1 wins
        deck2.clear()
        return
    previous_game_decks.add(t)

    # print("Player 1's deck: {}".format(deck1))
    # print("Player 2's deck: {}".format(deck2))
    card1, card2 = deck1.pop(0), deck2.pop(0)
    # print("Player 1 plays: {}".format(card1))
    # print("Player 2 plays: {}".format(card2))

    # On vérifie s'il faut un sub-game ou non
    if len(deck1) >= card1 and len(deck2) >= card2:
        # print("Playing a sub-game to determine the winner...")
        # On récupère les decks pour le sub-game
        sub_deck1, sub_deck2 = deck1[:card1], deck2[:card2]
        player1_win = play_subgame(sub_deck1, sub_deck2)
        # print("...anyway, back to game {}.".format(game_number))
        if player1_win:
            # Player 1 win sub-game
            # print("Player 1 wins round {} of game {}!".format(round_number, game_number))
            deck1.append(card1)
            deck1.append(card2)
        else:
            # Player 2 win sub-game
            # print("Player 2 wins round {} of game {}!".format(round_number, game_number))
            deck2.append(card2)
            deck2.append(card1)
    else:
        # Résolution classique
        if card1 > card2:
            # Player 1 win
            # print("Player 1 wins round {} of game {}!".format(round_number, game_number))
            deck1.append(card1)
            deck1.append(card2)
        else:
            # Player 2 win
            # print("Player 2 wins round {} of game {}!".format(round_number, game_number))
            deck2.append(card2)
            deck2.append(card1)


# Numéro du game au global
global_game = 1

subgame_results = {}


def play_subgame(sub_deck1, sub_deck2):
    global global_game
    global_game += 1
    subgame_number = global_game
    # print ("=== Game {} ===".format(subgame_number))

    # Cache des résultats précédents
    t = tuple(sub_deck1), tuple(sub_deck2)
    if t in subgame_results:
        return subgame_results[t]

    subgame_round = 1
    previous_subgame_decks = set()
    while sub_deck1 and sub_deck2:
        play_round(sub_deck1, sub_deck2, previous_subgame_decks, subgame_round, subgame_number)
        subgame_round += 1

    # On renvoie True si le sub_deck1 l'emporte, donc si sub_deck2 est vide
    player1_win = not sub_deck2
    # print("The winner of game {} is player {}!".format(subgame_number, 1 if player1_win else 2))
    subgame_results[t] = player1_win
    return player1_win


# On joue jusqu'à ce qu'un des decks soit vide
main_round = 1
main_previous_game_decks = set()
# print("=== Game 1 ===")
while player1 and player2:
    play_round(player1, player2, main_previous_game_decks, main_round, 1)
    main_round += 1

print("== Post-game results ==")
print("Player 1's deck: {}".format(player1))
print("Player 2's deck: {}".format(player2))


def score(deck):
    return sum((i + 1) * card for i, card in enumerate(reversed(deck)))


if player1:
    print(score(player1))
else:
    print(score(player2))
