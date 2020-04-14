# Open up a source file
file = open("wordcountinafilesource.txt", "r")
# Read the file contents
fileData = file.read()
# reset the pointer to starting of the file
file.seek(0)
fileDataList = file.readlines()
print("FileContains:")
print(len(fileData), ":Characters ")
print(len(fileDataList), ":Lines ")
words = fileData.split(" ")
total_no_of_words = len(words)
print(total_no_of_words, ": Words")
file.close()

# Enhancement
# Case 1: Number of specific words in a file.
# Case 2: Number of specific words in a file at perticular line.
# Case 3: Frequency Analysis of words
