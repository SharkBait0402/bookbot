def get_book_text(path):
    with open(path) as f:
        book_contents = f.read()

    return book_contents

def word_count(book_text):
    text_list = book_text.split()
    num_count = len(text_list)
    return f"Found {num_count} total words"

def sort_on(items):
    return items["count"]

def letter_list(book_text):
    char_dict = char_count(book_text)
    char_list = []

    for item in char_dict:
        char_list.append( {"letter": item, "count": char_dict[item]} )

    char_list.sort(reverse=True, key=sort_on)

    return char_list

def char_count(book_text):
    char_list = {}
    for letter in book_text:
        if letter.lower() in char_list and letter != " ":
            char_list[letter.lower()] += 1
        elif letter != " ":
            char_list[letter.lower()] = 1


    return char_list
