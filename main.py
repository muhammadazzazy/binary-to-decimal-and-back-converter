from sys import exit


def is_binary(binary_string: str) -> bool:
    if not binary_string.isnumeric():
        return False
    for c in binary_string:
        if c != '0' and c != '1':
            return False

    return True


def bin2dec(binary_string: str) -> int:
    dec_val = 0
    for i in range(len(binary_string)):
        if binary_string[i] == '1':
            dec_val += pow(2, len(binary_string)-1-i)

    return dec_val


def dec2bin(decimal_value: int) -> str:
    binary_string = ''
    while decimal_value > 0:
        binary_string += str(decimal_value % 2)
        decimal_value = decimal_value // 2
    return binary_string[::-1]


def main() -> None:
    print('This program converts from binary to decimal or vice versa!')
    base_dict = {'binary': 2, 'decimal': 10}

    while True:
        try:
            user_input = input('Enter the base to convert to: ')
            if user_input == 'exit':
                print('Thanks for trying my program!')
                exit()

            base = int(user_input)

            if base not in base_dict.values():
                print('Base can be either 2 or 10...')
                continue

            user_input = input('Enter the value to convert: ')

            if base == base_dict['binary']:
                dec_val = int(user_input)
                bin_equiv = dec2bin(dec_val)
                print(f'{user_input} is equivalent to {bin_equiv}.')
            elif base == base_dict['decimal']:
                if is_binary(user_input):
                    bin_val = user_input
                    dec_equiv = bin2dec(bin_val)
                    print(f'{user_input} is equivalent to {dec_equiv}.')
                else:
                    print('Invalid binary string...')
                    continue
            else:
                print('Invalid base...')
        except ValueError:
            print('Invalid input value...')
        except KeyboardInterrupt:
            print('Exiting...')
            exit()


if __name__ == '__main__':
    main()
