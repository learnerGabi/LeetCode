
# out put -> boolean
def borningArray(a, b):
    # sort 2 list
    a = sorted(a)
    b = sorted(b)

    # compare each ele in a and b
    for i in range(len(a)):
        if a[i] == b[i] or a[i] == b[i] - 1:
            continue
        else:
            return False

    return True

a = [1, 1, 2, 3, 4, 5, 6]
b = [2, 3, 3, 3, 5, 5, 7]


print(borningArray(a, b))