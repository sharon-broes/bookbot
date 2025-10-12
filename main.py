from stats import get_num_words
from stats import get_num_char

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_char = get_num_char(text)
    print(f"Found {num_words} total words")
    print(num_char)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    

main()

    