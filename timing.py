import time

def calculate_time(func):
    
    def timer(*args, **kwargs):
        start_time = time.time()
        value = func(*args, **kwargs)
        end_time = time.time()
        run_time = end_time - start_time

        return value
    return timer

@calculate_time
def func():
	time.sleep(2)
func()