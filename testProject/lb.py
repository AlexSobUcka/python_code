def remove_line_breaks(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    return text.replace('\n', '')

file_path = 'text.txt'
text_without_line_breaks = remove_line_breaks(file_path)
print(text_without_line_breaks)