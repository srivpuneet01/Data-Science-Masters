# define fucton to devide by zero
def dividebyZero():
    a = 0
    try:
        a = 5/0
    except ZeroDivisionError as ex :
        print(ex)
    print(a)

dividebyZero()