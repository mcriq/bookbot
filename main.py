def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_word_count(text)
    chars_dict = get_chars_dict(text)
    chars_dict_list = convert_dict_list(chars_dict)
    generate_report(num_words, chars_dict_list, book_path)

def generate_report(word_count, chars_list, path):
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document")
    print("\n")
    for char in chars_list:
        count, letter = char.values()
        print(f"The '{letter}' character was found {count} times")
    print("--- End report ---")

def sort_on(dict):
    return dict["count"]

def convert_dict_list(di):
    dict_list = []
    for (key, value) in di.items():
        dict_list.append({"letter": key, "count": value})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list

def get_chars_dict(text):
    chars = {}
    for char in text:
        if char.isalpha():
            lowered = char.lower()
            if lowered in chars:
                chars[lowered] += 1
            else:
                chars[lowered] = 1
    return chars

def get_word_count(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()    

main()