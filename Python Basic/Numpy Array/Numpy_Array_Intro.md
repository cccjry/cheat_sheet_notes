# Numpy Array Introduction

## Contents

[1.Basic](#Basic)

[2.Indexing](Numpy_Array_Indexing.md)

[3.Slicing](Numpy_Array_Slicing.md)

[4.Copy](Numpy_Array_Copy.md)

[5.Reshape](Numpy_Array_Reshaping.md)

[6.Iteration](Numpy_Array_Iteration.md)

[7.Concatenate](Numpy_Array_Concat.md)

[8.Split](Numpy_Array_Split.md)

[9.Sort](Numpy_Array_Sort.md)

[10.Search](Numpy_Array_Search.md)





## Reference

1. [Digital Black Board](https://digitalblackboard.online/python/numpyarrays/)



## 1.Basic

### 1.1`numpy.array()`

- same data type (auto-upcast if possible會自動轉換成相同數項)

  *E.g.*

  Input:

  ```python
  np.array([2.4, 3, 2])
  ```

  Output:

  ```bash
  array([2.4, 3. , 2. ])
  ```

- specify data type

  - Booleans
  - Integers
  - Unsigned integers
  - Floats
  - Complex numbers

  | Category              | Data Type    | Description                                                  |
  | --------------------- | ------------ | ------------------------------------------------------------ |
  | **Strings**           | `str_`       | Unicode string                                               |
  | **Boolean**           | `bool_`      | Boolean (`True` or `False`) stored as a byte                 |
  | **Integers**          | `int_`       | Default integer type (same as C `long`; normally `int32`)    |
  |                       | `intc`       | Identical to C `int` (normally `int32` or `int64`)           |
  |                       | `intp`       | Integer used for indexing; identical to C `ssize_t` (normally `int32` or `int64`) |
  |                       | `int8`       | Integer (–128 to 127)                                        |
  |                       | `int16`      | Integer (–32768 to 32767)                                    |
  |                       | `int32`      | Integer (–2147483648 to 2147483647)                          |
  |                       | `int64`      | Integer (–9223372036854775808 to 9223372036854775807)        |
  | **Unsigned Integers** | `uint8`      | Unsigned integer (0 to 255)                                  |
  |                       | `uint16`     | Unsigned integer (0 to 65535)                                |
  |                       | `uint32`     | Unsigned integer (0 to 4294967295)                           |
  |                       | `uint64`     | Unsigned integer (0 to 18446744073709551615)                 |
  | **Floats**            | `float_`     | Shorthand for `float64`                                      |
  |                       | `float16`    | Half-precision float: sign bit, 5 bits exponent, 10 bits mantissa |
  |                       | `float32`    | Single-precision float: sign bit, 8 bits exponent, 23 bits mantissa |
  |                       | `float64`    | Double-precision float: sign bit, 11 bits exponent, 52 bits mantissa |
  | **Complex**           | `complex_`   | Shorthand for `complex128`                                   |
  |                       | `complex64`  | Complex number, represented by two 32-bit floats             |
  |                       | `complex128` | Complex number, represented by two 64-bit floats             |

  *E.g.*

  ```python
  np.array([1, 2, 3, 4], dtype=**SPECIFY DATA TYPE HERE**)
  ```

### 1.2.Create Arrays

#### 1.2.1.some useful initials

| Array Creation Routine                   | Output Array                        |
| :--------------------------------------- | :---------------------------------- |
| `np.zeros(shape, dtype=float)`           | Filled with **zeros**.              |
| `np.ones(shape, dtype=None)`             | Filled with **ones**.               |
| `np.full(shape, fill_value, dtype=None`) | Filled with a certain `fill_value`. |
| `np.empty(shape, dtype=float)`           | Entries not initialized.            |

*E.g.*

Input:

```python
np.zeros((2, 3, 4), dtype=int)
```

Output:

```bash
array([[[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]],

        [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]])
```

> **Note:** The shape of a 3-D array is specified as `(frames, rows, columns)`



#### 1.2.2.`numpy.eye()`

> 對角陣列

```python
np.eye(N, M=None, k=0, dtype=<class 'float'>)
```

| Parameter | Required? | Default Value | Description                                                  |
| :-------: | :-------: | :-----------: | ------------------------------------------------------------ |
|    `N`    |   ✔️ Yes   |      NA       | 幾個列                                                       |
|    `M`    |   ❌ No    |    `None`     | 幾個行，預設同*列數*                                         |
|    `k`    |   ❌ No    |       0       | 對角線位置(**Index of the diagonal**)：只能整數，正值(`+`)使對角線上移；負值(`-`)使對角線下移 |
|  `dtype`  |   ❌ No    |    `float`    | Data type of the returned array.                             |

*E.g.*

Input:

```python
np.eye(4, None, -2, dtype=int)
```

Output:

```bash
array([[0, 0, 0, 0],
       [0, 0, 0, 0],
       [1, 0, 0, 0],
       [0, 1, 0, 0]])
```



#### 1.2.3.`numpy.arange()`

> 有次序列

```python
numpy.arange(start=0, stop, step=1, dtype=None)
```

| Parameter | Required? | Default Value | Description                                                  |
| :-------: | :-------: | :-----------: | ------------------------------------------------------------ |
|  `start`  |   ❌ No    |       0       | Start of interval. The interval is inclusive of this value.  |
|  `stop`   |   ✔️ Yes   |      NA       | End of interval. The interval is **not incluive of this value**. |
|  `step`   |   ❌ No    |       1       | Spacing between values. For any output `out`, this is the distance between two adjacent values, `out[i+1] - out[i]`. |
|  `dtype`  |   ❌ No    |   Inferred.   | The type of the output array. If `dtype` is not given, data type is inferred from the other input arguments. |

*E.g.*

Input:

```python
np.arange(0, 1, 0.125)
```

Output:

```bash
array([0.   , 0.125, 0.25 , 0.375, 0.5  , 0.625, 0.75 , 0.875])
```



#### 1.2.4.`numpy.linspace()`

> 均勻序列

```python
numpy.linspace(start=0, stop, num=50, endpoint=True, retstep=False, dtype=None)
```

| Parameter  | Required? | Default Value | Description                                                  |
| :--------: | :-------: | :-----------: | ------------------------------------------------------------ |
|  `start`   |   ❌ No    |       0       | The starting value of the sequence.                          |
|   `stop`   |   ✔️ Yes   |      NA       | The end value of the sequence, unless endpoint is set to `False`. In that case, the sequence consists of all but the last of `num + 1` evenly spaced samples, so that `stop` is excluded. . |
|   `num`    |   ❌ No    |      50       | Number of samples to generate.                               |
| `endpoint` |   ❌ No    |    `True`     | 是否包含結束點。If `True`, `stop` is the last sample. Otherwise, it is not included. |
| `retstep`  |   ❌ No    |    `False`    | 是否輸出均勻步伐長度。If `True`, return (samples, `step`), where `step` is the spacing between samples. |
|  `dtype`   |   ❌ No    |   Inferred.   | The type of the output array. If `dtype` is not given, data type is inferred from `start` and `stop`. |

*E.g.*

Input:

```python
np.linspace(0, 10, retstep=True)
```

Output:

```bash
(array([ 0.        ,  0.20408163,  0.40816327,  0.6122449 ,  0.81632653,
        1.02040816,  1.2244898 ,  1.42857143,  1.63265306,  1.83673469,
        2.04081633,  2.24489796,  2.44897959,  2.65306122,  2.85714286,
        3.06122449,  3.26530612,  3.46938776,  3.67346939,  3.87755102,
        4.08163265,  4.28571429,  4.48979592,  4.69387755,  4.89795918,
        5.10204082,  5.30612245,  5.51020408,  5.71428571,  5.91836735,
        6.12244898,  6.32653061,  6.53061224,  6.73469388,  6.93877551,
        7.14285714,  7.34693878,  7.55102041,  7.75510204,  7.95918367,
        8.16326531,  8.36734694,  8.57142857,  8.7755102 ,  8.97959184,
        9.18367347,  9.3877551 ,  9.59183673,  9.79591837, 10.        ]),
0.20408163265306123)
```





### 2.Attributes

|  Attribute  | Description                                                  |
| :---------: | :----------------------------------------------------------- |
|   `ndim`    | 幾維。Number of array dimensions.                            |
|   `shape`   | 維度。A tuple of integers representing the size of the array in each dimension. |
|   `size`    | 元素數。Total number of elements in the array.               |
|     `T`     | 轉置。Transpose of the array.                                |
|   `dtype`   | 元素性質。Data type of the elements of the array.            |
|  `nbytes `  | 記憶體大小。Total size (in bytes) of the array               |
| `itemsize ` | 每個元素記憶體大小。Size (in bytes) of each element of the array. |









[Top](#Numpy Array Introduction)
