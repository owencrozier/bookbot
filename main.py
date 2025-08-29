import sys
from stats import *


def main ():
    if len(sys.argv) == 2:
        book = "/home/ell/bookbot/books/frankenstein.txt"
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        word_counter(sys.argv[1])
        print("--------- Character Count -------")
        sorter(sys.argv[1])
        
        print("============= END ===============")
    
    else: 
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    

if __name__ == "__main__": 
    main()