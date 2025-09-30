from stats import get_book_text, char_count, dict_to_list 
import sys 

if len(sys.argv) == 1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)



def main(words, path):
    print(f"Found {words} total words")
    sorted_list = dict_to_list(char_count(path))
    for dicts in sorted_list:
            print(f"{dicts['char']}: {dicts['num']}")
    

 
main(get_book_text(sys.argv[1]), sys.argv[1]) 


