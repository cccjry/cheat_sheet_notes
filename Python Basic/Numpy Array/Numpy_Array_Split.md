# 8.Array Splitting

[TOC]

> Opposite of concatenation.

## 8.1.`numpy.split()`

```python
numpy.split(ary, indices_or_sections, axis=0)
```

|       Parameter       | Required? | Default Value | Description                                                  |
| :-------------------: | :-------: | :-----------: | ------------------------------------------------------------ |
|         `ary`         |   ✔️ Yes   |      NA       | Array to be divided into sub-arrays.                         |
| `indices_or_sections` |   ✔️ Yes   |      NA       | If `indices_or_sections` is an integer, N, the array will be divided into N equal arrays along axis. If such a split is not possible, an error is raised. If `indices_or_sections` is a 1-D array of sorted integers, the entries indicate where along axis the array is split. |
|        `axis`         |   ❌ No    |       0       | The axis along which to split. (0, 1, 2)=(frame, row, col)   |





| `indices_or_sections` |                         Description                         | Example |             Output             |
| :-------------------: | :---------------------------------------------------------: | :-----: | :----------------------------: |
|      `sections`       |            An integer N.可整除、均分陣列的`size`            |   `2`   |      `ary[:5]`,`ary[5:]`       |
|       `indices`       | A 1-D array of sorted integers.依照給定的位置切分原本的陣列 | `[2,3]` | `ary[:2]`,`ary[2:3]`,`ary[3:]` |

------



```python
import numpy as np
R = np.random.RandomState(19) #set a random seed
a1 = R.choice(10, size=10, replace=False) #array of random integers
a2 = R.choice(3 * 4, size=(3, 4), replace=False)
a21 = R.choice(3 * 4, size=(3, 4), replace=False) #2-D random array
a3 = np.stack((a2, a21), axis=0) #concatenation
```

```
[1 7 9 6 8 4 3 0 2 5] #a1

[[ 7  1  9 11]				#a2
 [ 0  6 10  4]
 [ 3  8  2  5]]

[[ 8  7  9  5]				#a21
 [ 3 11  0  4]
 [ 2  6 10  1]]

[[[ 7  1  9 11]				#a3
  [ 0  6 10  4]
  [ 3  8  2  5]]

 [[ 8  7  9  5]
  [ 3 11  0  4]
  [ 2  6 10  1]]]
```

### 8.1.1 1-D Splitting

#### *sections*

```python
print(np.split(a1, 2))
```

```
[array([1, 7, 9, 6, 8]), array([4, 3, 0, 2, 5])]
```

#### *indices*

```python
x1, x2, x3 = np.split(a1, [2, 6])
print(x1, x2, x3)
```

```
[1 7] [9 6 8 4] [3 0 2 5]
```

**Note**: *N* split points lead to *N*+1 sub-arrays.



> Split results are ***views*** of original parent. So any change will affect original parent.

```python
x2[0]=99
print(a1)
```

```
[ 1  7 99  6  8  4  3  0  2  5]
```

### 8.1.2 2-D Splitting

```python
y1, y2 = np.split(a2, 2, axis=1)
print(y1)
print(y2)

z1, z2 = np.split(a2, [1], axis=0)
print(z1)
print(z2)
```

```
[[7 1]					#y1
 [0 6]
 [3 8]]

[[ 9 11]				#y2
 [10  4]
 [ 2  5]]

[[ 7  1  9 11]]	#z1.shape=(1, 4)

[[ 0  6 10  4]	#z2.shape=(2, 4)
 [ 3  8  2  5]]
```

**Caution**: The split points need to be specified as a **sorted array**.

### 8.1.3 3-D Splitting

```python
d1, d2 = np.split(a3, 2, axis=2)
```

```
[[[ 7  1]			#d1.shape=(2, 3, 2)
  [ 0  6]
  [ 3  8]]

 [[ 8  7]
  [ 3 11]
  [ 2  6]]]

[[[ 9 11]			#d2.shape=(2, 3, 2)
  [10  4]
  [ 2  5]]

 [[ 9  5]
  [ 0  4]
  [10  1]]]
```



## 8.2.`numpy.array_split()`

> `numpy.array_split` is identical to `numpy.split` except that `numpy.array_split` allows `indices_or_sections` to be an integer that **does not equally divide the axis**.

In other words, the size of the dimension along where splitting occurs does not need to be divisible by the `indices_or_sections` parameter. For an array of length `l` that is to be split into `N` sections, it returns `l%N` sub-arrays of size `l//n + 1` and the rest of size `l//N`.

```python
print(np.array_split(a1, 3))
```

```
[array([1, 7, 9, 6]), array([8, 4, 3]), array([0, 2, 5])]
```



## 8.3.`numpy.hsplit()`

> Equivalent to `numpy.split` with `axis=1`

```python
numpy.hsplit(ary, indices_or_sections)
```

|       Parameter       | Required? | Default Value | Description                                                  |
| :-------------------: | :-------: | :-----------: | ------------------------------------------------------------ |
|         `ary`         |   ✔️ Yes   |      NA       | Array to be divided into sub-arrays.                         |
| `indices_or_sections` |   ✔️ Yes   |      NA       | If `indices_or_sections` is an integer, N, the array will be divided into N equal arrays along axis. If such a split is not possible, an error is raised. If `indices_or_sections` is a 1-D array of sorted integers, the entries indicate where along axis the array is split. |

```python
b1, b2 = np.hsplit(a1, 2)
print(b1, b2)

c1, c2, c3 = np.hsplit(a2, [1,3])
print(c1, c2, c3, sep="\n")
```

```
[1 7 9 6 8] [4 3 0 2 5]

[[7]
 [0]
 [3]]

[[ 1  9]
 [ 6 10]
 [ 8  2]]

[[11]
 [ 4]
 [ 5]]
```



## 8.4.`numpy.vsplit()`

> Equivalent to `numpy.split` with `axis=0`

```python
numpy.vsplit(ary, indices_or_sections)
```

|       Parameter       | Required? | Default Value | Description                                                  |
| :-------------------: | :-------: | :-----------: | ------------------------------------------------------------ |
|         `ary`         |   ✔️ Yes   |      NA       | Array to be divided into sub-arrays.                         |
| `indices_or_sections` |   ✔️ Yes   |      NA       | If `indices_or_sections` is an integer, N, the array will be divided into N equal arrays along axis. If such a split is not possible, an error is raised. If `indices_or_sections` is a 1-D array of sorted integers, the entries indicate where along axis the array is split. |

```python
d1, d2, d3 = np.vsplit(a2, [1,2])
print(d1, d2, d3, sep='\n')

e1, e2 = np.vsplit(a3, [1]) # split along axis=0
print(e1, e2, sep='\n')
```

```
[[ 7  1  9 11]]	#d1
[[ 0  6 10  4]]	#d2
[[3 8 2 5]]			#d3


[[[ 7  1  9 11]		#e1
  [ 0  6 10  4]
  [ 3  8  2  5]]]
[[[ 8  7  9  5]		#e2
  [ 3 11  0  4]
  [ 2  6 10  1]]]
```





[Back to Intro](Numpy_Array_Intro.md)