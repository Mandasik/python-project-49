#!/usr/bin/env python3
from brain_games import cli
from brain_games.games import prime


def main():
    moniker = cli.welcome_user()
    prime.game5(moniker)


if __name__ == '__main__':
    main()
