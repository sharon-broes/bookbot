from stats import get_num_words,get_num_char, sorted_list
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_char = get_num_char(text)
    output = sorted_list(num_char)
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...") 
    print(f"----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print(f"----------- Character Count ----------")
    for item in output:
        c = item["char"]
        n = item["num"]
        print(f"{c}: {n}")
    #print(output)
    print(f"============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()
    

main()

    