def remove_line_breaks(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    text = text.replace('\n', ' ')
    text = text.replace('  ', ' ')
    return text

file_path = 'text.txt'
text_without_line_breaks = remove_line_breaks(file_path)
print(text_without_line_breaks)

with open("mag.txt", "a") as file:
    file.write(text_without_line_breaks + '\n')