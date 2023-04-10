s = "aab qq c badcc a qqqqqaqqqqaa tpara"

words = []
for word in s.split():
    if word.lower().count('a') == 2:
        words.append(word)

result = ' '.join(words).title()

print(result)