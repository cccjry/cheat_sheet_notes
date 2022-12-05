# `if __name__ == "__main__"`

```python
# your code

if __name__ == "__main__":
    run_function()
```



## Modules

> A **module** is a self-contained piece of code, that is **logically separatable** from other pieces of code.

簡言之，**module** 可以泛指那些能夠<u>**獨立**</u>、<u>**可被重複使用**</u>且<u>**容易被區別成一個獨立單元**</u>的功能。也因此 套件(libraries)、函式(functions)、類別(classes)、獨立檔案(*.py) 都可以被稱之為 **module**。

而 `__name__` 則是指在 modules 之間互相交握時會用到的特殊變數，這個變數可以區別出



## Code Level

舉例：

```python
# my_program.py
import pandas	#<--top level
	#<--top level
df = pandas.DataFrame()
print("bla bla bla")	#<--top level
```

```
(base) % python3 my_program.py
bla bla bla
```

`DataFrame()` 並沒有在 `my_program.py` 當中被定義，無法直接運作，而是從 `pandas` 當中被借出來使用的，因此不算是 top level。

**NOTE**: 直接寫在 console 當中的也被歸類在 top level！

```
(base) % python3 -c "print('AAA')"
AAA
```



## `"__main__"`

> `"__main__"` represents the **name of the top level environment**, where top level code runs.

所以檢查 `if __name__ == "__main__"` 可以確定我們執行的程式是不是屬於 top level。



舉例1：

```python
# my_program.py
import pandas

df = pandas.DataFrame()
print("bla bla bla")
print(__name__)
print(pandas.__name__)
```

```
(base) % python3 my_program.py
bla bla bla
__main__
pandas
```

舉例2：

```python
# my_program.py
from pandas import DataFrame

print(DataFrame.__name__)
print(pandas.__name__)
```

```
(base) % python3 my_program.py
DataFrame
Traceback (most recent call last):
  File "/Users/ccchen-jerry/Documents/production_Pyhon/aaa/my_program.py", line 4, in <module>
    print(pandas.__name__)
NameError: name 'pandas' is not defined
```



## Rule of Thumbs

- Libraries: 因為 `__name__` 的特性讓套件可以直接使用名稱且不需要 `.py` 副檔名
- Classes, Functions: `__name__` 就直接等同於一個 Class 或是一個 Function 的名稱，直接在程式當中呼叫其名稱並且使用它。



使用情境：

```python
# import_me.py
def call_this():
    print("yaa")

call_this()
```

```python
# run_me.py
from import_me import call_this
```

```
(base) % python3 run_me.py
yaa
```

可以發現 `run_me.py` 不但引用 `call_this` 這個函式，還直接執行了一遍。



將 `import_me.py` 加上 `if __name__ == "__main__":` 之後重新執行一遍：

```python
# import_me.py
def call_this():
    print("yaa")

if __name__ == "__main__":
	call_this()
```

```
(base) % python3 run_me.py

```

就沒有自動執行了，這是因為 `if __name__ == "__main__":` 這個檢查動作確保在 `import` 的過程中，`call_me()` 是屬於在 top level 的呼叫，其運行的過程、結果並不會直接地被顯現出來。
