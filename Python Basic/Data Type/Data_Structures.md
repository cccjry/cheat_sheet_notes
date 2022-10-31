# Data Structures

[TOC]

## Overviews

In Python, data structures are objects that contain possibly a large number of other objects. Data structures make working with a collection of objects more convenient. Among the built-in data structures are **lists**, **tuples**, **dictionaries** and **sets**.



## Summary

| Data Structure                | Ordered | Indexed | Mutable |         Example          |
| :---------------------------- | :-----: | :-----: | :-----: | :----------------------: |
| [List](#1.lists)              |    ✔️    |    ✔️    |    ✔️    |        `[1,2,3]`         |
| [Tuple](#2.tuples)            |    ✔️    |    ✔️    |    ❌    |        `(1,2,3)`         |
| [Dictionary](#3.dictionaries) |    ❌    |    ✔️    |    ✔️    | `{'a':1 , 'b':2, 'c':3}` |
| [Set](#4.sets)                |    ❌    |    ❌    |    ✔️    |        `{1,2,3}`         |



## 1.Lists

> **Note**: The items in a list need not be of the same type.



### 1.1.Basic Operaters

```python
listA = [1, 2, 3, 4, 5, 6]
listB = ["a", "b", 'c', "d",'f']
listC = ['UK', 'USA', True, 2021, 2022]

listA+listB		#concatenation
len(listA)		#length
listB*2				#repetition
2022 in listC	#boolean

newlist = [listA, listB]	#nested list
newlist

row1 = [1,2,3]
row2 = [4,5,6]
row3 = [7,8,9]
mat = [row1, row2, row3]	#matrix in nested list
mat
```

```
[1, 2, 3, 4, 5, 6, 'a', 'b', 'c', 'd', 'f']
6
['a', 'b', 'c', 'd', 'f', 'a', 'b', 'c', 'd', 'f']
True

[[1, 2, 3, 4, 5, 6], ['a', 'b', 'c', 'd', 'f']]

[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```



### 1.2.Indexing and Slicing

#### 1.2.1.Indexing

```python
listA[0]
listA[2:]
listA[-2]

newlist[0]
newlist[1][2:4] #chain indexing
```

```
1
[3, 4, 5, 6]
5

[1, 2, 3, 4, 5, 6]
['c', 'd']
```

#### 1.2.2.Slicing

> `sequence[start:stop:step]`

| **Parameter** | **Description**                                              |
| ------------- | ------------------------------------------------------------ |
| `start`       | Optional (default=0). An integer number specifying at which position to start the slicing. |
| `stop`        | An integer number specifying at which position to end the slicing. |
| `step`        | Optional (default=1). An integer number specifying the step of the slicing. |

#### 1.2.3.Print Elements Individually

```python
print(*listA)
```

```
1 2 3 4 5 6
```



### 1.3.Mutable and Immutable Objects

> Refers to the original object or not.

```python
a="Singapore"
print(a)
print(id(a))

a = a + "an"
print(id(a))		#string is not mutable

```

```
Singapore
2269554790960

2269554498992
```

#### 1.3.1.List is mutable

```python
myList = ['foo','bar','cup']
print(id(myList))

myList[1] = 'hat'
print(id(myList))
```

```
2269554819584

2269554819584
```

That is, the list has been **modified in place**.

```python
values = [1, 2, 3]
values2 = values
print(id(values))
print(id(values2))		#refers to the same address

values2.append(4)
print(values)					#had being modified, too
print(values2)
print(id(values))
print(id(values2))		#stays the same
```

```
2269554820608
2269554820608

[1, 2, 3, 4]
[1, 2, 3, 4]
2269554820608
2269554820608
```



### 1.4.Methods

```python
fruits = ["orange", "apple", "banana"]
```

#### 1.4.1.`append()`

```python
fruits.append("pineapple")
print(fruits)
```

```
['orange', 'apple', 'banana', 'pineapple']
```

#### 1.4.2.`sort()`

```python
fruits.sort(reverse=False)
print(fruits)
```

```
['apple', 'banana', 'orange', 'pineapple']
```

#### 1.4.3.`extend()`

> An extension of append().

```python
fruits.extend(["grape", "watermelon"])
print(fruits)

#equivalent
fruits + ["grape", "watermelon"]
```

```
['apple', 'banana', 'orange', 'pineapple', 'grape', 'watermelon']
```

#### 1.4.4.`insert()`

```python
fruits.insert(2, "kiwi")
print(fruits)
```

```
['apple', 'banana', 'kiwi', 'orange', 'pineapple', 'grape', 'watermelon']
```

#### 1.4.5.`pop()`

```python
fruits.pop(2)
print(fruits)
```

```
['apple', 'banana', 'orange', 'pineapple', 'grape', 'watermelon']
```

#### 1.4.6.`count()`

```python
fruits.append("pineapple")
print(fruits.count("pineapple"))
```

```
2
```

#### 1.4.7.`index()`

```python
print(fruits.index("pineapple"))
```

```
3
```

**Note**: **Only returns the first index** when there is more than 1 occurrence of the specified value.

#### 1.4.8.`copy()`

```python
fruits_2nd = fruits.copy()
print(fruits_2nd)
print(id(fruits))
print(id(fruits_2nd))
```

```
['apple', 'banana', 'orange', 'pineapple', 'grape', 'watermelon', 'pineapple']
140578878639616
140578878016512
```

> **Caution**: Using `fruits_2nd=fruits` will also mutate the original object.

#### 1.4.9.Others

| Method      | Description                                      |
| ----------- | ------------------------------------------------ |
| `clear()`   | Removes all the elements from the list.          |
| `remove()`  | Removes the first item with the specified value. |
| `reverse()` | Reverses the order of the list.                  |

[Top](#Summary)



## 2.Tuples

> Similar to list, but **tuples are immutable**.

Once created, their elements cannot be changed unless a new tuple object is created. Tuples are the obvious choice for a collection of constants that never change throughout the program. It is written as a sequence of comma-separated values enclosed within a pair of parentheses `()`.

### 2.1.Create a tuple

```python
tupA = (1,2,3,3,4,5,6)
tupB = (1,2,3,"Python","code")
print(tupA)
print(tupB)

newTup = (tupA, tupB,(2,4,6))
print(newTup)
```

```
(1, 2, 3, 3, 4, 5, 6)
(1, 2, 3, 'Python', 'code')

((1, 2, 3, 3, 4, 5, 6), (1, 2, 3, 'Python', 'code'), (2, 4, 6))
```



### 2.2.Basic Operations

```python
tupA + tupB				#concatenation
len(tupA)					#length
tupB*2						#repetition
"Python" in tupB	#boolean
```

```
(1, 2, 3, 3, 4, 5, 6, 1, 2, 3, 'Python', 'code')
7
(1, 2, 3, 'Python', 'code', 1, 2, 3, 'Python', 'code')
True
```



### 2.3.Indexing and Slicing

#### 2.3.1.Indexing

```python
tupA[1]	#basic indexing
```

```
2
```

> **Recall**: Tuple is immutable. That is, it does not support item assignment.

```python
tupA[1] = 20
```

```
TypeError: 'tuple' object does not support item assignment
```

Using list to modify a tuple.

```python
temp = list(tupA)
temp[1]=20
tupA_updated = tuple(temp)
tupA_updated
```

```
(1, 20, 3, 3, 4, 5, 6)
```

#### 2.3.2.Slicing

Similar to list.

> `sequence[start:stop:step]`

| **Parameter** | **Description**                                              |
| ------------- | ------------------------------------------------------------ |
| `start`       | Optional (default=0). An integer number specifying at which position to start the slicing. |
| `stop`        | An integer number specifying at which position to end the slicing. |
| `step`        | Optional (default=1). An integer number specifying the step of the slicing. |



### 2.4.Methods

There are fewer methods available since tuples are immutable.

| Method    | Description                                                  |
| --------- | ------------------------------------------------------------ |
| `count()` | Returns the number of elements with the specified value.     |
| `index()` | Returns the index of the first element with the specified value. |

[Top](#Summary)



## 3.Dictionaries

> Dictionaries are ***mutable***. The ***Key*** is more important instead of order(dictionaries is unordered). The **keys must be unique**. Thus keys should be of an immutable data type such as **strings**, **numbers**, or **tuples**.

### 3.1.Define a Dictionary

```python
dict1 = {"Name": "Candice", "Age":22, "Gender": "Female", "Home": "NY"}
dict2 = {"Gender": "Female", "Name": "Candice", "Home": "NY", "Age":22}

print(dict1 == dict2)		#unordered
print(dict1["Age"])

dict3 = {'weather': 'thunderstorms', 1: [2, 4, 3], (20,30):92}		#different type of keys
```

```
True
22
```



### 3.2.Modifying

```python
entry = {'name': 'Wendy', 'age': 26, 'gender':'female','height':173}
entry['age'] = 27							#update an item
print(entry)

entry['country'] = 'Canada'		#add an item
print(entry)

del entry['height']						#remove an item
print(entry)

del entry											#remove entire dictionary
```

```
{'name': 'Wendy', 
 'age': 27, 
 'gender': 'female', 
 'height': 173}

{'name': 'Wendy',
 'age': 27,
 'gender': 'female',
 'height': 173,
 'country': 'Canada'}

{'name': 'Wendy',
 'age': 27,
 'gender': 'female',
 'country': 'Canada'}
```



### 3.3.Methods

#### 3.3.1.`pop()`

```python
dict1 = {1: 'apple', 2: 'orange', 3: 'banana', 4: 'pineapple'}
dict1.pop(2)
print(dict1)
print(dict1.pop(8, "Printed if not exist"))
```

```
{1: 'apple', 3: 'banana', 4: 'pineapple'}
'Printed if not exist'
```

#### 3.3.2.`popitem()`

```python
dict1 = {1: 'apple', 2: 'orange', 3: 'banana', 4: 'pineapple'}
dict1.popitem()
print(dict1)
```

```
{1: 'apple', 2: 'orange', 3: 'banana'}
```

#### 3.3.3.`clear()`

```python
dict1.clear()
print(dict1)
```

```
{}
```

#### 3.3.4.`copy()`

```python
dict1 = {1: 'apple', 2: 'orange', 3: 'banana', 4: 'pineapple'}
dict2 = dict1.copy()
dict1.popitem()

print(dict2)
print(dict1)
```

```
{1: 'apple', 2: 'orange', 3: 'banana', 4: 'pineapple'}
{1: 'apple', 2: 'orange', 3: 'banana'}
```

> Note: Dictionary is **mutable**.

```python
dict1 = {1: 'apple', 2: 'orange', 3: 'banana', 4: 'pineapple'}
dict2 = dict1
dict1.popitem()
print(dict2)
```

```
{1: 'apple', 2: 'orange', 3: 'banana'}
```

#### 3.3.5.`keys()`, `values()`

```python
print(dict1.keys())
print(dict1.values())
```

```
dict_keys([1, 2, 3, 4])
dict_values(['apple', 'orange', 'banana', 'pineapple'])
```

##### View reflects all changes of the dictionary

```python
dictVals = dict1.values()
print(dictVals)

dict1[2] = "kiwi"
print(dictVals)
```

```
dict_values(['apple', 'orange', 'banana', 'pineapple'])
dict_values(['apple', 'kiwi', 'banana', 'pineapple'])
```

#### 3.3.6.`get()`

```python
allScores = {"Carol": 81, "Sammy": 85, "Derrick": 68, "Juan": 72, "Wendy": 79, "Tom": 86}

print(allScores.get("Tom"))
print(allScores.get("Jerry"))
print(allScores.get("Jerry", "No item"))
```

```
86
None
No item
```

#### 3.3.7.`setdefault()`

```python
print(allScores.setdefault("Tom",100))

allScores.setdefault("Lisa",100)
print(allScores)
```

```
86
{'Carol': 81, 'Sammy': 85, 'Derrick': 68, 'Juan': 72, 'Wendy': 79, 'Tom': 86, 'Lisa': 100}
```

#### 3.3.9.`items()`

```python
print(allScores.items())
```

```
dict_items([('Carol', 81), ('Sammy', 85), ('Derrick', 68), ('Juan', 72), ('Wendy', 79), ('Tom', 86), ('Lisa', 100)])
```

#### 3.3.9.`update()`

```python
allScores.update([("Lisa", 99)])
print(allScores)
```

```
{'Carol': 81, 'Sammy': 85, 'Derrick': 68, 'Juan': 72, 'Wendy': 79, 'Tom': 86, 'Lisa': 99}
```

[Top](#Summary)



## 4.Sets

> Also as a dictionary, a set are **mutable**. And it's an **unordered collection of unique elements** which are **unindexed**. Most important thing, **set items are immutable** such as strings, numbers or tuples.

A set is written as a sequence of comma-separated values enclosed within a pair of curly braces `{}`.

```python
set1 = {23, 85, 41, 19, 22}
set2 = {41, 22, 85, 23, 19}

print(set1 == set2)			#unordered
set1[1]									#unindexed
```

```
True
TypeError: 'set' object is not subscriptable
```

### 4.1.Basic Operation

```python
list1 = [2, 4, 6, 6, 8, 8, 8, 9]
set3 = set(list1)

print(set3)
print(len(set3))

```

```
{2, 4, 6, 8, 9}
5
```



### 4.2.Modifying

#### 4.2.1.`add()`, `update()`

```python
fruits = {'apple', 'orange', 'banana', 'pineapple'}
fruits.add("strawberry")
print(fruits)

moreFruits = {"durian", "pear"}
fruits.update(moreFruits)
print(fruits)
```

```
{'apple', 'banana', 'orange', 'pineapple', 'strawberry'}
{'apple', 'banana', 'durian', 'orange', 'pear', 'pineapple', 'strawberry'}
```

> **Note**: `update()` will remove duplicates.

#### 4.2.2.`remove()`, `clear()`

```python
fruits.remove("durian")
print(fruits)

fruits.clear()
print(fruits)
```

```
{'apple', 'banana', 'orange', 'pear', 'pineapple', 'strawberry'}
set()
```



### 4.3.Mathematical Operations

#### 4.3.1.`union()`

```python
set1 = {1, 2, 3, 4}
set2 = {2, 4, 6, 8}
print(set1.union(set2))
print(set1)
```

```
{1, 2, 3, 4, 6, 8}
{1, 2, 3, 4}
```

> **Note**: `union()` does not modify the original set. You can assign a new variable to store the result.

#### 4.3.2.`intersection()`

```python
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(A.intersection(B))
print(A & B) #equivalent
```

```
{4, 5}
{4, 5}
```

#### 4.3.3.`intersection_update()`

```python
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

A.intersection_update(B)
print(A)
```

```
{4, 5}
```

> **Note**: `intersection_update()` produces the intersection and update the set.

#### 4.3.4.`difference()`

```python
A = {1, 2, 3, 4, 5}
B = {2, 5}

print(A.difference(B))
print(A - B) #equivalent
```

```
{1, 3, 4}
{1, 3, 4}
```

#### 4.3.5.`difference_update()`

```python
A = {1, 2, 3, 4, 5}
B = {2, 5}

A.difference_update(B)
print(A)
```

```
{1, 3, 4}
```

> **Note**: `difference_update()` produces the intersection and update the set.

#### 4.3.6.`issubset()`

$$
B \subseteq A
$$

```python
A = {1, 2, 3, 4, 5}
B = {2, 5}
B.issubset(A)
```

```
True
```

#### 4.3.7.`issuperset()`

$$
A \supseteq B
$$

> `True` if *A* is a superset of B*. That is, all elements of *B* are present in *A*. Otherwise, it returns `False`.

```python
A = {1, 2, 3, 4, 5}
B = {2, 5}
A.issuperset(B)
```

```
True
```



#### 4.3.8.`isdisjoin()`

$$
A \cap B = \empty
$$

```python
A = {1, 3}
B = {2, 5}
A.isdisjoint(B)
```

```
True
```

#### 4.3.9.Others

| Method      | Description                                        |
| ----------- | -------------------------------------------------- |
| `copy()`    | Returns a copy of the set.                         |
| `discard()` | Removes an element from the set if it is a member. |

[Top](#Summary)
