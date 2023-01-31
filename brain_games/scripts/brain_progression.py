#!/usr/bin/env python3
from brain_games.games import progression
from brain_games import cli
from brain_games import in_out


def main():
    in_out.in_o(cli.welcome_user, progression.game4, progression.RULES)


if __name__ == '__main__':
    main()
