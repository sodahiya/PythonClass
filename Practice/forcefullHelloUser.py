name = ''
while not name:
    name = input('Please enter your name: ')
    if name.isspace():
        name = None

print('Hello, {}!'.format(name))