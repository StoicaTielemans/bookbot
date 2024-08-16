def main():
    path = "books/frankenstein.txt"
    print_file(path)
    print(count_words(path))
    print(count_characters(path))


def print_file(path):
    with open("books/frankenstein.txt") as f:
        file = f.read()
        print(file)


def count_words(path):
    with open(path) as file:
        text = file.read()
        count = len(text.split())
        return count


def count_characters(path):
    with open(path) as file:
        dir = {}
        text = file.read()
        words = text.split()
        for word in words:
            for letter in word:
                letter = letter.lower()
                if letter in dir:
                    dir[letter] += 1
                else:
                    dir[letter] = 1
        return dir


main()
