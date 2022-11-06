
def sed(template_str, change_str, filename_1, filename_2):
    """
    Функция sed() принимает в качестве аргументов строку шаблона,
    строку замены и два имени файлов; программа считывает содержимое
    первого файла и записывает его во второй файл (создавая его при
    необходимости). Если строка шаблона встречается где-либо в файле, ее
    следует заменяет строка замены
    """

    try:
        text = open(filename_1, 'r')
        text_copy = open(filename_2, 'w')
        for line in text.readlines():
            if line == template_str:
                line = change_str
            text_copy.write(line)
    except:
        print('error')


sed('tttt\n', 'new line\n', 'test12.txt', 'test2.txt')
