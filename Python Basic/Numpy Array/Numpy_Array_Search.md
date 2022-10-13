# 10.Array Search

[TOC]

> Find what you want inside an array.

```python
import numpy as np
R = np.random.RandomState(17) #set a random seed
a1 = R.choice(10, size=15, replace=True) # 1-D random array
a2 = R.choice(10, size=(4, 5), replace=True) # 2-D random array
```

```
[1 6 6 9 0 6 4 7 4 7 1 1 9 8 2]

[[3 6 6 9 9]
 [1 5 1 0 5]
 [6 6 2 6 9]
 [8 3 2 1 9]]
```



## 10.1.`numpy.extract()`

> Extract **elements** out.

```python
numpy.extract(condition, arr)
```

|  Parameter  | Required? | Default Value | Description                                                  |
| :---------: | :-------: | :-----------: | ------------------------------------------------------------ |
| `condition` |   ✔️ Yes   |      NA       | An array whose nonzero or `True` entries indicate the elements of `arr` to extract. |
|    `arr`    |   ✔️ Yes   |      NA       | Input array of the same size as `condition`.                 |

```python
np.extract(a1 > 6, a1)
```

```
array([9, 7, 7, 9, 8])
```

Easily using `len(np.extract(a1 > 6, a1))` to find out how many elements inside.



## 10.2.`numpy.where()`

> Extract **indices of elements** out.

```python
numpy.where(condition, x=None, y=None)
```

|  Parameter  | Required? | Default Value | Description                                                  |
| :---------: | :-------: | :-----------: | ------------------------------------------------------------ |
| `condition` |   ✔️ Yes   |      NA       | Where `True`, yield `x`, otherwise yield `y`.                |
|   `x, y`    |   ❌ No    |    `None`     | Values from which to choose. `x`, `y` and `condition` need to be broadcastable to some shape. Return `x` if `condition` is `True`and `y` if `condition` is `False`. |

```python
print(np.where(a1 > 6))

for (index, value) in zip(np.where(a1 > 6)[0], np.extract(a1 > 6, a1)):
    print(f'{index}: {value}')

print(np.where(a1%2==0, 1, 0))
```

```
(array([ 3,  7,  9, 12, 13], dtype=int64), )

3: 9
7: 7
9: 7
12: 9
13: 8

[0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1]
```



## 10.3.`numpy.insert()`

```python
numpy.insert(arr, obj, values, axis=None)
```

| Parameter | Required? | Default Value | Description                                                  |
| :-------: | :-------: | :-----------: | ------------------------------------------------------------ |
|   `arr`   |   ✔️ Yes   |      NA       | Input array.                                                 |
|   `obj`   |   ✔️ Yes   |      NA       | Object that defines the index or indices before which `values` is inserted. |
| `values`  |   ✔️ Yes   |      NA       | Values to insert into `arr`. In addition, `values` should be shaped so that `arr`[…,`obj`,…] = `values` is legal. |
|  `axis`   |   ❌ No    |    `None`     | Axis along which to insert `values`. If axis is `None` then `arr` is flattened first. |

### 10.3.1 1-D

```python
ar = np.arange(10)
ins = [3, 5, 7]
val = [91, 92, 93]
print(ar)
print(np.insert(ar, ins, val))
```

```
[0 1 2 3 4 5 6 7 8 9]
[ 0  1  2 91  3  4 92  5  6 93  7  8  9]
```

### 10.3.2 2-D

```python
ins = [1, 3]
val = [91, 92]
print(np.insert(a2, ins, val, axis=1))
```

```
[[ 3 91  6  6 92  9  9]
 [ 1 91  5  1 92  0  5]
 [ 6 91  6  2 92  6  9]
 [ 8 91  3  2 92  1  9]]
```

**Caution**: Array `values` should be shaped so that `arr`[...,`obj`,...] = `values` is legal.

```python
ins = [1, 3]
val = [91, 92]
print(np.insert(a2, ins, val, axis=0))
```

```
ValueError: shape mismatch: value array of shape (2,) could not be broadcast to indexing result of shape (2,5)
```

**Note**: 若要從 `row` 方向插入，`values` 的 `shape[1]` 必須符合原始陣列的 `shape[1]`。E.g. `[91, 91, 91, 91, 91]`



## 10.4.`numpy.searchsorted()`

> Returns the **indices of insetion**.

```python
numpy.searchsorted(a, v, side='left', sorter=None)
```

| Parameter | Required? | Default Value | Description                                                  |
| :-------: | :-------: | :-----------: | ------------------------------------------------------------ |
|    `a`    |   ✔️ Yes   |      NA       | Input array. If sorter is `None`, then it must be sorted in *ascending*order, otherwise sorter must be an array of indices that sort it. |
|    `v`    |   ✔️ Yes   |      NA       | Values to be inserted into `a`.                              |
|  `side`   |   ❌ No    |   `'left'`    | If `'left'`, the index of the first suitable location found is given. If `'right'`, return the last such index. If there is no suitable index, return either 0 or N (where N is the length of `a`). |
| `sorter`  |   ❌ No    |    `None`     | Optional array of integer indices that sort array a into ascending order. They are typically the result of [`argsort`](Numpy_Array_Sort.md#9.3.numpy.argsort()). |

### 10.4.1.When input array is sorted:

```python
ar = np.arange(10)
val = [3, 5, 20]
ins = np.searchsorted(ar , val)
print(ins)
```

```
array([ 3,  5, 10], dtype=int64) #回傳"值"被插在哪個位置
```

### 10.4.2.When input array is NOT sorted:

```python
#Using a1 as an example
ind = a1.argsort() #first to get indices for sorting
inss = np.searchsorted(a1 , val, sorter=ind) #using `sorter` argument
print(f'Insertion indices: {inss}')
```

```
Insertion indices: [ 5  7 15]
```







[Back to Intro](Numpy_Array_Intro.md)