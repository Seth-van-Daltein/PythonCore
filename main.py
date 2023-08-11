print('Hello, Python')

a = str(input('Enter a: '))

a = int(a)
print(a)

b = a
print(b)

c = id(b)
print(c)

name = str(input('Enter name: '))
surname = str(input('Enter surname: '))
age = int(input('Enter age: '))

print(f'Привіт {name} {surname}!!!')
print(f'Тобі зараз {age} років!')
