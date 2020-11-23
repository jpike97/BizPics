import time
##get letters
word_dict = {}
already_checked = {}
actual_words = []


numwords = 0
#check all combos and such
def permutations(string, step = 0):
    k = 3
    i = 0
    if step == len(string):
        while i + k < len(string) + 1:
            while i + k < len(string) + 1:
                letterslice = string[i:i+k]
                letterstring = "".join(letterslice)
                if letterstring not in already_checked:
                    already_checked[letterstring] = 1
                if already_checked[letterstring] < 2:
                    check_word(letterstring)
                    already_checked[letterstring] += 1
                i+=1
            i=0
            k+=1

    for i in range(step, len(string)):
        string_copy = [character for character in string]
        string_copy[step], string_copy[i] = string_copy[i], string_copy[step]
        permutations(string_copy, step + 1)

def check_word(wordcheck):
    global numwords
    try:
        if (word_dict[wordcheck] == 1):
            actual_words.append(wordcheck)
            numwords += 1
    except:
        pass


letters = input("Enter your letters: ")
if len(letters) > 2:
    start = time.time()
    with open("words_alpha.txt") as f:
        for line in f:
            string_line = line.strip(("\n"))
            word_dict[string_line] = 1

    permutations(letters)
    end = time.time()
    print(end - start)
    print(numwords)
    for x in actual_words:
        print(x)
    







