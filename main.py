def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    letter_count = get_letter_count(text)
    list_of_letters = convert_letters_dict(letter_count)
    #print(list_of_letters)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    for dict in list_of_letters:
        for k, v in dict.items():
            print(f"The '{k}' character was found {v} times")
    print("--- End report ---")

def convert_letters_dict(dict):
    letter_list = []
    def sort_on(d):
        return next(iter(d.values()))

    for k in dict:
        if k.isalpha():
            letter_list.append({k: dict[k]})
    letter_list.sort(reverse=True, key=sort_on)
    return letter_list

def get_book_text(bpath):
    with open(bpath) as f:
        return f.read()
    
def get_word_count(btext):
    total_words = btext.split()
    word_count = len(total_words)
    return word_count

def get_letter_count(btext):
    l_count = {}
    for l in btext:
        letter = l.lower()
        if letter not in l_count:
            l_count[letter] = 1
        else:
            l_count[letter] += 1
    return l_count


main()