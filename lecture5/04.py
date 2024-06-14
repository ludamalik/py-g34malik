import sys


def print_help():
    help_message = """
usage: square.py number [-h]

positional arguments:
  number         display a square of a given number

options:
  -h | --help    show this help message and exit
"""
    print(help_message)


def main():
    if len(sys.argv) != 2 or sys.argv[1] in ('-h', '--help'):
        print_help()
        return

    try:
        number = float(sys.argv[1])
        print(f"The square of {number} is {number ** 2}")
    except ValueError:
        print("Please provide a valid number.")


if __name__ == "__main__":
    main()
