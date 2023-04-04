#!/usr/bin/env python3
from brain_games.cli import welcome_user


def main():
    welcome_user()  # вызов фунции с запросом имени из дир-ии brain_games/
    # print('Welcome to the Brain Games!'),
    # не сработала посл-ть при выводе, перенес в cli.py


if __name__ == '__main__':
    main()
