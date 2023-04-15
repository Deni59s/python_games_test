#!/usr/bin/env python3
from brain_games.welcome_home import welcome_name
from brain_games.games import game_calc


def main():
    welcome_name(game_calc)
    #  вызов фунции с запросом имени из дир-ии brain_games/


if __name__ == '__main__':
    main()
