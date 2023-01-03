from sample_utility import is_windows

def get_operating_system():
    return 'Windows' if is_windows() else 'Linux'