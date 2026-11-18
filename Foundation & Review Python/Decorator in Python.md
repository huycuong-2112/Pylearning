---
link: https://www.geeksforgeeks.org/python/decorators-in-python/
---
==🔴The non-parameter Decorator in python==
==🔴Decorators== are flexible way tomodify or extend behavior of functions on methods, without changing their actual code.

+ It takes another function as an argument and returns a new function with enhanced functionality
+ They are often used in scenarios such as logging, authentication and memoization, allowing us to add additional functionality to existing functions or methods in a clean, reusable way.
![[205695853.webp]]

Example:
**I have** 
```
def greet():
	print('hello')
```
**Now I want to extend the function, i want to print 'before' before the 'hello' and after the 'after', i will create a function that has the initial function as a argument**
```
def my_decorator (func)"
	def wrapper():
		print('Before')
		func()
		print('After')
	
	return wrapper
@my_decorator1 (assume it's a valid function)
@my_decorator
def greet():
	print('hello')
```
The `@my_decorator` equivalent `greet =  my_decorator(greet)`
The `@my_decorator1` equivalent `greet = my_decorator1(my_decorator(greet))`, ==🟡 **It's called "Channing Multiple Decorators" ==

# ==🔴Use Decorator with parameters==

Commonly, we often use the decorator with functions which have parameters. We use `*args` and `**kwargs` to store the parameters, so our wrappers can accept any number of parameters.
	Explanation:
		 - The `wrapper(*args, **kwargs)` nested function that wraps another functions. `*args` collects positional arguments, `**kwargs` collects keyword arguments 

```
def parameter_decorator(func):
	def wrapper(*args, **kwargs):
		print("Starting Execution")
		return func(*args, **kwargs)
		print("Finish Execution")
	
	return wrapper
@parameter_decorator
def add(a,b,c):
	return a + b +c

print(add(3,5,3))
```
**Output:
```
Starting Execution
Finish Execution
11
```

More example:
Remake the `app.get('/users') in FastAPI` 
```
routes = {}

def get(path):
	def decorator(func):
		print("Start execution")
		routes[path] = func
		print("Finish")
		return func 
		
	return decorate
@get("/users")
def get_usesr():
	return["Alice", "Bob"]
print(routes)
```
Output is location of the get_users function, because in backend we just need to know where the function to execute
```
<function get_users at 0x000001F4E6E5DD00>
```

# Some Bulit-in Decorate
1. @staticmethod : use directly function in the class without the defined step
```
	class Student:
		school = 'UIT'
		def __init__(self,name,score):
			self.name = name
			self.score = score
		@staticmethod
		def greet():
			print (f"Hello, I'm a {Student.school}")
	Student.greet()
	OUTPUT:
	Hello, I'm a UIT
```
2. @classmethod
```
	class Student:
		school = 'UIT'
		def __init__(self,name,score):
			self.name = name
			self.score = score
		@classmethod
		def show(cls):
			print(f"Toi la mot sinh vien {cls.school}")
		
	Student.show()
	OUTPUT:
	Toi la mot sinh vien UIT
```
2. @property: Used to define a method as a property, which allows to access it like an attribute. This is useful for encapsulating implementation of a method while still providing a simple interface.
```
	class Student:
		school = 'UIT'
		def __init__(self,name,score):
			self.name = name
			self.score = score
	@property
	def introduce(self):
		return self.name
		
	s = Student("Huy Cuong",9.8)
	print(f"s.introduce") #instead s.introduce()
```

