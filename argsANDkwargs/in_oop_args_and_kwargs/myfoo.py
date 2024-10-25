from foo import Foo

class MyFoo(Foo):
    def __init__(self, *args, **kwargs):
        super(MyFoo, self).__init__(*args, **kwargs)