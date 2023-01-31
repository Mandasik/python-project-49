#!/usr/bin/env python3
from brain_games.games import calc
from brain_games import cli
from brain_games import in_out


def main():
    in_out.in_o(cli.welcome_user, calc.game2, calc.RULES)


if __name__ == '__main__':
    main()
