#!/usr/bin/env python3
from brain_games.games import calc
from brain_games import cli


def main():
    moniker = cli.welcome_user()
    calc.game2(moniker)


if __name__ == '__main__':
    main()
