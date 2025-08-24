# PRINTING / STDOUT
> [*See file*](printing.py)

Printing is the way Python displays output to CLI where user can read. `print()` is the function to display output value in Python. Python `print()` function is bit different than C `printf()` function. To do formatted-print in Python, you'll need to use concatenation-format, *f-string*, `.format()`, or *C-based % format* method instead.
<br><br>
### Print Arguments
---
- `*objects`: Things to display, can be direct value or variable. Can be inputted indefinitely with comma as separator of arguments.
- `end`: Thing to add at the end of printing value. Default to `'\n'` (Line break).
- `sep`: Separates each object to be printed with this. Default to `' '` (space).
- `flush`: Prints as it can without waiting code to finish executing. Default to `False`.
- `file`: Output file for this print result written in. To write output to file, there must be an opened file with write permission. Default to `sys.stdout` (CLI).
<br><br>
### Example
---
> Basic String Printing
```py
print('Hello, World!')
# Hello, World!
```
> String Concatenation
```py
print('Hell' 'o')
# Hello
# This connects the string because string behaves like char list, so it's basically list of a single char and connected to make string

print('Good' + 'bye')
# Goodbye
# Just like the previous one, but this uses +
```
> Separated String
```py
print('Hello', 'Andrew')
# Hello Andrew
# string 1 and string 2 separated by comma means it's now connected with `sep` value which not set means default to ' '

print('Py', 'hon', sep='t')
# Python
# 'Py' (str 1) + 't' (sep) + 'hon' (str 2)
```
> Formatted Print
```py
# Value Concatenation Format
print('6 years ago was.. ' + 2025-6 + ', nostalgic..')
# 6 years ago was.. 2019, nostalgic..
# This can be done with comma as well, the difference is + uses no separator while comma uses

# f-string
print(f'Market stock price was raising, up to {0.026*12:.2f}% this month')
# Market stock price was raising, up to 0.31% this month
# f-string uses {VALUE} format-system, while `:.2f` is format style, this means result will be 2 digit decimal

# .format() Function
print("'Settled' is a word with {:_>7} as its 2nd or 3rd verb with its real word length is {} characters".format('d',6))
# 'Settled' is a word with ______d as its 2nd or 3rd verb with its real word length is 6 characters
# .format() fill all `{}` within string connected with arguments it has

# C-based % Format
print('%s has %d balls to play with' % ('Marchel',2))
# Marchel has 2 balls to play with
# %s for string, %d for integer, etc.
```
