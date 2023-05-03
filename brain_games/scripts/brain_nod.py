#!/usr/bin/env python3

from brain_games.engine import start_game
from brain_games.games import brain_nod


def main():
    start_game(brain_nod)


if __name__ == '__main__':
    main()
