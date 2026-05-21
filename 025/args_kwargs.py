def func(a, b, c, *args, **kwargs):
    print(a, b, c)
    print(args)
    print(kwargs)

func('Hello', 'Dear', 'Viewer', z='Hello')