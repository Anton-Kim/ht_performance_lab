def iterator(length, start):
    i, counter = [], start
    while len(i) < length:
        i.append(counter)
        counter = counter + 1 if counter < length else 1
    return i


n, m = map(int, input().split())
it, res = iterator(n, 1), [1]
if n == m:
    print(1)
else:
    step = [1, it[(m - 1) % len(it)]]
    while step[-1] != 1:
        it = iterator(n, step[-1])
        step = [step[-1], it[(m - 1) % len(it)]]
        res.append(step[0])

print(*res, sep='')
