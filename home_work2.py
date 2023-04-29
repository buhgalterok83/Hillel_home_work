def call_counter(file):
    def decorator(func):
        def wrapper(*args, **kwargs):
            with open(file, 'a') as f:
                wrapper.counter += 1
                f.write(f"Function '{func.__name__}' was called {wrapper.counter} times\n")
            return func(*args, **kwargs)
        wrapper.counter = 0
        return wrapper
    return decorator


@call_counter('data.txt')
def add(a, b):
    return a + b

add.counter = 0

print(add(4, 6))
print(add.counter)
print(add(4, 6)) 
print(add.counter)
