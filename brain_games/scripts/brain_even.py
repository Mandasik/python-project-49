#!/usr/bin/env python3
from brain_games import game_engine
from brain_games.games import even_odd


def main():
    game_engine.run_game_in_engine(even_odd)


if __name__ == '__main__':
    main()
