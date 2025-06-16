# main.py
def main():
    book_path = "books/frankenstein.txt" # hardcoded book path
    text = get_book_text(book_path) # get book path from string
    num_words = get_num_words(text) # calculate num words
    chars_dict = get_chars_dict(text) # get char count in book
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict) # sort from most to least

    print(f"--- Begin report of {book_path} ---") # add book title
    print(f"{num_words} words found in the document") # list no of words
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue # skip char if not alphabetical
        print(f"The '{item['char']}' character was found {item['num']} times") # loop print each char with number of times found

    print("--- End report ---")


def get_num_words(text):
    words = text.split() # split all words to list
    return len(words) # return len of list


def sort_on(d):
    return d["num"] # sort by num of chars


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]}) # add char & count to list
    sorted_list.sort(reverse=True, key=sort_on) # reverse sort
    return sorted_list


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower() # lower case for easy check
        if lowered in chars:
            chars[lowered] += 1 # increment char count
        else:
            chars[lowered] = 1 # set to 1 if not in list
    return chars



def get_book_text(path):
    with open(path) as f:
        return f.read() # read from txt file


main()