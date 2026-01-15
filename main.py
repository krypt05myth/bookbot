# print("greetings boots")
# I had the following uncommented to ensure the course test would pass: print("hello boots")
from stats import *
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

#Example of absolute path for my reference
# a = "/mnt/c/Users/kUser/Documents/Coding/Boot.dev/bookbot/books/frankenstein.txt"

#Example of relative path for my reference
# a = "books/frankenstein.txt"

def main():
	a = ""
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)

#This was my solution, but i wanted it more correct/clean, which resulted in remove elif and set path and text vars; see below.
	#elif len(sys.argv) == 2:
		#a = str(input("What is the path?"))
		#a = sys.argv[1]
		#a = "books/frankenstein.txt"

#This is the cleaner way to handle the whole operation
	path = sys.argv[1]
	text = get_book_text(path)

	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {path}...")
	print("----------- Word Count ----------")
	word_count = get_book_word_count(text)
	print(f"Found {word_count} total words")
	#print(f"Per character count is broken down as such: \n{char_count}")
	print("--------- Character Count -------")
	char_count_sorted = book_char_count_sorted(get_book_char_count_dict(text))
#dict.items() gives (key, value) pairs — name them yourself in the loop - Python unpacks to whatever variable names you choose
	for each_char, char_count in char_count_sorted.items():
		print(f"{each_char}: {count}")
	print("============= END ===============")
#quick test to see if I am getting it right!
	#print(f"a: {a}",sys.argv, len(sys.argv))
	
	
	
if __name__ == "__main__":
    main()