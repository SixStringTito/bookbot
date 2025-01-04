def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_count = get_char_count(text)
    char_dict = get_char_dict(chars_count)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()
    for item in char_dict:
        if item["char"].isalpha():
            print(f"The {item['char']} character was found {item['num']} times")
    print("--- End report ---")

def get_num_words(text):
    return len(text.split())

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_char_count(text):
    characters = {}
    for c in text:
        lowered = c.lower()
        if lowered in characters:
            characters[lowered] += 1
        else:
            characters[lowered] = 1
    return characters

def sort_on(d):
    return d["num"]

def get_char_dict(dict):
    sorted = []
    for ch in dict:
        sorted.append({"char":ch, "num":dict[ch]})
    sorted.sort(reverse=True,key=sort_on)
    return sorted

main()