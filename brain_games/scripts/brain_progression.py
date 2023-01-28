#!/usr/bin/env python3
from brain_games import cli
from brain_games.games import progression


def main():
    moniker = cli.welcome_user()
    progression.game4(moniker)


if __name__ == '__main__':
    main()
