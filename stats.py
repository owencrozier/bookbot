
def sorter(text_name):
    char_count = char_counter(text_name)
    sorted_list = sorted(char_count.items(), key=None)



    for char, count in sorted_list:
        if char.isalpha():
            print(f"{char}: {count}")






def char_counter(text_name):
    contents = get_book_text(text_name)
    char_count = {}
    for char in contents.lower():
        char_count [char] = char_count.get(char, 0) + 1

    # print(char_count.sort(reverse=True, key=sort_on))
    return char_count


def word_counter (text_name):
    string = get_book_text(text_name)
    num_words = len(string.split())
    print(f"Found {num_words} total words")
    return num_words

def get_book_text (filepath):
    with open (filepath) as f:
        contents = f.read()
        return(contents) 

