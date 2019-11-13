# Bayan Machine Learning

Bayan is a small simple Python module to analyze files and strings.

## Example

Below is an example of a program that learns to differentiate between cats and dogs.

**It is assumed tat you have downloaded bayan.py in the same diectory as your program.**

```python
import bayan as b

b.assign('Cat','Dog') #Assign Cat to category one, an Dog to category two

f = b.getfile('https://www.example.com/cat1.jpg') #Get file from URL and string it.
b.train(1,f) #Train cat1.jpg to slot 1


f = b.getfile('https://www.example.com/dog1.jpg') #Get file from URL and string it.
b.train(2,f) #Train dog1.jpg to slot 2


f = b.getfile('https://www.example.com/cat2.jpg')#Get file to test.
result = b.analyze(f)

print(result) #Returns '1' for Cat
```
Of course, you must provide it with more exmples.
## Advanced Options
