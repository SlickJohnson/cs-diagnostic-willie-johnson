def array_list():
    arr = []
    lst = []

    for i in range(0, 11):
        arr[i] = i
        lst.append(i)

    print(arr, lst)


def dict_hash():
    # not sure how to do this in python, but you basically have to set a Key to each value added to the dictionary
    print(":(")


def tuple():
    tup = {"i", "am", "IMMUTABLE!!!"}
    print(tup)


def generator():
    for i in range(0, 1):
        print(i)
        yield
