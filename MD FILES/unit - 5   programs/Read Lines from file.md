# Read Lines from a file

<img src="./img/readline.png" style="width:500px;" class="center"/>

## Table of Contents

- [Problem Statement](#problem-statement)
- [Python Code](#python-code)
- [Sample Output](#Sample-Output)
- [Replit Link](#replit-link)



## Problem Statement

<div align="justify"> <p> Python provides inbuilt functions for creating, writing, and reading files. There are two types of files that can be handled in python, normal text files and binary files (written in binary language, 0s, and 1s). In this article, we are going to study reading line by line from a file.  </div></p>

**<div align="justify"> <p>readlines()** is used to read all the lines at a single go and then return them as each line a string element in a list. This function can be used for small files, as it reads the whole file content to the memory, then split it into separate lines. We can iterate over the list and strip the newline ‘\n’ character using strip() function.</div></p>




## Python Code

```python
fileToRead = open("source.txt", "r")
data = fileToRead.readlines()
print(data)
fileToRead.close()

```
```text
source.txt
 Hello Andrew
 ```

## Sample Output
<img src="./img/OPReadLines.JPG" style="width:400px;" class="center"/>

## Replit Link
https://replit.com/@profsathish/ReadLines#main.py

