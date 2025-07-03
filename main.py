from stats import word_counter
from stats import charakter_counter
from stats import sorting_charakters
import sys


def main(imput):
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    text = get_book_text(filepath)
    words = word_counter(text)
    charakters = charakter_counter(text)
    sorted_charakters = sorting_charakters(charakters)


    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words\n--------- Character Count -------")
    for item in sorted_charakters:
        print(f"{item["char"]}: {   item["num"]}")
    print("============= END ===============")




def get_book_text(filepath):
    with open(filepath) as content:
        output = content.read()
    return output




main(sys.argv)