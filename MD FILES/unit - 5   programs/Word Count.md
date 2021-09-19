# Word Count
<img src="./img/wordcount.gif" style="width:400px;" class="center"/>

## Table of Contents

- [Problem Statement](#problem-statement)
- [Python Code](#python-code)
- [Sample Output](#Sample-Output)
- [Replit Link](#replit-link)



## Problem Statement

<div align="justify"> <p> Python provides us with a lot of useful methods to work with files. We don’t need any extra module to work on any file. You can read from a file, write to a file or even append any content to a file easily using these methods. The problem statement is to count the number of words in a given file. Split function is quite useful and usually quite generic method to get words out of the list </div></p>




## Python Code


```python
# Open up a source file
file = open("sample.txt", "r")
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
# Case 2: Number of specific words in a file at particular line.
# Case 3: Frequency Analysis of words

```
```text
sample.txt
 Python is an interpreted, high-level, general-purpose 
programming language. Created by Guido van Rossum and first 
released in 1991, Python's design philosophy emphasizes code 
readability with its notable use of significant whitespace. 
Its language constructs and object-oriented approach aim to 
help programmers write clear, logical code for small and 
large-scale projects
```

## Sample Output
<img src="./img/OPWordCount.png" style="width:400px;" class="center"/>

## Replit Link
https://replit.com/@profsathish/wordcount#main.py


