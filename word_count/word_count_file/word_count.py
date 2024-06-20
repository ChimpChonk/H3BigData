
text = "./AChristmasCarol_CharlesDickens_English.txt"

number_of_words = 0
word_dict = {}
line_count = 1 

with open(text, "r") as f:
    data = f.read()
    words = data.split()
    number_of_words = len(words)
    for word in words:
        word = word.lower().strip('.,:;?!-\'"').strip()
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

with open ("word_count.txt", "w") as f:
    f.write(f"Total number of words = {number_of_words}\n")
    f.write("Word count: \n")
    for key, value in word_dict.items():
        f.write(f"{line_count}.{key} = {value}\n")
        line_count += 1


print(f"Total works {number_of_words}")
for key, value in word_dict.items():
    print(f"{line_count}. {key} = {value}")
    line_count += 1


