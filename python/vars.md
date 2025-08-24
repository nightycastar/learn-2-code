# VARIABLES
> [*See file*](variables.py)

Variable is an object that stores value, and then it can be used later for referencing or just a value storage. In a simple terms, variable is a container that is used to stores item which can be accessed for later usage. To define a variable in Python, just type variable name at first (*must follow [variable writing rules](#variable-writing-rules) below*) and followed by equal (`=`) sign after name and then value after equal. Variables can be rewritten and do operation. To rewrite, simply declare the variable back. While to do operation, can be declared back with some function, mathematical, or other operations, [*see here*](#operations).

### Variable Writing Rules
---
In writing variable, there are several condition must met the criteria (*Violating will causes error*):
- It can't be named with defined keywords, functions, and other pre-defined things, such as `with`, `for`, `return`, etc. You can either add some letter to make it different.
- It must ***NOT*** be started with number. `2name` is invalid, while `name2` is valid, etc.
- When contained space for name, just concatenate or use underscore (`_`).

There are also few common tips to write a variable (*Violating doesn't cause error*):
- The name must be *'meaningful'*, even though it's not really that important.
- When concatenating words for the name, it's very recommended to use `camelCase` which common technique by most programmers.
- Using type annotation / hinting for easier to understand the code while reading, even if that doesn't really affect the program. Type hinting doesn't really stricten the syntax, you can freely violate the hinting without any error being occured.

### Variable Types
---
There are main known types:
- `str`: String. Text that started and ended by quotation marks (`'` or `"`) (In C, this is *'char list'*). Tripled the quotation mark in start-end side will turns it into multi-line string, while freely placed multi-line string can be used as multi-line comment.
- `int`: Integer, rounded number. In Python, integer can has no limit, while in most languages, the limit is still based on 32-bit floating point (`-2.147.483.648` until `2.147.483.647`). When writing big integer, some people use underscore (`_`) as thousand-separator that Python doesn't conflict with, e.g. `2_000`.
- `float`: Float, a decimal number separated with peridot (`.`) not comma (`,`), e.g. `2.46`.
- `bool`: Boolean, condition. Acts like switch, only has `True` and `False` condition (In Python the first letter must be capitalized unlike in another languages).
- `list`: List, or array. This behaves like large container that can has multiple values in single variable. Data is stored inside square brackets (`[...]`) and separated by comma for each value. To access value inside, you need to call it by index.
- `tuple`: Tuple. Simply it's `list` but can't be modified anymore once defined. Its value written inside regular brace (`(...)`).
- `dict`: Dictionary. Like a `list` but it's set of key and value. Written inside curly brace (`{...}`) with format of `'KEY': VALUE`. Key must be string, while value is in its type form. Accessing value can be using index or key index.
- `None`: None, null. Null value (self-explanatory).

### Operations
---
Operation is the way to modify value. Operations have order hierarchy, like `+` is done after `*` regardless of its position like how math works. And of course, this hierarchy can be manipulated by using brackets `()` to make it priority to evaluate first. There are various operations in Python:
> Mathematical Operations

These operations are number related. The result will also be number.
| Operator | Function | Example |
|-|-|-|
| `+` | Increases value. | `5 + 3` = `8` |
| `-` | Decreases value. | `5 - 3` = `2` |
| `*` | Multiply value. | `5 * 3` = `15` |
| `/` | Divides value. | `5 / 3` = `1.66..7` |
| `//` | Divides value with return as integer. | `5 // 3` = `1` |
| `**` | Raise to power the value. | `5 ** 3` = `125` |
| `%` | Returns remainder of division (for the return decimal, there will be remainder, return `0` if division returns integer) | `5 % 3` = `2` |
| `-x` | Negates value | `-5` |
> Comparison Operations

These operations check for condition. If met, it will result in `True`, otherwise `False`.
| Operator | Function | Example |
|-|-|-|
| `==` | Checks for equal value. | `5 == 3` = `False` |
| `!=` | Checks for different or not equal value. | `5 != 3` = `True` |
| `>` | Check if value is greater (from left). | `5 > 3` = `True` |
| `<` | Check if value is lesser (from left). | `5 < 3` = `False` |
| `>=` | Check if value is greater or equal (from left). | `5 >= 3` = `True` |
| `<=` | Check if value is lesser or equal (from left). | `5 <= 3` = `False` |
> Logic Operations

These operations used to change the condition. [*See 'Logic Gates'*](https://en.wikipedia.org/wiki/Logic_gate)
| Operator | Function | Example |
|-|-|-|
| `and` | Checks for both value are `True`. | `5 < 3 and 5 > 3` = `False` |
| `or` | Checks for at least one of value is `True`. | `5 < 3 or 5 > 3` = `True` |
| `not` | Inverse condition. Must be placed in front of condition. | `not 5 < 3` = `True` |
> Bitwise Operations

These operations work by comparing the binary of value and returns as non-binary number, based on *'Logic Gates'*. For begginers, these operations is kinda difficult to understand, so it's ***not recommended*** to learn, even that these operations very rarely to be used by common users.
| Operator | Function | Example |
|-|-|-|
| `&` | Checks for both binary value are `True` (AND). | `5 & 3` = `1` |
| `\|` | Checks for both binary value are at least one is `True` (OR). | `5 \| 3` = `7` |
| `^` | Checks for single binary value is `True` (XOR). | `5 & 3` = `1` |
| `~` | Inverse binary value (NOT). | `~5` = `-6` |
| `<<` | Left shift binary value. | `2 << 1` = `4` |
| `>>` | Right shift binary value. | `4 >> 1` = `2` |
> Assignment Operations

These operations are used to declare or re-declare value to variable with some self-operation.
| Operator | Function | Example |
|-|-|-|
| `=` | Declares value to variable. | `var = 67` |
| `+=` | Re-declares to self-value added by other value. | `var += 3` = `70` |
| `-=` | Re-declares to self-value subtracted by other value. | `var -= 20` = `50` |
| `*=` | Re-declares to self-value multiplied by other value. | `var *= 2` = `100` |
| `-=` | Re-declares to self-value divided by other value. | `var /= 20` = `5` |
| `//=` | Re-declares to self-value floor-divided by other value. | `var //= 2` = `2` |
| `**=` | Re-declares to self-value raised to power of other value. | `var **= 3` = `8` |
| `%=` | Re-declares to remainder of self-value divided by other value. | `var %= 3` = `2` |
> Attributes Operations

These operations check for value attributes.
| Operator | Function | Example |
|-|-|-|
| `is` | Checks for object identity is equal to this. | `var1 is var2` |
| `is not` | Inverted `is`. | `var1 is not var2` |
| `in` | Checks for object is part of this. | `var1 in var2` |
| `not in` | Inverted `in`. | `var1 not in var2` |

> Other Operations

| Operator | Function | Example |
|-|-|-|
| `!x` | Set value to not `x`. Usually for boolean switch like `not`. | `!True` = `False` |
| `:=` | Assign value as input while used in condition evauation. Called as 'walrus operator'. | `if 'Cory' in (var_input := input('Your name: ')): ...` |
| `func()` | Assign return value to variable if it has. Var types such as `int`, `str`, and other can also be used as function to converts value to corresponding types. | `int(9.37)` = `9` |

### Examples
---
> String
- Defining
```py
name = "Cory"
corporation = 'Bolt Drive'
friends = """
Allie
Fred
Azcoli
"""
height = str(176)
```
- Slicing
```py
subject = 'Quantum Physics'
print(subject[3:13:2])
# nu hs
# String slice is work like array slice (see below about 'array slicing'), so string was single char array that per-char is collected with the rule of array slicing
```
> Integer
```py
age = 23
tax = 2300 * 0.12
corporalProfit = -65_000
promo_code = int("277936")
```
> Float
```py
money_in_bank = 14.75
discountPercent = float("0.15")
```
> Boolean
```py
has_job = True # 0
hasChild = False
amIHappy = bool(0) # Hlep
```
> List
- Defining
```py
toBuy = ["Egg","Eggplant","Fish Egg","vEggie"]
h_e_l_l_o = list("hello")
list_of_number = list(range(3))
# `range()` function is list of number generator commonly used for iteration (See 'looping' topic for iteration)
squared = [x**2 for x in range(5)]
# This one is list comprehension, single line list generator, you'll get this subject later on the future
```
- Accessing, Modifying, and Slicing
```py
day = ['Monday','Tuesday','Wednesday']

# Access
print(day[0])
# Monday
# Each items in list has attribute called 'index', sort of queue for value inside, started from 0 at first

# Inserting
day.append('Thursday')
# New: ['Monday','Tuesday','Wednesday','Thursday']

# Modifying
day[2] = 'Day Off!'
print(day[2])
# Day Off!
# New: ['Monday','Tuesday','Day Off!','Thursday']
# The item of index 2 ('Wednesday') was replaced by 'Day Off!'

# Deleting
day.remove('Tuesday')
# New: ['Monday','Day Off!','Thursday']
# Remove Tuesday
print(f'Removed: {day.pop(1)}')
# Removed: Day Off!
# New: ['Monday','Thursday']
# Removed value on index 1 + output the value popped
day.append('Friday')
day.append('Saturday')
# New: ['Monday','Thursday','Friday','Saturday']

# Slicing
print(day[0:3:2])
# ['Monday', 'Friday']
# List/array slicing is works as take-part-of. It's START:STOP:STEP pattern.
# Start is using index, first item was 0
# Stop is using human-identifying position, start from 1 at first item (basically index + 1)
# Step is 'leap' for items to be taken. Step 2 means first gonna be included, second doesn't, third does, fourth doesn't, and the pattern repeats
```
> Tuple
```py
cube = (10,30,25)
shippingID = tuple([12,65,97,84])
# For accessing, same concept as `list`
```
> Dict
- Defining
```py
member1 = {
  'name':'Josh',
  'age':26
}
member2 = dict([('name','Alice'), ('age',22)])
# I wanted to show dictionary comprehension but it's not commonly used by many people, and i don't get good example here. I might get it for you on later work
```
- Accessing and Modifying
```py
data = {
  'id_m1': 7624,
  'id_m2': 5278,
  'id_m3': 1928,
  'id_m4': 2827,
  'id_m5': 4482,
}

# Accessing
print(data[1])
# 5278
print(data['id_m5'])
# 4482
# This is key-index accessing

# Inserting
data['id_m6'] = 9020
# New = + {'id_m6':9020} at the end

# Modifying
data['id_m4'] = 3353
# New update the value of m4

# Deleting
data.pop('id_m3')
# New will lost the m3 value and return m3 value on this
# There actually other whay other than pop but it's not for early learning concept

# No slicing?
# There should be available, but it has same concept as list slicing
```
> None
```py
this_is_actually_not_cool = None
```
<br><br>
> Writing Variable with Type Annotation / Type Hinting
```py
text : str = "Hello, World!"
# Just add `: <type>` and done

number_or_not : int = "This doesn't error tho"
# It doesn't bother with violation
```