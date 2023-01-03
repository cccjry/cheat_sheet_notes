import sample_utility 

def get_operating_system():
    return 'Windows' if sample_utility.is_windows() else 'Linux'