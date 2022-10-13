# 5.Array Reshaping

[TOC]

> Reshaping an array.

## 5.1.Reshaping Examples

*E.g.1* **1-D**

```python
import numpy as np

a = np.arange(1, 13)
print(a)
b = a.reshape(4, 3) #1D>>2D
print(b)
```

```bash
[ 1  2  3  4  5  6  7  8  9 10 11 12]

[[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]]
```

*E.g.2* **2-D**, **3-D**

```python
c = b.reshape(2, 6)
print(c)
d = c.reshape(6, 2)
print(d)
e = d.reshape(2, 3, 2) #2D>>3D
print(e)
```

```bash
[[ 1  2  3  4  5  6]
 [ 7  8  9 10 11 12]]

[[ 1  2]
 [ 3  4]
 [ 5  6]
 [ 7  8]
 [ 9 10]
 [11 12]]

[[[ 1  2]
  [ 3  4]
  [ 5  6]]

 [[ 7  8]
  [ 9 10]
  [11 12]]]
```



## 5.2.Attribute: Base

> Reshape returns a ***view***.

```python
a = np.arange(1, 13)
b = a.reshape(4, 3)
c = b.reshape(2, 6)

print(b.base) #come from original section
print(c.base) #come from original section too

print(b.base is a)
```

```bash
[ 1  2  3  4  5  6  7  8  9 10 11 12]
[ 1  2  3  4  5  6  7  8  9 10 11 12]

True
```

### 5.2.1.Verifiy

```python
b[0, 0] = 99
print(a)
print(b)
print(c)
```

```bash
[99  2  3  4  5  6  7  8  9 10 11 12]

[[99  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]]

[[99  2  3  4  5  6]
 [ 7  8  9 10 11 12]]
```



## 5.3.Method: numpy.newaxis()

> Typycally using newaxis to add new dimension.

```python
x = np.arange(1, 5) # 1-D array
print(x)
x_row = x[np.newaxis, :] # row matrix
print(x_row)
x_col = x[:, np.newaxis] # column matrix
print(x_col)
```

```bash
[1 2 3 4]

[[1 2 3 4]]

[[1]
 [2]
 [3]
 [4]]
```

### 5.3.1.Reshape works as well

```python
x_row = x.reshape((1, 4)) #row matrix
x_col = x.reshape((4, 1)) #column matrix
```



## 5.4.Find Dimension Automatically

> Calculate the missing dimension given any other dimensions.

```python
x2 = x.reshape(2, 2, -1)
print(x2.shape)
print(x2)
```

```bash
(2, 2, 3)

[[[ 1  2  3]
  [ 4  5  6]]

 [[ 7  8  9]
  [10 11 12]]]
```



## 5.5.Flattening an Array

```python
print(x2)#3-D array
print(x2.reshape(-1)) #flattened array
```

```bash
[[[ 1  2  3]
  [ 4  5  6]]

 [[ 7  8  9]
  [10 11 12]]]

[ 1  2  3  4  5  6  7  8  9 10 11 12]
```







[Back to Intro](Numpy_Array_Intro.md)
