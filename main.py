import sys


def get_file_content(file_path):
    """ Extracts the contents of a file. """

    with open(file_path) as f:
            file_content = f.read()
    
    return file_content


def count_words(text):
    """ Counts the number of words in a string. """

    words = text.split()
    num_words = len(words)
    return num_words


def sort_dict_by_value(unordered):
    """ Sorts a dict in descending order based on its values. """

    ordered = dict(sorted(unordered.items(), key=lambda d: d[1], reverse=True))
    return ordered


def count_characters(text):
    """ Counts the number of times all the letters appear on a text. """

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


def print_report(file_path, num_words, num_characters):
    """ Shows a book report in stdout. """

    print("---")
    print(f"Begin of book report for {file_path}")
    print()
    print(f"\tNumber of words:")
    print()
    print(f"\t\t{num_words}")
    print()
    print("\tList of most used letters:")
    print()
    
    for character in num_characters:
        print(f"\t\t{character}: {num_characters[character]}")
    pass

    print()
    print("End of report")
    print("---")


def main():
    """ Runs the program. """

    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        raise Exception("Command format: python3 bookbot.py path/to/book/file/")
    
    file_content = get_file_content(file_path)
    num_words = count_words(file_content)
    num_characters = count_characters(file_content)
    print_report(file_path, num_words, num_characters)


main()