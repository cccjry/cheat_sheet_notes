from time import sleep  
def is_windows():    
    # This sleep could be some complex operation instead
    sleep(2)    
    return True  
def get_operating_system():    
    return 'Windows' if is_windows() else 'Linux'