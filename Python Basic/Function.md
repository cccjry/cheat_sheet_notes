# Functions

[TOC]

## Defining a Function

```python
def function_name(parameters):
	statement(s)
    return value1, value2, ...
```





## `sorted()` Function

```python
sorted(iterable, key=None, reverse=False)
```

| Parameter  | Required? | Default Value | Description                                                  |
| ---------- | :-------: | :-----------: | ------------------------------------------------------------ |
| `iterable` |   ✔️ Yes   |      NA       | An ordered sequence (string, tuple, list) or an unordered collection (set, dictionary) or any other iterator. |
| `key`      |   ❌ No    |    `None`     | A function that serves as a key for the sort comparison.     |
| `reverse`  |   ❌ No    |    `False`    | If `True`, the sorted list is reversed (sorted in descending order). |

### Example

```python
import random as rd
list1 = rd.sample(range(1,21),20)
print(f'Original random list: {list1}.')

def sum_of_digits(x):			#把數字加起來 E.g. 12 >> 1+2=3
    return sum([int(a) for a in str(x)])

print(f"Sorted according to sum of digits : {sorted(list1, key = sum_of_digits)}.")
```

```
Original random list: [14, 6, 16, 20, 12, 18, 8, 17, 7, 15, 19, 5, 3, 13, 4, 10, 2, 11, 1, 9].
Sorted according to sum of digits : [10, 1, 20, 2, 11, 12, 3, 13, 4, 14, 5, 6, 15, 16, 7, 8, 17, 18, 9, 19].
```





## `Lambda`

> By given a function in a single line.

```python
lambda arg1, arg2, ...: return_value
```

### Example

```python
import random as rd
list1 = rd.sample(range(1,21),20)
print(f'Original random list: {list1}.')

print(list1) # random integers (generated above).
print(sorted(list1, key = lambda x: sum([int(a) for a in str(x)])))
```

```
Original random list: [14, 6, 16, 20, 12, 18, 8, 17, 7, 15, 19, 5, 3, 13, 4, 10, 2, 11, 1, 9].
[10, 1, 20, 2, 11, 12, 3, 13, 4, 14, 5, 6, 15, 16, 7, 8, 17, 18, 9, 19]
```





## Namespaces

A **namespace** is a ***collection of currently defined variable names along with information about the object that each name references***. A namespace is a mapping from names to objects. We can think of a namespace as a dictionary in which the keys are the object names and the values are the objects themselves.

### Global versus Local

#### Global

```python
def func(x): #parameter x is a local variable
    global b #this b is a global variable
    b = 10   #global b is now set to 10
    a = b + x
    return a

b = 2
print(func(b))
print(b)
```

```
12
10
```

#### Local

```python
def func(x):
    b = 10
    a = b + x #b refers to the local b, not the global b
    return a

b = 2
print(func(b))
print(b)
```

```
12
2
```

> **Caution**: Accessing global variables from within functions should be avoided as much as possible. Passing values via parameters and returning values is usually preferable because it keeps different parts of the code as **independent** of each other as possible.









[Top](#Functions)