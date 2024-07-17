import time

def delay(seconds):
    def decorator(func):
        def wrapper(*args, **kwargs):
            time.sleep(seconds)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@delay(5)
def it_may_be(name=''):
    return (name + " ask: It's nearly Luncheon Time? \n")

for t in range(12):
    print(it_may_be(name='Winnie-the-Pooh'))