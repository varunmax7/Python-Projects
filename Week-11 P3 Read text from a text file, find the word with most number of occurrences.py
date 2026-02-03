# Week 11- Program 3
# Read text from a text file, find the word with most number of occurrences
f1 = open("file1.txt", "r")
f2=f1.read()
f1.close()
frequent_word = " "
frequency = 0
words=f2.lower().replace(',', '').replace('.', '').split(" ")
for i in range(0, len(words)):
    count = 1
    for j in range(i + 1, len(words)):
         if (words[i] == words[j]):
            count = count + 1;
    if (count > frequency):
        frequency = count;
        frequent_word = words[i];
print("-------------------------")
print("File 1 content is as follows: ")
print(f2)
print("-------------------------")
print("File 1 content after splitting will look like as follows: ")
print(words)
print("-------------------------")
print("Most repeated word: ", frequent_word)
print("Frequency: ", frequency)
