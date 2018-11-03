def my_reduce(fn, collection):
    iterable_collection = iter(collection)
    length = len(collection) - 1 
    a = 0
    if(length < 0): 
        raise ValueError("'collection' should contain one or more elements")
    elif(length == 0): 
        return next(iterable_collection)
    try:
        a = next(iterable_collection)
        while length > 0:
            a = fn(a, next(iterable_collection))
            length -= 1
    except:
        pass
    return a
