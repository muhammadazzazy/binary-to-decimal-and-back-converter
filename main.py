def bin2dec(binary_string: str):
    dec_val = 0
    for i in range(len(binary_string)):
        if binary_string[i] == '1':
            dec_val += pow(2, len(binary_string)-1-i)
    
    return dec_val

def dec2bin(decimal_value: int):
    binary_string = ''
    while decimal_value > 0:
        binary_string += str(decimal_value % 2)
        decimal_value = decimal_value // 2
    return binary_string[::-1]

if __name__ == '__main__':
    print('This program converts from binary to decimal or vice versa!')
    base_dict = {'Binary': 2, 'Decimal': 10}
    
    base_prompt = 'Enter the base to convert to: '
    base_string = input(base_prompt)
    while not base_string.isnumeric() or int(base_string) not in base_dict.values():
        base_string = input(base_prompt)
    
    base = int(base_string)

    value_prompt = 'Enter the value to convert: '
    
    if base == base_dict['Decimal']:
        binary_string = input(value_prompt)
        
        while not binary_string.isnumeric():
            binary_string = input(value_prompt)
        
        print(f'The decimal value equivalent to the binary string {binary_string} is {bin2dec(binary_string)}.')
    else:
        decimal_string = input(value_prompt)

        while not decimal_string.isnumeric():
            decimal_string = input(value_prompt)
        
        decimal_value = int(decimal_string)
        print(f'The binary string equivalent to the decimal value {decimal_value} is {dec2bin(decimal_value)}.')
