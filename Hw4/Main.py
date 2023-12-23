import re
from antlr4 import FileStream
from PassLexer import PassLexer

def main():
    input_file = "input.txt"
    input_stream = FileStream(input_file)
    lexer = PassLexer(input_stream)

    def is_valid_password(password):
        if len(password) < 8:
            return False

        if not any(char.isdigit() for char in password):
            return False

        if not any(char.isupper() for char in password):
            return False

        special_characters = r"[@#$%^&*()-=_+{}|\[;':\",.<>?/]"
        if not re.search(special_characters, password):
            return False

        if ' ' in password:
            return False

        return True

    token_texts = [token.text for token in lexer.getAllTokens()]

    password_input = ''.join(token_texts)

    result = is_valid_password(password_input)

    if result:
        print(password_input)
        if ' ' in token_texts:
            print("False")
        else:
            print("True")

    else:
        print(password_input)
        print("False")


if __name__ == "__main__":
    main()