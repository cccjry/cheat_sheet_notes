# 2.For Loops

[TOC]

## 2.1.The `for` Loop Statement

```python
for item in sequence:
    loop body
```



## 2.2.Setup Your Looping Ranges

### 2.2.1.`range()`

```python
range(start, stop, step)
```

| Parameter | Required? | Default Value | Description                                                  |
| --------- | :-------: | :-----------: | ------------------------------------------------------------ |
| `start`   |   ❌ No    |       0       | An integer number specifying the start index of the range object. |
| `stop`    |   ✔️ Yes   |      NA       | An integer number specifying the stop index of the range object. |
| `step`    |   ❌ No    |       1       | An integer number specifying the step size.                  |

> **Note**: The `range` object produces integers **up to but not including the endpoint**.

#### Example

```python
total = 0
for i in range(101):
    if i % 2 == 0: # modulo operator to ensure that only even numbers get summed
        total += i
print(f"Sum of all even numbers from 1 to 100 is {total}")
#There is an efficient way to do sum. This is just an example.
```

```
Sum of all even numbers from 1 to 100 is 2550
```



### 2.2.2.`enumerate()`

```python
enumerate(sequence, start)
```

| Parameter  | Required? | Default Value | Description                                              |
| ---------- | :-------: | :-----------: | -------------------------------------------------------- |
| `sequence` |   ✔️ Yes   |      NA       | An iterable object that supports iteration.              |
| `start`    |   ❌ No    |       0       | The index value from which the counter is to be started. |

> **Note**: The `range` object produces integers **up to but not including the endpoint**.

#### Example

```python
for (index, fruit) in enumerate(fruits,2):
    print(f"{index}: {fruit}")
```

```
2: apple
3: orange
4: banana
5: pear
6: pineapple
7: durian
```



### 2.2.3.`zip()`

| Parameter  | Required? | Default Value | Description                                              |
| ---------- | :-------: | :-----------: | -------------------------------------------------------- |
| `sequence` |   ✔️ Yes   |      NA       | An iterable object that supports iteration.              |
| `start`    |   ❌ No    |       0       | The index value from which the counter is to be started. |

> **Note**: The `range` object produces integers **up to but not including the endpoint**.

#### Example

```python
names = ["Lily", "Jane", "Tom", "Matt"]
scores = [62, 86, 75, 91]
grades = ["C", "A", "B", "A+"]

for (i, (name, score)) in enumerate(zip(names, scores)):
    print(f"{i}: {name} receives a score of {score}")

for (name, score, grade) in zip(names, scores, grades):
    print(f"{name} receives a score of {score} and grade {grade}.")
```

```
0: Lily receives a score of 62
1: Jane receives a score of 86
2: Tom receives a score of 75
3: Matt receives a score of 91

Lily receives a score of 62 and grade C.
Jane receives a score of 86 and grade A.
Tom receives a score of 75 and grade B.
Matt receives a score of 91 and grade A+.
```



### 2.2.4.Some Other Useful Functions

#### 2.2.4.1.`random.sample()`

> **No repetition is allowed**

```python
random.sample(range(1, 11), 10)
```

```
[8, 10, 9, 2, 3, 1, 7, 6, 5, 4]
```

#### 2.2.4.2.`random.choice()`

**Repetition is allowed**

```python
tosses = random.choices(range(1, 7), k=100)
dict1 = {}
for x in range(1, 7):
    dict1[x] = tosses.count(x)
    print(f"Face {x} shows {dict1[x]} times")
```

```
Face 1 shows 20 times
Face 2 shows 22 times
Face 3 shows 15 times
Face 4 shows 14 times
Face 5 shows 17 times
Face 6 shows 12 times
```





[Top](#2.For Loops)

[Back to Contents](Flow_README.md)