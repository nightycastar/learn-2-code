# INPUTTING / STDIN
> [*See file*](inputting.py)

Printing is the way to display an output, while this inputting is the way to accept value from user. By  using `input()` function declared to variable, the input can be processed later or validated. But inputting value using `input()` function will always returns value to `str` type, so if you want to input `int` type as example, you'll need to attach `int()` at `input()` which result in `int(input())`, etc. (Used `bool()` will always returns `True` if input value wasn't empty string). Adding single string argument on `input()` will make it as input prompt to be showed to user.
<br><br>
Using `input()` without text as an argument like:
```py
... input()
...
```
Will result in an empty blank as an input field.<br>For example, with code like this:
```py
print("Take an input below: ")
input()
```
And the output will be:
```sh
Take an input below:
[nput Field]
```
<br><br>
And the input with text as an argument like:
```py
...
input("Your name: ")
...
```
Will prompt user like this:
```sh
...
Your name: [Input Field]
...
```
<br><br>
### Example
---
```py
# Ask for input without declaring to var (as break with manual continue by user)
print('Count 1')
input('Press [ENTER] to Continue Counting..')
print('Count 2')
# Count 1
# Press [ENTER] to Continue Counting..
# Count 2
# The input can be anything but continuing, must press [ENTER]
# Can be used to stop `while True:` looping so it doesn't overload

# Without inline prompt
print('Insert your name below:')
name = input()
print(f'Your name: {name}')
# Insert your name below:
# [Input Field]
# Your name: [name]

# With inline prompt
age = int(input('Your age: '))
print('Your birth year:', 2025-age)
# Your age: [Input Field]
# Your birth year: [2025-age]

# Walrus operator
if (name := input('What is your name: ')).lower() == 'zara':
  print('Access granted')
else:
  print('Access Denied')
# What is your name: [Input Field]
# [conditional printing]
# Walrus operator works as a gate to define and direct comparison usage without adding extra variable input to define first.
```