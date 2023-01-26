#!/usr/bin/env python3
from brain_games import cli
from brain_games import even_odd


def main():
    moniker = cli.welcome_user()
    even_odd.game1(moniker)


if __name__ == '__main__':
    main()
