def main():
    book_path = 'frankenstein.txt'
    text = get_book_text(book_path)
    num_words = count_words(text)
    char_dict = dict()
    num_char = count_char(text,char_dict)
    output = f"""--- Begin report of books/frankenstein.txt ---
{num_words} words found in the document
    """
    print(output)
    char_dict = char_dict.sort(reverse=True, key=sort_on)
    for letter in char_dict:
        print(f"The '{letter}' was found {char_dict[letter]} times")
    print("--- End report ---")

def count_words(text):
    text = text.split()
    return len(text)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_char(text,char_dict):
    allowed = "abcdefghijklmnopqrstuvwxyz"
    for letter in text:
        if letter.lower() not in char_dict and letter.lower() in allowed:
            char_dict[letter.lower()] = 1
        elif letter.lower() in allowed:
            char_dict[letter.lower()] += 1
    
    return char_dict

main()

