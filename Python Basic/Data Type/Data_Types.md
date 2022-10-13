# Data Types

[TOC]

## 1.Overviews

| **Category** | **Data Types**                     |
| ------------ | ---------------------------------- |
| Text         | `str`                              |
| Numeric      | `int`, `float`, `complex`          |
| Sequence     | `list`, `tuple`, `range`           |
| Mapping      | `dict`                             |
| Set          | `set`, `frozenset`                 |
| Boolean      | `bool`                             |
| Binary       | `bytes`, `bytearray`, `memoryview` |

[Top](#Data Types)



## 2.Integers, Floats

```python
type(5)
type(6.1)
type(5.)
int(6.8)
```

```
int
float
float
int
```

[Top](#Data Types)



## 3.Strings

> Can be expressed by using either double quotes (") or single quotes (’). But **<u>double quotes (")</u>** recommended.

### 3.1.Concatenate

```python
"This is a course on " + "Python."
"3 times. " * 3
```

```
'This is a course on Python.'
'3 times. 3 times. 3 times. '
```



### 3.2.String Methods

#### 3.2.1.`title()`

Each word begin with a capital letter.

```python
"jerry".title()
```

```
Jerry
```

#### 3.2.2.`upper()`, `lower()`

Change string into **ALL** uppercase or lowercase.

```python
"jerry".upper()
"JERRY".lower()
```

```
JERRY
jerry
```

#### 3.2.3.`count()`

Count the number of occurrences of a certen letter.

```python
"test test".count("t")
"test test".count("a")
```

```
4
0
```

#### 3.2.4.`replace()`

Make replacements in a string.

```python
"Hello I am back!".replace("backe", "here")
```

```
"Hello I am here!"
```

#### 3.2.5.`center()`

```python
txt = "DigitalBlackboard"

txt.center(50, "=") #returns a string with 50 characters with tex centered and
```

```
================DigitalBlackboard=================
```

#### 3.2.6.Others

| **Method**     | **Description**                                              |
| -------------- | ------------------------------------------------------------ |
| `capitalize()` | Converts **ONLY** the first letter to upper case.            |
| `startswith()` | Returns true if string starts with a specified letter.       |
| `endswith()`   | Returns true if string ends with a specified letter.         |
| `find()`       | Searches for a specified letter and returns the first position of where it is found. |
| `isalnum()`    | Returns `True` if all characters are alphanumeric.           |
| `isalpha()`    | Returns `True` if all characters are alphabets.              |
| `islower()`    | Returns `True` if all characters are lower case.             |
| `isupper()`    | Returns `True` if all characters are upper case.             |



### 3.3.Mixing Strings

#### 3.3.1.*f*-string

```python
year = 2022
event = "Election"
f"Results of the {year} {event}"
```

```
'Results of the 2022 Election'
```

##### Mutiline *f*-strings

```python
name = "Julia"
age = "28"
country = "Singapore"
message = (
    f"Her name is {name}. "
    f"Her age is {age} and "
    f"she lives in {country}."
)
message
```

```
'Her name is Julia. Her age is 28 and she lives in Singapore.'
```



### 3.4.Indexing and Slicing

#### 3.4.1.Sizing

```python
s="This is London"
len(s) #including spaces
```

```
14
```

#### 3.4.2.Indexing

```python
country = "Singapore"
country[0]
country[-3]
```

```
S
o
```

#### 3.4.3.Slicing

> The start index is included while the stop index is not.

| **Parameter** | **Description**                                              |
| ------------- | ------------------------------------------------------------ |
| `start`       | Optional (default=0). An integer number specifying at which position to start the slicing. |
| `stop`        | An integer number specifying at which position to end the slicing. |
| `step`        | Optional (default=1). An integer number specifying the step of the slicing. |

Concept Example:

| Index          | 0    | 1    | 2    | 3    | 4    | 5    | 6    | 7    | 8    |
| -------------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| Negative Index | -9   | -8   | -7   | -6   | -5   | -4   | -3   | -2   | -1   |
| Character      | S    | i    | n    | g    | a    | p    | o    | r    | e    |

##### Specified End points

```python
country[1:4]
```

```
'ing'
```

##### Negative Slicing

```python
country[-4:-1]
```

```
'por'
```

##### Step

```python
country[::2]
country[::-1]
country[-2:-5:-1]
```

```
'Snaoe'
'eropagniS'
'rop'
```

##### Chain Indexing

```python
country[:5][2:]
```

```
'nga'
```

[Top](#Data Types)



## 4.Booleans

> **Note**: Booleans are considered a ***numeric type*** in Python. `True` has a value of 1 and `False` has a value of 0.

### 4.1.False Objects

```python
bool(None)
bool(False)
bool(0)
bool("") #all False
```



### 4.2.Comparison Operators

| Operator | Meaning                  | Description                                                  |
| -------- | ------------------------ | ------------------------------------------------------------ |
| `==`     | Equal to                 | results in `True` if the 2 operands are equal and `False` if unequal. |
| `!=`     | Not equal to             | results in `True` if the 2 operands are unequal and `False` if equal. |
| `<`      | Less than                | results in `True` if the first operand is smaller than the second, else a `False`. |
| `>`      | Greater than             | results in `True` if the first operand is greater than the second, else a `False`. |
| `<=`     | Less than or equal to    | results in `True` if the first operand is lesser than or equal to the second, else a `False`. |
| `>=`     | Greater than or equal to | results in `True` if the first operand is greater than or equal to the second, else a `False`. |



### 4.3.Logical Operators

| Operator | Meaning                     | Type   | Usage     | Binary or Unary |
| -------- | --------------------------- | ------ | --------- | --------------- |
| `and`    | `True` if both `True`       | Binary | x `and` y | Binary(雙邊)    |
| `or`     | `True` if at least 1 `True` | Binary | x `or` y  | Binary(雙邊)    |
| `not`    | `True` only if `False`      | Unary  | `not` x   | Unary(只要一邊) |

[Top](#Data Types)