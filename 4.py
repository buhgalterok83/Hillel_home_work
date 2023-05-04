def custom_map(function, *sequences):
    length = min(map(len, sequences))
    if len(sequences) == 1:
        return [function(sequences[0][i]) for i in range(length)]
    else:
        return [function(*[seq[i] for seq in sequences]) for i in range(length)]



result1 = custom_map(sum, [[1, 2, 3], [4, 5]])
print(result1)

result2 = custom_map(lambda x, y: x + y, [1, 2, 3, 4], (3, 4, 4, 4, 4, 4, 44))
print(result2)
