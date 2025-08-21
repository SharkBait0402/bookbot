from stats import word_count
from stats import letter_list
from stats import get_book_text
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


print(len(sys.argv))

path = sys.argv[1]

text = get_book_text(path)

char_list = letter_list(text)

def main():
    print( f" ============ BOOKBOT ============\n Analyzing book found at {path}... \n ----------- Word Count ----------")
    print(word_count(text), "\n--------- Character Count -------")

    for item in char_list:
        if item["letter"].isalpha():
            print( f"{item["letter"]}: {item["count"]}" )
    print("============= END ===============")
main()
