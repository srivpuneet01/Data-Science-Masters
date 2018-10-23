def my_filter(fn, collection):
    iterable_collection = iter(collection)
    length = len(collection) 
    a = 0
    if(length == 0): 
        raise ValueError("'collection' should contain one or more elements")
    try:
        a = next(iterable_collection)
        while length > 0:
            a = next(iterable_collection)
            if fn(a):
                yield a
            length -= 1
    except:
        pass
