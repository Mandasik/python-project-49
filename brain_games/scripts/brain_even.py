#!/usr/bin/env python3
from brain_games import cli
from brain_games import in_out
from brain_games.games import even_odd


def main():
    in_out.in_o(cli.welcome_user, even_odd.game1, even_odd.RULES)


if __name__ == '__main__':
    main()
