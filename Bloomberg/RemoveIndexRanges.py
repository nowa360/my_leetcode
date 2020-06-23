def remove_range(arr, rang):
    pos = [0 for _ in xrange(len(arr))]

    for x, y in rang:

        if x < len(pos):
            pos[x] = 1

        if y < len(pos):
            pos[y] = -1

    res = []
    tracker = 0
    for i, num in enumerate(arr):

        tracker += pos[i]
        if tracker > 0:
            continue
        else:
            res.append(num)

    return res


arr = [-8, 3, -5, 1, 51, 56, 0, -5, 29, 43, 78, 75, 32, 76, 73, 76]
rang = [[5, 8], [10, 13], [3, 6], [20, 25]]
# expects [-8, 3, -5, 29, 43, 76, 73, 76]
print(remove_range(arr, rang))
