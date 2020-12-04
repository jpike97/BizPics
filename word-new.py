import time
word_dict = []
count = 0
result_words = []

letters = input("Enter your letters: ")
print(letters)
if len(letters) > 2:
	start = time.time()
	with open("words_alpha.txt") as f:
		for line in f:
			string_line = line.strip(("\n"))
			word_dict.append(string_line)
	for x in word_dict:
		if len(x) < 3:
			continue
		if all(elem in letters for elem in x):
			result_words.append(x)
			count += 1
	print(count)
	end = time.time()
	for x in result_words:
		print(x)
	print(end - start)
	print(count)
