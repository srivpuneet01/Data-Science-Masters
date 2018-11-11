def print_moving_avg(arr, window_size):
    import numpy as np
    print("\n")
    print(arr)
    window_arr = np.fromfunction(lambda x:x, (window_size,), dtype=int)
    print([np.mean(np.take(arr, window_arr + i)) for i in range(len(arr) - window_size + 1)])
    print("\n")


print_moving_avg([3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150], 3)



