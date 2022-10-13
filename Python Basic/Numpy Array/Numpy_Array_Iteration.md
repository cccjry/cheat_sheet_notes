# 6.Array Iteration

[TOC]

> Looping within array to speed up process.

## 6.1.Introduction

```python
import numpy as np
R = np.random.RandomState(18) #set a random seed
arr = R.choice(10, size=10, replace=False)
arr2 = R.choice(12, size=(3, 4), replace=False)
arr3 = R.choice(12, size=(2, 3, 2), replace=False)
```

```bash
[7 9 0 4 2 1 6 5 8 3]	#arr

[[ 3  4 10  0]				#arr2
 [ 8 11  6  7]
 [ 9  5  1  2]]

[[[11  2]							#arr3
  [ 0  6]
  [ 9  5]]
 [[ 8  3]
  [ 1 10]
  [ 4  7]]]
```

### 6.1.1.for-loop

> Easiest way

### 6.1.2.enumerate

> Provides index & element together (index, element)

### 6.1.3.`numpy.ndenumerate()`*

> Numpy build-in function.



## 6.2.Examples

### 6.2.1 1-D

```python
for (i, x) in np.ndenumerate(arr):
    print(i, x)
```

```bash
(0,) 7
(1,) 9
(2,) 0
(3,) 4
(4,) 2
(5,) 1
(6,) 6
(7,) 5
(8,) 8
(9,) 3
```



### 6.2.2 2-D

```python
for (i, x) in np.ndenumerate(arr2):
    print(i, x)
```

```bash
(0, 0) 3
(0, 1) 4
(0, 2) 10
(0, 3) 0
(1, 0) 8
(1, 1) 11
(1, 2) 6
(1, 3) 7
(2, 0) 9
(2, 1) 5
(2, 2) 1
(2, 3) 2
```



### 6.2.3 3-D

```python
for (i, x) in np.ndenumerate(arr3):
    print(i, x)
```

```bash
(0, 0, 0) 11
(0, 0, 1) 2
(0, 1, 0) 0
(0, 1, 1) 6
(0, 2, 0) 9
(0, 2, 1) 5
(1, 0, 0) 8
(1, 0, 1) 3
(1, 1, 0) 1
(1, 1, 1) 10
(1, 2, 0) 4
(1, 2, 1) 7
```









[Back to Intro](Numpy_Array_Intro.md)
