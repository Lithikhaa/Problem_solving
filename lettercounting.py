def print_char_count(string):
    char_count = {}
    for char in string:
        char_count[char] = char_count.get(char, 0) + 1

    grouped_chars = {}
    for char, count in char_count.items():
        grouped_chars.setdefault(count, []).append(char)

    for count, chars in sorted(grouped_chars.items(), reverse=True):
        chars_sorted = ''.join(sorted(chars))
        print(''.join(char + str(count) for char in chars_sorted))

if __name__ == "__main__":
    S = input().strip()
    print_char_count(S)