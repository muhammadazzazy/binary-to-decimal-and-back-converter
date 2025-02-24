from sys import exit
from word2number import w2n


def is_binary(binary_string: str) -> bool:
    if not binary_string.isnumeric():
        return False
    for c in binary_string:
        if c != '0' and c != '1':
            return False

    return True


def bin2dec(binary_string: str) -> int:
    dec_val: int = 0
    for i in range(len(binary_string)):
        if binary_string[i] == '1':
            dec_val += pow(2, len(binary_string)-1-i)

    return dec_val


def dec2bin(decimal_value: int) -> str:
    binary_string: str = ''
    while decimal_value > 0:
        binary_string += str(decimal_value % 2)
        decimal_value = decimal_value // 2
    return binary_string[::-1]


def main() -> None:
    print('Welcome to The Base-2️⃣-to-Base-🔟-and-Back Converter!')
    base_dict: dict[str, int] = {'binary': 2, 'decimal': 10}
    exit_message: str = 'Exiting program...'
    while True:
        try:
            user_input: str = input('Enter the base to convert to: ')
            if user_input == 'exit':
                print(exit_message)
                exit()
            if user_input.isnumeric():
                base: int = int(user_input)
            else:
                base: int = w2n.word_to_num(user_input)

            if base not in base_dict.values():
                print('Base can be either 2 or 10...')
                continue

            user_input = input('Enter the value to convert: ')

            if base == base_dict['binary']:
                dec_val: int = int(user_input)
                bin_equiv: str = dec2bin(dec_val)
                print(f'The binary equivalent of {user_input} is {bin_equiv}.')
            else:
                if is_binary(user_input):
                    bin_val: str = user_input
                    dec_equiv: int = bin2dec(bin_val)
                    print(
                        f'The decimal equivalent of {user_input} is {dec_equiv}.')
                else:
                    print('Please enter a valid binary string...')
                    continue

        except ValueError:
            print('Please enter valid input...')

        except KeyboardInterrupt:
            print(exit_message)
            exit()


if __name__ == '__main__':
    main()
