def get_file_content(file_path):
    with open(file_path) as f:
        file_content = f.read()
    return file_content


def count_words(text):
    words = text.split()
    num_words = len(words)
    return num_words


def sort_dict_by_value(unordered):
    ordered = dict(sorted(unordered.items(), key=lambda d: d[1], reverse=True))
    return ordered


def count_characters(text):
    lower_text = text.lower()
    num_characters = {}

    for character in lower_text:
        if character.isalpha():
            if character in num_characters:
                num_characters[character] += 1
            else:
                num_characters[character] = 1

    num_characters = sort_dict_by_value(num_characters)
    return num_characters


def tab():
    return "  "


def print_report(file_path, num_words, num_characters):
    t = tab()

    print("---")
    print(f"Begin of book report for {file_path}")
    print()
    print(f"{t}Number of words on the file")
    print()
    print(f"{t}{t}{num_words}")
    print()
    print("  Characters found and how many times in descending order")
    print()
    
    for character in num_characters:
        print(f"    {character}: {num_characters[character]}")
    pass

    print()
    print("End of report")
    print("---")


def main():
    file_path = "books/frankenstein.txt"
    file_content = get_file_content(file_path)
    num_words = count_words(file_content)
    num_characters = count_characters(file_content)
    print_report(file_path, num_words, num_characters)


main()