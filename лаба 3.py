'''def read_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
    return content
print(read_file('example.txt'))'''
'''def read_file(filename):
    with open('example.txt', 'r') as file:
        for line in file:
            return line
print(read_file('example.txt'))
'''def read_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
    return content

def read_line(filename):
    with open(filename, 'r') as file:
        for line in file:
            return line

print('выберите тип чтения: "2 - построчное" "1 - цельное"')
r1=int(input())
try:
    if r1 == 1:
        print(read_file('example.txt'))
    elif r1 == 2:
        print(read_line('example.txt'))
    else:
        print("ошибка")
except FileNotFoundError:
    print('файл не найден')

def write_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)
    return 'ALL GOOD'
print('введите данные:')
text = input()
print(write_file('user_input.txt', text))
'''
'''def add_to_file(filename):
    with open(filename, 'a') as file:
        content=file.write(f'\n{input()}')
    return content
print('введите данные:')
print(add_to_file('user_input.txt'))'''