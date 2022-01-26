def myfunction(first, *args, **kwargs):
    print(first)
    for i in args:
        print(i)
    print(type(args))
    for key, value in kwargs.items():
        print(f"{key} is a {value}")

myfunction(0)
args = ('a', 'b', 'c', 'd', 'e', 1)
myfunction(0, *args)

kwargs = {'1': 'x', '2': 'y', '3': 'z'}
myfunction(0, *args, **kwargs)
