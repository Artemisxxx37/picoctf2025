def solve_password():
    target = [0xe1, 0xa7, 0x1e, 0xf8, 0x75, 0x23, 0x7b, 0x61, 0xb9, 0x9d, 0xfc, 0x5a, 0x5b, 0xdf, 0x69, 0xd2, 0xfe, 0x1b, 0xed, 0xf4, 0xed, 0x67, 0xf4]
    result, var_1c_1, var_20_1 = bytearray(27), 0, 0
    for byte in target:
        for j in range(8):
            if var_20_1 == 0: var_20_1 = 1
            if byte & (1 << (7 - j)):
                result[var_1c_1] |= (1 << (7 - var_20_1))
            var_20_1 += 1
            if var_20_1 == 8: var_20_1, var_1c_1 = 0, var_1c_1 + 1
            if var_1c_1 >= 27: break
    return result.decode('latin-1')

try:
    password = solve_password()
    print(f"Password: {password}\nLength: {len(password)}\nBytes: {' '.join(f'{ord(c):02x}' for c in password)}")
    if "pico" in password: print("Possible flag found!")
except Exception as e:
    print(f"Error: {e}")
