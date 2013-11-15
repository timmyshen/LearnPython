# http://julien.danjou.info/blog/2013/guide-python-static-class-abstract-methods

# The definitive guide on how to use static, class or abstract methods in Python

import math
import abc

class Pizza(object):
	"""
	docstring for Pizza
	"""
	def __init__(self, size):
		super(Pizza, self).__init__()
		self.size = size
	def get_size(self):
		return self.size

# Note that it's 'unbound'
print Pizza.get_size

# TypeError: unbound method get_size() must be called with Pizza instance as first argument (got nothing instead)
# Pizza.get_size()

print Pizza.get_size(Pizza(42))

print Pizza(42).get_size()

# The following gives: <bound method Pizza.get_size of <__main__.Pizza object at 0x000000000259B320>>
# Note that it is 'bound' to an object
print Pizza(42).get_size

m = Pizza(42).get_size
print m()

# todo: I think we can show closure here.

# which object this bound method is bound to? Here's a little trick:
print m.__self__
print m == m.__self__.get_size

# In Python 3, the functions attached to a class are not considered as unbound method anymore, 
# but as simple functions, that are bound to an object if required. 
# So the principle stays the same, the model is just simplified.

# Static methods
print 'Section static methods'

class Pizza2(object):
	"""docstring for Pizza2"""
	# def __init__(self, arg):
		# super(Pizza2, self).__init__()
		# self.arg = arg
	
	@staticmethod
	def mix_ingredients(x, y):
		return x + y

	def cook(self):
		return self.mix_ingredients(self.cheese, self.vegetables)

# Bound methods are objects too, and creating them has a cost. Having a static method avoids that:
print Pizza2().cook is Pizza2().cook
print Pizza2().mix_ingredients is Pizza2.mix_ingredients
print Pizza2().mix_ingredients is Pizza2().mix_ingredients

# Class methods
print 'Section class methods'

# Class methods are methods that are not bound to an object, but to a class!
class Pizza3(object):
	"""docstring for Pizza3"""
	# def __init__(self, arg):
		# super(Pizza3, self).__init__()
		# self.arg = arg
	
	radius = 42
	@classmethod
	def get_radius(cls):
		return cls.radius

# <bound method type.get_radius of <class '__main__.Pizza'>>
r1 = Pizza3.get_radius
print r1
r2 = Pizza3().get_radius
print r2

# OH NO! Author says it's True
print Pizza3.get_radius is Pizza3().get_radius

# This is True
print Pizza3.get_radius == Pizza3().get_radius

# todo: We are in TROUBLE
# 1. what's the difference between is and ==
# 2. how can I see the physical address of classmethod?

print Pizza3.get_radius()

# Factory methods
class Pizza4(object):
	"""docstring for Pizza4"""
	def __init__(self, ingredients):
		super(Pizza4, self).__init__()
		self.ingredients = ingredients
		
	@classmethod
	def from_fridge(cls, fridge):
		return cls(fridge.get_cheese() + fridge.get_vegetables())

# Static methods calling static methods
class Pizza5(object):
	"""docstring for Pizza5"""
	def __init__(self, radius, height):
		super(Pizza5, self).__init__()
		self.radius = radius
		self.height = height

	@staticmethod
	def compute_circumference(radius):
		return math.pi * (radius ** 2)

	@classmethod
	def compute_volume(cls, height, radius):
		return height * cls.compute_circumference(radius)

	def get_volume(self):
		return self.compute_volume(self.height, self.radius)

# Abstract methods
print 'Section abstract methods'

class Pizza6(object):
	"""docstring for Pizza6"""
	def __init__(self):
		super(Pizza6, self).__init__()
	
	def get_radius(self):
		raise NotImplementedError

# the error will only be raised when you'll try to use that method.
print Pizza6()
# print Pizza6().get_radius()

class BasePizza(object):
	"""docstring for BasePizza"""
	def __init__(self):
		super(BasePizza, self).__init__()
		
	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def get_radius(self):
		print 'do something'

# Using abc and its special class, 
# as soon as you'll try to instantiate BasePizza or 
# any class inheriting from it, you'll get a TypeError.

# print BasePizza()

# Mixing static, class and abstract methods
print 'Section Mixing static, class and abstract methods'

class BasePizza2(object):
	"""docstring for BasePizza2"""
	def __init__(self):
		super(BasePizza2, self).__init__()

	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def get_ingredients(self):
		'''Returns the ingredients list.'''

# Calzone fulfil the interface requirement we defined for BasePizza objects. 
class Calzone(BasePizza2):
	"""docstring for Calzone"""
	def __init__(self):
		super(Calzone, self).__init__()
	
	def get_ingredients(self, with_egg = False):
		egg = Egg() if with_egg else None
		return self.ingredients + egg

# This is also correct and fulfil the contract we have with our abstract BasePizza class. 
# The fact that the get_ingredients method don't need to know about the object to return result 
# is an implementation detail, 
# not a criteria to have our contract fulfilled.
class DietPizza(BasePizza2):
	"""docstring for DietPizza"""
	def __init__(self):
		super(DietPizza, self).__init__()
	
	@staticmethod
	def get_ingredients():
		return None

