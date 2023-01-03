import application4
from pytest_mock import MockFixture


def test_mock_function(mocker: MockFixture):
    return_value = 100

    mocker.patch(target="application4.add", return_value=return_value)

    result = application4.calculate(num1=10, num2=10)
    print(result)

    assert result == return_value