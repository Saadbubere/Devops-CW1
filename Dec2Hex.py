import sys

def decimal_to_hex(decimal_value):
    hex_chars = "0123456789ABCDEF"
    hexadecimal = ""
    num = decimal_value

    print(f"Converting {num} to Hex...")
    while num != 0:
        rem = num % 16
        hexadecimal = hex_chars[rem] + hexadecimal
        num //= 16

    print(f"Hexadecimal representation: {hexadecimal}")
    return hexadecimal

if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            decimal_value = int(sys.argv[1])
            decimal_to_hex(decimal_value)
        except ValueError:
            print("ERROR: Input must be an integer!")
    else:
        print("ERROR: Please provide a decimal number!")
