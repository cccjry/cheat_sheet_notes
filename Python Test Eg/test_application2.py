from application2 import get_operating_system

def test_get_operation_system(mocker):
    mocker.patch('application2.is_windows', return_value=True)
    assert get_operating_system() == 'Windows'