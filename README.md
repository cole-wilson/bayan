# Bayan Machine Learning

Bayan is a small simple Python module to analyze files and strings.

## Example

Below is an example of a program that learns to differentiate between cats and dogs.
It is assumed tat you have downloaded bayan.py in the same diectory as your program.

```python
import bayan as b

b.assign('Cat','Dog') #Assign Cat to category one, an Dog to category two

b.getfile('https://www.example.com/cat.jpg')
b.train(
