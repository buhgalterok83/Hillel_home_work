multi_string = "Hello all. Here's pretty cold and hot. Choose yourself."

sentences = multi_string.split('.')
word_counts = []

for sentence in sentences:
    words = sentence.strip().split(' ')
    count = len(words)
    if count != 1 or words[0] != '':
        word_counts.append(count)

print(word_counts)