with open('sentences.txt', 'r') as file:
    lines = file.read().splitlines()

new_sentence = "If Peter Piper picked a peck of pickled peppers."

lines.insert(2, new_sentence)

with open('modified_sentences.txt', 'w') as file:
    for line in lines:
        file.write(line + '\n')
