# Build a histogram

<img src="./img/Histogram.gif" style="width:400px;" class="center"/>

## Table of Contents

- [Problem Statement](#problem-statement)
- [Python Code](#python-code)
- [Sample Output](#Sample-Output)
- [Replit Link](#replit-link)
- [PythonTutor Link](#pythontutor-link)


## Problem Statement

<div align="justify"> <p> A histogram is basically used to represent data provided in a form of some groups.It is accurate method for the graphical representation of numerical data distribution. It is a type of bar plot where X-axis represents the bin ranges while Y-axis gives information about frequency.  </div></p>




## Python Code

```python
import random
from collections import defaultdict
counters = defaultdict(int)
input_list = []
entries = int(input("Number of entries? "))
for _ in range(entries):
    userval = int(input("Enter value:"))
    input_list.append(userval)
    counters[userval] += 1

if input_list:
    print("Input values", input_list)
    histogram = sorted(counters.items())
    print("Histogram", histogram)
    print("Visualize the histogram")
    for i in range(len(histogram)):
        print(f'{histogram[i][0]:2}', '*' * histogram[i][1])
else:
    print("No values available to build histogram")

################################
# Program No 1
# using dictionary to build the histogram
#   - using a randomizer for input
#   - functionally decomposing the logic
#
#################################
# Build a histogram

# build a random list
# returns a list containing numbers 1 <= v <= maxval
# the list will contain n elements where
#   mincount < n < maxcount


def random_list(mincount, maxcount, maxval, minval=1):
    size = random.randint(mincount, maxcount)
    alist = []
    for _ in range(size):
        alist.append(random.randrange(minval, maxval + 1))
    return alist


arlist = random_list(50, 120, 20, -10)
print("A random list", arlist)


# returns a list containig tuples with
# value and frequency, aka a histogram


def generate_histogram(arlist):
    counters = defaultdict(int)  # inits value to 0
    for number in arlist:
        counters[number] += 1

    histogram = sorted(counters.items())
    return histogram


histo = generate_histogram(arlist)
print("A histogram with", histo)

print("Visualizing the histogram")
for i in range(len(histo)):
    print(f'{histo[i][0]:2}', '*' * histo[i][1])


################################
# Program No 2
# without using dictionary
#
#################################

# returns a list of tuples with value and frequency
def generate_histogram2(arlist):
    counters = [0] * (1 + max(arlist))  # non-zero values

    for number in arlist:
        try:
            counters[number] += 1
        except BaseException:
            print(f'**** Error with {number}!')
            print(f'--- in {histo} with {len(histo)}')

    histogram = [(i, n)
                 for i, n in enumerate(counters) if n
                 ]
    return histogram


arlist = random_list(50, 120, 20)  # positive integers
print("A random list", arlist)

histo = generate_histogram2(arlist)
print("A histogram with", histo)

print("Visualizing the histogram")
for i in range(len(histo)):
    print(f'{histo[i][0]:2}', '*' * histo[i][1])
    
```

## Sample Output
<img src="./img/OPHistogram.PNG" style="width:400px;" class="center"/>

## Replit Link
https://tinyurl.com/HistogramRepl

## PythonTutor Link

https://tinyurl.com/HistogramVisualize
