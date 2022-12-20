import time
import psutil
import csv
import re

# Time initialization for calculating performance
initial_time = time.time()

# Read find_words.txt file

find_words_txt = open("find_words.txt", "r")
words_to_find = find_words_txt.read()
words_to_find = words_to_find.split()
find_words_txt.close()

# Reading the text file

text_file = open("t8.shakespeare.txt", 'r')
text = text_file.read().lower()
word_list = re.findall(r'\b[a-z]{3,15}\b', text)

# Read the French dictionary file as a dictionary u
with open('french_dictionary.csv', mode='r') as words:
    reader = csv.reader(words)
    french_dict = {rows[0]: rows[1] for rows in reader}

# creating an english list for all english words in find_words file
english_words = []
for word in word_list:
    if word in words_to_find:
        english_words.append(word)
english_words = set(english_words)
english_words = list(english_words)

# creating a French list for all French words in find_words file
french_words = []
for word in english_words:
    for key, value in french_dict.items():
        if word in key:
            french_words.append(value)

# creating a frequency list for all words

frequency = {}
for word in english_words:
    count = frequency.get(word, 0)
    frequency[word] = count + 1
frequency_list = frequency.keys()

# create frequency list of  the word replacement

f = []
for word in frequency_list:
    f.append(frequency[word])

# zip list of lists for english,French words and their corresponding frequency

final = list(zip(english_words, french_words, f))
# Creating frequency.csv with 3 columns “English Word”, “French Word”, “Frequency”.

csv_header = ['English Word', 'French Word', 'Frequency']

with open('frequency.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(csv_header)
    for row in final:
        for x in row:
            f.write(str(x) + ',')
        f.write('\n')

# create t8.shakespeare.translated.txt output file that contains the words translated to French

temp = text.split()
res = []
for word in temp:
    res.append(french_dict.get(word, word))

res = ' '.join(res)
print()
f = open("t8.shakespeare.translated.txt", "w")
f.write(str(res))
f.close()

# create performance.txt with the time taken for the script to complete and memory used by script

time_taken = time.time() - initial_time
memory_taken = psutil.cpu_percent(time_taken)

f = open("performance.txt", "w")
f.write(f'Time to process: 0 minutes {time_taken} seconds\nMemory used: {memory_taken} MB')
f.close()
