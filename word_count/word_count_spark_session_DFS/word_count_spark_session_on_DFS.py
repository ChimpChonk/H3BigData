from pyspark.sql import SparkSession
import subprocess

spark = SparkSession.builder.appName("Word Count").getOrCreate()
text = "hdfs://0.0.0.0:19000/input_dir/AChristmasCarol_CharlesDickens_English.txt"

number_of_words = 0
word_dict = {}
line_count = 1

word_count = spark.sparkContext.textFile(text)
line_collect = str(word_count.collect())
words = line_collect.split()

for word in words:
    word = word.lower().strip('.,:;?!-\'"(){}[]').strip()
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1
    number_of_words += 1

try: subprocess.call(["hdfs", "dfs", "-rm", "-r", "hdfs://0.0.0.0:19000/output_dir/output_spark_session.txt"], shell=True)
    
except Exception as e: print(f"Error while deleting ", e)

with open("output_spark_session.txt", "w") as f:
    f.write(f"Total number of words = {number_of_words}\n")
    f.write("Word count: \n")
    for key, value in word_dict.items():
        f.write(f"{line_count}.{key} = {value}\n")
        line_count += 1

subprocess.call(["hadoop","fs","-put","output_spark_session.txt", "hdfs://0.0.0.0:19000/output_dir"], shell=True)
print("complete")

spark.stop()