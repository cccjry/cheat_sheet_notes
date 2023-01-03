# Unit test example in Python
> File description

## Unittest

Related files:

| Name               | Detail |
| ------------------ | ------ |
| unittest_sample.py |        |



## Pytest

| Name                    | Detail                                  |
| ----------------------- | --------------------------------------- |
| sample_function_add1.py | An function as a test target.           |
| test_add1.py            | Pytest basic use and some cheat sheets. |



## Pytest with Mocking

> 進行測試時，把不想要執行的方法給替換掉，在測試的過程中，有時候只是要測試函式的可用性，但像是發送 email、撰寫檔案等等的函式，往往是不希望被執行的，總不能每執行一次測試就寄一封 mail 給你，這樣信箱會很快就爆炸的，針對這個情況我們就可以透過 pytest-mock 來替我們進行函式的抽換，並回傳假的資料，只要確認函式運行的流程是正確的即可。

### E.g.1

| Name                    | Detail                                              |
| ----------------------- | --------------------------------------------------- |
| **application.py**      | An application as a mocking target.                 |
| **test_application.py** | Pytest the **application.py** with mocking setting. |

### E.g.2

| Name                     | Detail                                                      |
| ------------------------ | ----------------------------------------------------------- |
| **sample_utility.py**    | An independent function outside **application2.py**.        |
| **application2.py**      | An application using function inside **sample_utility.py**. |
| **test_application2.py** | Pytest the **application2.py** with mocking setting.        |

### E.g.3

| Name                     | Detail                                                       |
| ------------------------ | ------------------------------------------------------------ |
| **sample_utility.py**    | Same independent function in E.g.2.                          |
| **application3.py**      | An application using function inside **sample_utility.py**. *But with different importing type.* |
| **test_application3.py** | Pytest the **application3.py** with mocking setting. (Notice differences in mock setting) |

### E.g.4

| Name                     | Detail                                                       |
| ------------------------ | ------------------------------------------------------------ |
| **application4.py**      | An application with some functions inside. |
| **test_application4.py** | Pytest the **application4.py** with mocking `add` inside `calculate` |

## Reference

- [Mocking functions Part I](https://medium.com/analytics-vidhya/mocking-in-python-with-pytest-mock-part-i-6203c8ad3606)
- [Mocking functions Part II](https://medium.com/@durgaswaroop/writing-better-tests-in-python-with-pytest-mock-part-2-92b828e1453c)
