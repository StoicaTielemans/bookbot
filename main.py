def main():
    path = "books/frankenstein.txt"
    text = read_file(path)
    # print(text)
    # print(count_words(text))
    # print(count_characters(text))
    print_a_report(text)


def read_file(path):
    with open("books/frankenstein.txt") as f:
        file = f.read()
        return file


def count_words(text):
    count = len(text.split())
    return count


def count_characters(text):
    dir = {}
    words = text.split()
    for word in words:
        for letter in word:
            letter = letter.lower()
            if letter.isalpha():
                if letter in dir:
                    dir[letter] += 1
                else:
                    dir[letter] = 1
    return dir


def print_a_report(text):
    path = "books/frankenstein.txt"
    print(f"--- Begin report of {path} ---")
    print(f"{count_words(text)} words found in the document")
    dir = count_characters(text)
    list_symbols = []
    for symbol in dir:
        temp_dir = {"name": symbol, "num": dir[symbol]}
        list_symbols.append(temp_dir)
    list_symbols.sort(reverse=True, key=sort_on)

    for dir in list_symbols:
        print(f"The '{dir["name"]}' character was found {dir["num"]} times")


def sort_on(dict):
    return dict["num"]


main()
