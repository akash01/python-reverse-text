''' This programe takes the user input as string, calcutes the length of the string, number of words in the string, the string in reverse and finally it prints the result'''

def process_text():
	# takes the user input
	text = raw_input('Enter your text to reverse: ')
	# reverses the text
	reverse_text = text[::-1]
	# gets the text length
	text_length = len(text)
	# gets the word count
	words_count = len(text.split(' '))
	# prints the result, string lenght, words count and reverse text
	print "Length: %d, Words: %d, Reverse: %s " %(text_length,words_count,reverse_text)

if __name__ == '__main__':
	process_text()