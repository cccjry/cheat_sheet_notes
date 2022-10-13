# 9.Array Sorting

[TOC]

> Rearranging elements.

```python
import numpy as np

R = np.random.RandomState(17) #set a random seed
a1 = R.choice(10, size=15, replace=True) # 1-D random array
a2 = R.choice(10, size=(4, 5), replace=True) # 2-D random array
```

```
[1 6 6 9 0 6 4 7 4 7 1 1 9 8 2]	#a1

[[3 6 6 9 9]										#a2
 [1 5 1 0 5]
 [6 6 2 6 9]
 [8 3 2 1 9]]
```



## 9.1.`numpy.sort()`

```python
numpy.sort(a, axis=-1, kind=None, order=None)
```

| Parameter | Required? | Default Value | Description                                                  |
| :-------: | :-------: | :-----------: | ------------------------------------------------------------ |
|    `a`    |   ✔️ Yes   |      NA       | Array to be sorted.                                          |
|  `axis`   |   ❌ No    |     `-1`      | Axis along which to sort. If `None`, the array is flattened before sorting. The default is `-1`, which **sorts along the last axis**. |
|  `kind`   |   ❌ No    |    `None`     | Sorting algorithm. The default is ‘quicksort’. Options:**{‘*quicksort*’, ‘mergesort’, ‘heapsort’, ‘stable’}** |
|  `order`  |   ❌ No    |    `None`     | When `a` is an array with fields defined, this argument specifies which fields to compare first, second, etc. |

> Returns a ***copy***.



### 9.1.1 1-D

#### Ascending

```python
print(np.sort(a1))
```

```
[0, 1, 1, 1, 2, 4, 4, 6, 6, 6, 7, 7, 8, 9, 9]
```

#### Descending

```python
-np.sort(-a1)
np.sort(a1)[::-1]
```

```
[9, 9, 8, 7, 7, 6, 6, 6, 4, 4, 2, 1, 1, 1, 0] #results are equivalent
```

### 9.1.2 2-D

#### Ascending

```python
print(np.sort(a2)) #np.sort(a2, axis=1)
```

```
[[3, 6, 6, 9, 9],
 [0, 1, 1, 5, 5],
 [2, 6, 6, 6, 9],
 [1, 2, 3, 8, 9]]
```

#### Descending

```python
-np.sort(-a2)
np.sort(a2)[:,::-1]
```

```
array([[9, 9, 6, 6, 3],
       [5, 5, 1, 1, 0],
       [9, 6, 6, 6, 2],
       [9, 8, 3, 2, 1]]) #results are equivalent
```

**Note**: The rows or columns are sorted **independently**. This also applies to sorting of arrays of higher dimensions.



## 9.2.`numpy.ndarray.sort()`

> Sort in-place. That is, **the parents are sorted**.

```python
a1.sort()
a2.sort(axis=0)

print(a1)
print(a2)
```

```
[0 1 1 1 2 4 4 6 6 6 7 7 8 9 9]

[[1 3 1 0 5]
 [3 5 2 1 9]
 [6 6 2 6 9]
 [8 6 6 9 9]]
```



## 9.3.`numpy.argsort()`

> Gives you **sorted indices**.

```python
numpy.argsort(a, axis=-1, kind=None, order=None)
```

| Parameter | Required? | Default Value | Description                                                  |
| :-------: | :-------: | :-----------: | ------------------------------------------------------------ |
|    `a`    |   ✔️ Yes   |      NA       | Array to be sorted.                                          |
|  `axis`   |   ❌ No    |     `-1`      | Axis along which to sort. If `None`, the array is flattened before sorting. The default is `-1`, which sorts along the last axis. |
|  `kind`   |   ❌ No    |    `None`     | Sorting algorithm. The default is ‘quicksort’.               |
|  `order`  |   ❌ No    |    `None`     | When `a` is an array with fields defined, this argument specifies which fields to compare first, second, etc. |



```python
ind = a2[-1, :].argsort()
print(ind)
print(a2[ind]) #sorted by indices
```

```
[3 2 1 0 4]

[[9 6 6 3 9]
 [0 1 5 1 5]
 [6 2 6 6 9]
 [1 2 3 8 9]]
```









[Back to Intro](Numpy_Array_Intro.md)