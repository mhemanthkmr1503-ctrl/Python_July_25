def kw_arguments(**kwargs):
    print(kwargs)
    print(type(kwargs))
    print(kwargs['name'])

kw_arguments(name = "Raj", company = "INFY", exp = 2)
