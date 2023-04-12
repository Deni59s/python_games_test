#!/usr/bin/env python3
from brain_games.welcome_home import welcome_name
from brain_games.games import game_even


def main():
    welcome_name(game_even)
    # вызов фунции с запросом имени из дир-ии brain_games/


if __name__ == '__main__':
    main()
