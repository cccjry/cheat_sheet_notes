# 3.While Loops

[TOC]

## 3.1.The `while` Statement

The `while` loop in Python is used to iterate over a block of code as long as the test expression is `True`. We typically use the `while` loop when we don’t know the number of times to iterate beforehand. `while` loops can also have an optional `else` block. The `else` code block is executed if the `test expression` of the `while` loop evaluates to `False` (i.e. end of the loop).

```python
while test_expression:
    statement(s)
```

### Example1

```python
i = 1		#counter variable
while i <= 10:
    print(i**2)
    i += 1
```

```
1
4
9
16
25
36
49
64
81
100
```

> **Note**: often used in conjunction with a **counter variable** to keep track of the iteration number

### Example2(with else)

```python
ind = 0
word = "excellent"

while ind < len(word):
    print(f"Letter '{word[ind]}' is found at index {ind}")
    ind+= 1
else:
    print(f"End of Loop with a total of {ind} letters")
```

```
Letter "e" is found at index 0
Letter "x" is found at index 1
Letter "c" is found at index 2
Letter "e" is found at index 3
Letter "l" is found at index 4
Letter "l" is found at index 5
Letter "e" is found at index 6
Letter "n" is found at index 7
Letter "t" is found at index 8
End of Loop with a total of 9 letters
```





## 3.2.The `break` Statement

> The `break` statement **terminates the loop** containing it.

### 3.2.1.`break` in `for`-loop

#### Example1

```python
ind = 0
word = "terrible"
target = "r"

for letter in word:
    if letter == target:
        print(f"The letter {target} is found at index {ind}")
        break
    ind+= 1
else:
    print(f"Letter {target} not found.")
```

```
The letter r is found at index 2
```

#### Example2

```python
lower = 2
upper = 50

for num in range(lower, upper):
    for i in range(2, num):
        if (num % i) == 0:
            break
    else:
        print(num)
```

```
2
3
5
7
11
13
17
19
23
29
31
37
41
43
47
```

### 3.2.2.`break` in `while`-loop

```python
ind = 0
word = "excellent"
target = "n"

while ind < len(word):
    if word[ind] == target:
        print(f"The letter {target} is found at index {ind}")
        break
    ind+= 1
else:
    print(f"Letter {target} not found.")
```

```
The letter n is found at index 7
```

> **Note**: The `else` block of a `while` loop **will only be executed** if no `break` occurs and the test condition turns `False`.





## 3.3.The `continue` Statement

```python
ind = 0
word = "extraterrestrial"
target = "t"

for (ind, letter) in enumerate(word):
    if letter != target:
        continue
    else:
        print(f"Letter '{target}' is found at index {ind}")

```

```
Letter "t" is found at index 2
Letter "t" is found at index 5
Letter "t" is found at index 11
```







[Top](#3.While Loops)

[Back to Contents](Flow_README.md)