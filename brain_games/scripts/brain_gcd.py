from brain_games.games import gcd
from brain_games import cli


def main():
    moniker = cli.welcome_user()
    gcd.game3(moniker)


if __name__ == '__main__':
    main()
