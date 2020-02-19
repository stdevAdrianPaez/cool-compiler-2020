import lexer as lex
import sys


def exit_with_error(error):
    print(f'CompilerError: {error}')
    exit(1)


def main():
    if len(sys.argv) != 2:
        exit_with_error("invalid number of arguments")

    input_data = ""
    try:
        with open(sys.argv[1]) as f:
            input_data = f.read()
    except FileNotFoundError:
        exit_with_error(f'file {sys.argv[1]} not found')

    lex.test(input_data)


if __name__ == "__main__":
    main()