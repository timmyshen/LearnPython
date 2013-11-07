# functools.wraps example

# This is a convenience function for invoking
# partial(update_wrapper, wrapped=wrapped, assigned=assigned, updated=updated)
# as a function decorator when defining a wrapper function. For example:

from functools import wraps

def my_decorator(f):
	@wraps(f)
	def wrapper(*args, **kwargs):
		print 'Calling decorated function'
		return f(*args, **kwargs)
	return wrapper

@my_decorator
def example():
	"""Docstring"""
	print 'Called example function'

example()
