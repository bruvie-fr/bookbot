
def get_book_text(file_path):
    with open(file_path) as book_text:
        book_content = book_text.read()
        words = len(book_content.split())
        return words

def char_count(file_path):
    letter_dict = {}
    with open(file_path) as book_text:
        book_content = book_text.read()
        words = book_content.split()
        for word in words:
            for letter in word:
                true_letter = letter.lower()
                if true_letter.isalpha():
                    if true_letter in letter_dict:
                        letter_dict[true_letter] += 1
                    else:
                        letter_dict[true_letter] = 1
    return letter_dict

def sort_on(items):
    return items["num"]

def dict_to_list(required_dict):
    letter_list = []
    for name in required_dict:
        base_dict = {
            "char": name,
            "num": required_dict[name],
        }
        letter_list.append(base_dict)
    letter_list.sort(reverse=True, key=sort_on)
    return letter_list



