word_found = False

def main():
    print("Let's get started!")

    number = 20

    while not word_found and number > 0:
        print("Now trying ", number)
        process_words_file(number)
        number -= 1


def process_words_file(number):
    if 1 <= number <= 20:
        filename = f'words_{number:02d}.txt'

        try:
            with open(filename, 'r') as file:
                # Read each line (word) from the file
                for line in file:
                    word = line.strip()  # Remove leading/trailing whitespace
                    # Call the substring function for the word
                    subless_found = no_substring_checker(word)
                    if subless_found:
                        print(word)
        except FileNotFoundError:
            print(f"File {filename} not found.")
    else:
        print("Invalid input. Please enter a number between 1 and 20.")

def no_substring_checker(word):
    substrings = every_substring(word)
    for substring in substrings:
        valid_word_found = is_valid_word(substring)
        if valid_word_found:
            return False
    # global word_found
    # word_found = True
    return True

def every_substring(word):
    substrings = []
    for i in range(len(word)):
        for j in range(i + 1, len(word) + 1):
            substring = word[i:j]
            if substring != word:
                substrings.append(substring)
    return substrings

def binary_search(substring, lines):
    left, right = 0, len(lines) - 1

    while left <= right:
        mid = (left + right) // 2
        word = lines[mid].strip()

        if word == substring:
            return True
        elif word < substring:
            left = mid + 1
        else:
            right = mid - 1

    return False

def is_valid_word(substring):
    num_letters = len(substring)
    filename = f'words_{num_letters:02d}.txt'

    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            return binary_search(substring, lines)

    except FileNotFoundError:
        print(f"File {filename} not found.")
    return False

main()