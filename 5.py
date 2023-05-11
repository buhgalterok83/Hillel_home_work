def custom_zip(*sequences, full=False, default=None):
    if not full:
        length = min(len(seq) for seq in sequences)
    else:
        length = max(len(seq) for seq in sequences)
    result = []
    for i in range(length):
        values = []
        for seq in sequences:
            if i < len(seq):
                values.append(seq[i])
            elif default is not None:
                values.append(default)
            else:
                values.append(None)
        result.append(tuple(values))
    return result


seq1 = [1,  2, 3, 4, 5]
seq2 = [9,   8, 7]

print(custom_zip(seq1, seq2))
print(custom_zip(seq1, seq2, full=True))
