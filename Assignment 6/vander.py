#import numpy module
import numpy as np

def generate_vander_matrix(vector, no_of_columns, increasing):
    #define numpy array as input
    x = np.array(vector)
    start, stop, step = 0, 0, 1
    if not increasing:
        stop = no_of_columns
    else:
        start, stop, step = no_of_columns - 1, -1, -1
    print("\n")
    print("Printing in {a} order:".format(a="increasing" if increasing else "decreasing"))
    print(np.column_stack([x**(no_of_columns - 1 - i) for i in range(start, stop, step)]))

generate_vander_matrix([1,2,3,4,5], 5, True)