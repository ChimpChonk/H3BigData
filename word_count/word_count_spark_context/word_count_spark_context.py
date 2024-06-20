from pyspark import SparkContext
text = "./AChristmasCarol_CharlesDickens_English.txt"

sc = SparkContext(appName="Word Count")
number_of_words = 0
word_dict = {}
line_count = 1

lines = sc.textFile(text)
line_collect = str(lines.collect())
words = line_collect.split()

for word in words:
    word = word.lower().strip('.,:;?!-\'"(){}[]').strip()
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1
    number_of_words += 1

with open ("word_count_spark_context.txt", "w") as f:
    f.write(f"Total number of words = {number_of_words}\n")
    f.write("Word count: \n")
    for key, value in word_dict.items():
        f.write(f"{line_count}.{key} = {value}\n")
        line_count += 1

sc.stop()