
def h_ascii(key, N):
    if key == '':
        raise ValueError("Empty string supplied")
    if key is None:
        raise ValueError("Key cannot be None")
    if N <= 0:
        raise ValueError("Size of array must be positive integer")
    str_val = 0
    output = 0
    for char in key:
        str_val += ord(char)
    if str_val == N:
        output = N - 1
    elif str_val > N:
        output = str_val - (str_val - N) - 1
    else:  # str_val < N
        output = str_val - 1
    return output


def h_rolling(key, N):
    pass
