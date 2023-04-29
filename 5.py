import re

def generate_sentence(text: str) -> str:
    sentences = [s.strip() for s in re.split('[.?!]', text) if s.strip()]
    words = [s.split()[0].lower() for s in sentences]
    sentence = ' '.join(words)
    sentence = sentence.capitalize()
    sentence += '.'
    return sentence

text = """Happy New Year! Wish you good luck.
Please write me how are you doing? Goodbye...
"""
print(generate_sentence(text)) 
