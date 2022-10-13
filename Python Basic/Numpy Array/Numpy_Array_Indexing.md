# 2.Array Indexing

[TOC]

> To access an array element. Start with *0*.

## 2.1.`numpy.random.choice()`

> Easy way to generates a random sample.

```python
numpy.random.choice(a, size=None, replace=True, p=None)
```

| Parameter | Required? | Default Value | Description                                                  |
| :-------: | :-------: | :-----------: | ------------------------------------------------------------ |
|    `a`    |   ✔️ Yes   |      NA       | If an `ndarray`, a random sample is generated from its elements. If an `int`, the random sample is generated as if it were `numpy.arange(a)`. |
|  `size`   |   ❌ No    |    `None`     | Output shape. If the given shape is, e.g., `(m, n, k)`, then `m*n*k` samples are drawn. Default is `None`, in which case a single value is returned. |
| `replace` |   ❌ No    |    `True`     | `True` means sample is drawn with replacement. `False`means without replacement. |
|    `p`    |   ❌ No    |    `None`     | The probabilities associated with each entry in `a`. If not given, the sample assumes a uniform distribution over all entries in `a`. |

*E.g.1*

```python
import numpy as np
R = np.random.RandomState(32) #set a random seed

a1 = R.choice(10, size=10, replace=False)
print(a1)
```

```bash
[9 1 2 8 3 0 4 6 5 7]
```

*E.g.2*

```python
a2 = R.choice(3 * 4, size=(3, 4), replace=False)
print(a2)
```

```bash
[[ 8 10  0  2]
 [ 6  7  1 11]
 [ 4  9  5  3]]
```

*E.g.3*

```python
a3 = R.choice(3 * 4 * 5, size=(3, 4, 5), replace=False)
print(a3)
```

```bash
[[[21  8  7 25  1]
  [53 31 23 44 12]
  [ 3 54 37 51 42]
  [45 14 22 27 34]]

 [[28 57 52 40 17]
  [32  9  2 59 39]
  [33 15 46 43 24]
  [35 58 19 16 41]]

 [[ 4 30  6 49  0]
  [48 47 29 26 56]
  [11 13 38  5 55]
  [36 50 20 10 18]]]
```



## 2.2 1-D array

| Positive Index | 0    | 1    | 2    | 3    | 4    | 5    | 6    | 7    | 8    | 9    |
| -------------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| Element        | 9    | 1    | 2    | 8    | 3    | 0    | 4    | 6    | 5    | 7    |

```python
print(a1[3])
print(a1[-5])
```

```bash
8
0
```



## 2.3 2-D array

$$
\mathbf{a_2} = 
\begin{bmatrix}
  8   &  10  &  0   &  2   \\
  6   &  7   &  1   &  11  \\
  4   &  9   &  5   &  3   \\
\end{bmatrix}
$$

```python
print(a2[-2, 3])
```

```bash
11
```



## 2.4 3-D array

$$
a_3 = \begin{pmatrix}
Frame_0 = 
\begin{bmatrix}
21 & 8  & 7  & 25 & 1  \\
53 & 31 & 23 & 44 & 12 \\
3  & 54 & 37 & 51 & 42 \\
45 & 14 & 22 & 27 & 34
\end{bmatrix},\\
Frame_1 = 
\begin{bmatrix}
28 & 57 & 52 & 40 & 17 \\
32 & 9  & 2  & 59 & 39 \\
33 & 15 & 46 & 43 & 24 \\
35 & 58 & 19 & 16 & 41
\end{bmatrix},\\
Frame_2 = 
\begin{bmatrix}
4  & 30 & 6  & 49 & 0  \\
48 & 47 & 29 & 26 & 56 \\
11 & 13 & 38 & 5  & 55 \\
36 & 50 & 20 & 10 & 18
\end{bmatrix}
\end{pmatrix}
$$

```python
print(a3[2, 3, 1])
```

```bash
50
```







[Back to Intro](Numpy_Array_Intro.md)