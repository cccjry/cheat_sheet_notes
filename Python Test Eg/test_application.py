from application import get_operating_system

def test_get_operating_system(mocker):
    mocker.patch('application.is_windows', return_value=True) 
    assert get_operating_system() == 'Windows'

def test_operation_system_is_linux(mocker):
    mocker.patch('application.is_windows', return_value=False) # set the return value to be False
    assert get_operating_system() == 'Linux'