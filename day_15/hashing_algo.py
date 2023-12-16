def hash_char(char: str, initialisation: int) -> int:
    asc_value = list(bytes(char, "ascii"))[0]
    current_value = asc_value + initialisation
    current_value *= 17
    return current_value % 256

def hash(input: str) -> int:
    current_value = 0
    for char in input:
        current_value = hash_char(char, current_value)
    print(f"the hash of {input} is {current_value}")
    return current_value