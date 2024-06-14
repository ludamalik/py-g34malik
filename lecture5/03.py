from pathlib import Path

file_path = Path('your_file.txt')

text = file_path.read_text()

num_lines = text.count('\n') + 1
num_words = len(text.split())
num_chars = len(text)

print(f"Number of lines: {num_lines}")
print(f"Number of words: {num_words}")
print(f"Number of characters: {num_chars}")
