def h_ascii(key, N):
    if key is None:
        raise ValueError("Key cannot be None")
    try:
        key = str(key)
    except TypeError:
        print("Cannot convert the key to a string")
        sys.exit(1)
    if key == '':
        raise ValueError("Empty string supplied")
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
    if key is None:
        raise ValueError("Key cannot be None")
    try:
        key = str(key)
    except TypeError:
        print("Cannot convert the key to a string")
        sys.exit(1)
    if key == '':
        raise ValueError("Empty string supplied")
    if key is None:
        raise ValueError("Key cannot be None")
    if N <= 0:
        raise ValueError("Size of array must be positive integer")

    H = 0
    k = len(key) - 1
    for char in key:
        c = ord(char)
        H = H + (c*(31**(k)))  # multiply char value by 31 raised to the count
        k += 1
    H = H % N  # modulo for size
    if H > N:
        H = H - 1
    elif H == N:
        H = H - 1
    elif H > N:
        H = H - (H - N) - 1
    return H


def h_fletcher64(key, N):
    if key is None:
        raise ValueError("Key cannot be None")
    try:
        key = str(key)
    except TypeError:
        print("Cannot convert the key to a string")
        sys.exit(1)
    if key == '':
        raise ValueError("Empty string supplied")
    if key is None:
        raise ValueError("Key cannot be None")

    a = list(map(ord, key))
    b = [sum(a[:i]) % 4294967295 for i in range(len(a)+1)]
    H = (sum(b) << 32) | max(b)
    return H
