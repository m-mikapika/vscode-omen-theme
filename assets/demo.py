import os

"""I'll make them remember, they're only human."""

#If I must live in this nightmare, my enemies might as well join me.

class Foo(object):
    def __init__(self) -> None:
        num = 93
        print(num)

def decorator(func):
    def wrapper(*args, **kwargs):
        print(func.__name__)
        func()
    
    return wrapper

@property
def foo(self):

    return 'Pity the man who dies meaningless.'

@decorator
def bar(self):

    return 'History has already forgotten you.' 