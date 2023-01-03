from application3 import get_operating_system

def test_get_operation_system(mocker):
    mocker.patch('application3.sample_utility.is_windows', return_value=True)
    assert get_operating_system() == 'Windows'