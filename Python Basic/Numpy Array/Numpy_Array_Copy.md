# 4.Array Copy versus Views

[TOC]

## 4.1.Differences

|   Object    | Subarray | Difference (Copy vs View)                                    |
| :---------: | :------: | ------------------------------------------------------------ |
| Python List |   Copy   | 不會改變原本的陣列。Changes to subarray will not modify array. |
| NumPy Array |   View   | 會改變原本的陣列。Changes to subarray will modify array.     |



## 4.2.Python List Slices Return Copies

```python
import random
random.seed(10)
a1 = random.sample(range(10), 10) #[9, 0, 6, 3, 4, 8, 1, 7, 2, 5]
a1_slice = a1[1:4] #[0, 6, 3]

a1_slice[0] = 99
print(a1_slice)
print(a1)
```

```bash
[99, 6, 3]
[9, 0, 6, 3, 4, 8, 1, 7, 2, 5]
```



## 4.3.NumPy Array Slices Return Views

```python
a2 = np.array(a1) #[9, 0, 6, 3, 4, 8, 1, 7, 2, 5]
a2_slice = a2[1:4] #[0, 6, 3]

a2_slice[0] = 99
print(a2_slice)
print(a2)
```

```bash
[99  6  3]
[ 9 99  6  3  4  8  1  7  2  5]
```



## 4.4.Creating Copies of Numpy Array

```python
a2 = np.array(a1) #[9 0 6 3 4 8 1 7 2 5]
a2_subcopy = a2[1:4].copy() #[0 6 3]

a2_subcopy[0] = 99
print(a2_subcopy)
print(a2)
```

```bash
[99  6  3]
[9 0 6 3 4 8 1 7 2 5]
```





[Back to Intro](Numpy_Array_Intro.md)
