lst = [1, 2, 3, 5]

# n = len(lst) + 1

# missing = (n * (n + 1)) // 2 - sum(lst)

# print(missing)





expected = set(range(1, 11))

actual = set(lst)

missing = expected - actual

print(missing)