# http://hackflow.com/blog/2013/11/03/painless-decorators/

from functools import wraps

def some_decorator(func):
	@wraps(func)
	def wrapper(*args, **kwargs):
		# ... do something before
		result = func(*args, **kwargs)
		# ... do something after
		result = result + 5
		return result
	return wrapper

def my_func(*args):
	result = 0
	for x in args:
		result = result + x
	return result

# print my_func(1, 2, 3)

mystery = some_decorator(my_func)

# print mystery(1, 2, 3)

def some_decorator(before, after):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            before()
            result = func(*args, **kwargs)
            after()
            return result
        return wrapper
    return decorator

def my_before():
	print "Before"

def my_after():
	print "After"

# print some_decorator(my_before, my_after)(my_func)(1, 2, 3)

