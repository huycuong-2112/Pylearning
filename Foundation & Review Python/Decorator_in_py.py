def my_decorator(func):
    def wrapper():
        print('Before')
        func()
        print('After')
    
    return wrapper

@my_decorator
def hello():
    print('hello')

routes = {}

def get(path):
    def decorator(func):
        routes[path] = func
        return func

    return decorator

@get("/users")
def get_users():
    return ["Alice", "Bob"]

print(get_users)




