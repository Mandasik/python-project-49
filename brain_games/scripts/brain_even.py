#!/usr/bin/env python3
from brain_games import game_engine
from brain_games.games import even_odd


def main():
    game_engine.run_game(even_odd)


if __name__ == '__main__':
    main()
