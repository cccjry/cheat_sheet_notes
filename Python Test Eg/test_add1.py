import pytest
from random import randint

from sample_function_add1 import add1

'''
Basic use
'''
def test_add1_result():
    test_obj = randint(-100, 100)
    assert add1(test_obj) == test_obj + 1

def test_add1_output_type():
    test_obj = randint(-100, 100)
    assert type(add1(test_obj)) is int

## % pytest test_add1.py -v

'''
Parameterize methods
'''
test_obj1 = randint(-100, 100)
@pytest.mark.parametrize('x, expected', [(test_obj1, test_obj1 + 1)])
def test_add1_result_param(x, expected):
    assert add1(x) == expected

'''
auto-create test cases(better use with fixture property, this one is just an example)
'''
def auto_gen_testcases():
    testcases = []
    for i in range(-2, 2):
        testcases.append((i, i + 1))
    return testcases

@pytest.mark.parametrize('x, expected', auto_gen_testcases())
def test_add1_result_param(x, expected):
    assert add1(x) == expected

'''
The use of consistently test.
Some kind of a pack of same-property test, only shown detail when failed)
'''
# @pytest.fixture
# def with_failed_testcase():
#     testcases = []
#     for i in range(-50, 50):
#         testcases.append((i, i + 1))
#     ''' failed test examples
#     testcases.append((1, 0))
#     '''

#     return testcases

# def test_add1_result_fixtures(with_failed_testcase):
#     for cases in with_failed_testcase:
#         assert add1(cases[0]) == cases[1]

##############################################################

'''
Actions every session<moddule<class<function.
In this fixture, action before and after each test and set to be "autouse"
'''
@pytest.fixture(autouse=True)
def setup_and_teardown():
    print('\nFetching data from db')
    yield
    print('\nSaving test run data in db')

'''
The fixture are set to be 'every session'
'''
@pytest.fixture(scope="session")
def with_failed_testcase2():
    testcases = []
    for i in range(-50, 50):
        testcases.append((i, i + 1))
    ''' failed test examples
    testcases.append((1, 0))
    '''
    return testcases

def test_add1_result_fixtures2(with_failed_testcase2):
    for cases in with_failed_testcase2:
        assert add1(cases[0]) == cases[1]

## % pytest test_add1.py -v -s

##############################################################
'''
Filter tests by choosing the marker
'''
@pytest.mark.myconditionmarker
def test_add():
    assert add1(5) == 6

## % pytest test_add1.py -m myconditionmarker -v



##############################################################
'''
Some cheet sheets:

#1 Run all tests with some string 'validate' in the name
pytest -k “validate”
#2 Exclude tests with 'db' in name but include 'validate'
pytest -k “validate and not db” 
#3 Run all test files inside a folder demo_tests
pytest demo_tests/
#4 Run a single method test_method of a test class TestClassDemo 
pytest demo_tests/test_example.py::TestClassDemo::test_method
#5 Run a single test class named TestClassDemo 
pytest demo_tests/test_example.py::TestClassDemo
#6 Run a single test function named test_sum
pytest demo_tests/test_example.py::test_sum
#7 Run tests in verbose mode: 
pytest -v demo_tests/
#8 Run tests including print statements: 
pytest -s demo_tests/
#9 Only run tests that failed during the last run 
pytest — lf

More example from internet: https://github.com/shashikumarraja/pytest_tutorial

'''