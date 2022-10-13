# 4.Comprehension

[TOC]

## 4.1.List Comprehension

### 4.1.1.`for` Loop Create a List

```python
[x**2 for x in range(1,11)]
```

```
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

### 4.1.2.Create a List with `if`

```python
collection = ["Jane", "Peter", "Tom", "Julian", "Wendy", "Violet"]
[val.upper() for val in collection if val[0]=="J"]
```

```
['JANE', 'JULIAN']
```

### 4.1.3.`while` Loop Create a List

```python
squares = []
i = 1
while i**2 < 200:
    squares.append(i**2)
    i += 1
print(squares)
```

```
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
```

### 4.1.4.Including a Condition in the `list` Comprehension Expression

```python
names = ["Jane", "Peter", "Tom", "Julian", "Wendy", "Violet"]
io = [x[0]=="J" for x in names]
print(io)
print(sum(io))
```

```
[True, False, False, True, False, False]
2
```

### 4.1.4.Nested Comprehension

```python
import random as rd
A = [[j for j in list(rd.sample(range(10,100), 4))] for i in range(4)]
print(*A, sep='\n')

mat = [[j for j in range(5)] for i in range(3)]
print(mat)
print(*mat, sep='\n')
```

```
[35, 47, 42, 91]
[89, 43, 60, 85]
[64, 86, 85, 62]
[86, 41, 31, 14]

[[0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]

[0, 1, 2, 3, 4]
[0, 1, 2, 3, 4]
[0, 1, 2, 3, 4]
```



## 4.2.Dictionary Comprehension

```python
scores1 = {"Carol":68, "Sammy":85, "Derrick":62, "Juan":49, "Wendy":79, "Tom":86}
{k:
 "A" if v >85 else
 "B" if v > 75 else
 "C" if v >65 else
 "D"
 for (k, v) in scores1.items()}
```

```
{'Carol': 'C',
 'Sammy': 'B',
 'Derrick': 'D',
 'Juan': 'D',
 'Wendy': 'B',
 'Tom': 'A'}
```



## 4.3.Set Comprehension

```python
currencies = ["sgd", "usd", "hkd", "eur", "aud", "inr", "rmb", "sgd", "eur"]
{x.upper() for x in currencies}
```

```
{'AUD', 'EUR', 'HKD', 'INR', 'RMB', 'SGD', 'USD'}
```





[Top](#4.Comprehension)

[Back to Contents](Flow_README.md)
