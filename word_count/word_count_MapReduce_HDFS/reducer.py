import sys

word_count = {}
line_count = 1
number_of_words = 0
for line in sys.stdin:
    word, count = line.strip().split('\t')
    if word in word_count:
        word_count[word] += int(count)
    else:
        word_count[word] = int(count)
    number_of_words += 1

for word, count in word_count.items():
    print(f"{word}\t{count}")
    line_count +=1
print(f"Total Number of words: {number_of_words}")
print(f"Total lines: {line_count}")

