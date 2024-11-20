from random import randint
import os

os.system('cls')
print("Vamos jogar Três Dragões!")


team_blue_score = []
team_red_score = []


def first_dragon():
    f_dragon = randint(1, 6)
    return f_dragon


def play_die():
    dice_rolls = (randint(1, 6), randint(1, 6))
    return dice_rolls


def check_point(f_dragon, dies):

    # SE OS DOIS NÚMEROS FOREM IGUAIS
    if dies[0] == f_dragon and dies[1] == f_dragon:
        score = 5

    # SE O PRIMEIRO NÚMERO FOR IGUAL AO DRAGÃO
    elif dies[0] == f_dragon:
        score = 3
        if (dies[1] % 2 == 1) and (f_dragon % 2 == 1):
            score += 1
        elif (dies[1] % 2 == 0) and (f_dragon % 2 == 0):
            score += 1

    # SE O SEGUNDO NÚMERO FOR IGUAL AO DRAGÃO
    elif dies[1] == f_dragon:
        score = 3
        if (dies[0] % 2 == 0) and (f_dragon % 2 == 0):
            score += 1
        elif (dies[0] % 2 == 1) and (f_dragon % 2 == 1):
            score += 1

    # SE O PRIMEIRO NÚMERO E O DRAGÃO FOREM PAR
    elif (dies[0] % 2 == 0) and (f_dragon % 2 == 0):
        score = 1
        if (dies[1] % 2 == 0) and (f_dragon % 2 == 0):
            score += 1

    # SE O SEGUNDO NÚMERO O E O DRAGÃO FOREM PAR
    elif (dies[1] % 2 == 0) and (f_dragon % 2 == 0):
        score = 1
        if (dies[0] % 2 == 0) and (f_dragon % 2 == 0):
            score += 1

    # SE O PRIMEIRO NÚMERO E O DRAGÃO FOREM ÍMPAR
    elif (dies[0] % 2 == 1) and (f_dragon % 2 == 1):
        score = 1
        if (dies[1] % 2 == 1) and (f_dragon % 2 == 1):
            score += 1

    # SE O SEGUNDO NÚMERO E O DRAGÃO FOREM ÍMPAR
    elif (dies[1] % 2 == 1) and (f_dragon % 2 == 1):
        score = 1
        if (dies[0] % 2 == 1) and (f_dragon % 2 == 1):
            score += 1
    else:
        score = 0
    return score


game_on = 0

while game_on < 3:

    print(f"RODADA ATUAL: {game_on + 1}")

    f_dragon = first_dragon()
    print(f"\n***Primeiro Dragão: {f_dragon}***\n")

    print("É a vez do Time Azul, use o comando 2d6, 'q' pra finalizar")
    choice_blue = input("\n--->  ")
    if choice_blue == "2d6":
        blue_dies = play_die()
        blue_results = check_point(f_dragon, blue_dies)
        print(f"Você rolou {blue_dies[0]}, {blue_dies[1]}!")
        print(f"Pontuação da Rodada: {blue_results}")
        team_blue_score.append(blue_results)
    else:
        game_on = 4
        break

    print("É a vez do Time Vermelho, use o comando 2d6, 'q' pra finalizar")
    choice_red = input("\n--->  ")
    if choice_red == "2d6":
        red_dies = play_die()
        red_results = check_point(f_dragon, red_dies)
        print(f"Você rolou {red_dies[0]}, {red_dies[1]}")
        print(f"Pontuação da Rodada: {red_results}")
        team_red_score.append(red_results)
    else:
        game_on = 3
        break

    game_on += 1

    input("Próxima Rodada: ")
    os.system('cls')

print("Blue Team Score: ", team_blue_score)
print("Red Team Score: ", team_red_score)
