import time

def calculate_time(func):
    
    def timer(*args, **kwargs):
        start_time = time.time()
        x = func(*args, **kwargs)
        end_time = time.time()
        run_time = end_time - start_time
        print(f'Total time X',run_time)
        return x
    return timer

@calculate_time
def func():
	time.sleep(2)
func()