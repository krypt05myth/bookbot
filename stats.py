def get_book_word_count(book_text):
    splitted = book_text.split()
    # print(splitted)
    counted = len(splitted)  # count(splitted)
    return counted

def get_book_char_count_dict(book_text):
	lowered_book_text = book_text.lower()
	total_chars = len(lowered_book_text)
	each_char_count_dict = {}
	for each in lowered_book_text:
		if each in each_char_count_dict:
			each_char_count_dict[each] += 1
		else:
			each_char_count_dict[each] = 1
	return each_char_count_dict

def sort_on(book_char_count_dict):
	#tuple 'items' comes in, and we want to sort on the second element - ie the value
	return book_char_count_dict[1]

def book_char_count_sorted(book_char_count_dict):
	# .items() turns the dictionary into a list of tuples
	sorted_counts = sorted(book_char_count_dict.items(), reverse=True, key=sort_on)
    # Converts the sorted list of tuples back to a dict
	sorted_dict = dict(sorted_counts)
	return sorted_dict