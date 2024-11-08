def determine_base_values(target):
    unique_chars = sorted(set(target))
    if len(unique_chars) <= 4:
        base_values = [ord(c) for c in unique_chars]
    else:
        min_char, max_char = min(unique_chars), max(unique_chars)
        step = (ord(max_char) - ord(min_char)) // 3
        base_values = [ord(min_char) + step * i for i in range(4)]
    return sorted(base_values, reverse=True)


def map_chars_to_base_values(unique_chars, base_values):
    char_to_base = {}
    for char in unique_chars:
        char_ord = ord(char)
        closest_base = min(base_values, key=lambda b: abs(char_ord - b))
        char_to_base[char] = (closest_base, char_ord - closest_base)
    return char_to_base


def generate_brainfuck_code(target, base_values, char_to_base):
    code = ""
    current_position = 0

    for char in target:
        base, offset = char_to_base[char]
        target_position = base_values.index(base)

        move_cost = target_position - current_position
        if move_cost > 0:
            code += ">" * move_cost
        elif move_cost < 0:
            code += "<" * (-move_cost)

        current_position = target_position
        code += "$"

        if offset > 0:
            code += "+" * offset
        elif offset < 0:
            code += "-" * (-offset)

        code += ".!"

    code += "@"
    for i in base_values:
        code += chr(i)

    return code

def generate_brainfuck(target):
    base_values = determine_base_values(target)
    unique_chars = sorted(set(target))
    char_to_base = map_chars_to_base_values(unique_chars, base_values)
    return generate_brainfuck_code(target, base_values, char_to_base)


def main():
    login = "XNOVAKF23"
    generated_code = generate_brainfuck(login)
    print(f"login       : {login}")
    print(f"code        : {generated_code}")
    print(f"code length : {len(generated_code)}")


if __name__ == "__main__":
    main()

