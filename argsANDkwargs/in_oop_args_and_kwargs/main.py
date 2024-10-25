from foo import Foo
from myfoo import MyFoo

# Ex: 1 - Creating an instance of Foo
foo_instance = Foo(5, 10)
print("Foo Instance")
print(f'Width: {foo_instance.width}, Height: {foo_instance.height}')

# Ex: 2 - Creating an instance of MyFoo with the same arguments
myfoo_instance = MyFoo(8, 12)
print("MyFoo Instance")
print(f'Width: {myfoo_instance.width}, Height: {myfoo_instance.height}')

# Ex: 3 - Using *args to pass positional argumenets
args = (15, 20)
myfoo_instance_args = MyFoo(*args)
print("with *args")
print(f'Width: {myfoo_instance_args.width}, Height: {myfoo_instance_args.height}')
print(f'Width: {Foo.width}, Height: {Foo.height}')

# Ex: 4 - Using **kwargs to pass keyword arguments
kwargs = {'a': 7, 'b': 14}
myfoo_instance_kwargs = MyFoo(**kwargs)
print("with **kwargs")
print(f'Width: {myfoo_instance_kwargs.width}, Height: {myfoo_instance_kwargs.height}')
