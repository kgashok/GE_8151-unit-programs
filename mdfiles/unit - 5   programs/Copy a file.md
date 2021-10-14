# Copy a File

<img src="./img/copyfile.jpg" style="width:400px;" class="center"/>

## Table of Contents

- [Problem Statement](#problem-statement)
- [Python Code](#python-code)
- [Sample Output](#Sample-Output)
- [Replit Link](#replit-link)



## Problem Statement

<div align="justify"> <p> Given two text files, the task is to write a Python program to copy contents of the first file into the second file.
The text files which are going to be used are source.txt and dest.txt.  </div></p>




## Python Code


```python
print("--------Before Copying File--------")
print("First Text File Contains ")
f = open("first.txt", "r")
print(f.read())
print("Second Text File Contains ")
f = open("second.txt", "r")
print(f.read())

# open both files
with open('first.txt','r') as firstfile, open('second.txt','a') as secondfile:
      
    # read content from first file
    for line in firstfile:
               
             # append content to second file
             secondfile.write(line)

print("--------After Copying File--------")
print("First Text File Contains ")
f = open("first.txt", "r")
print(f.read())
print("Second Text File Contains ")
f = open("second.txt", "r")
print(f.read())

```
```text
first.txt
 Hello maria
 ```
 ```text
second.txt
 Hi
 ```

## Sample Output
<img src="./img/OPCopyFile.PNG" style="width:400px;" class="center"/>

## Replit Link
https://replit.com/@profsathish/CopyFile#main.py


