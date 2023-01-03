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

### 

## Reference

- [Mocking functions Part I](https://medium.com/analytics-vidhya/mocking-in-python-with-pytest-mock-part-i-6203c8ad3606)
- [Mocking functions Part II](https://medium.com/@durgaswaroop/writing-better-tests-in-python-with-pytest-mock-part-2-92b828e1453c)
