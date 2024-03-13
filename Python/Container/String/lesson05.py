import keyword
# Các phương pháp tách chuỗi
name = 'My name is Tuan Nguyen'
lst1 = name.split(None, 3)
print(lst1)
lst2 = name.rsplit(None, 2)
print(lst2)
lst3 = ('Hello World\n' + name).splitlines()
print(lst3)
lst4 = name.partition('is')
print(lst4)
lst5 = name.rpartition('I')
print(lst5)

# Các phương thức tiện ích
number = name.count('y')
print(number)
print(name.startswith('name', 3, None))
print(name.endswith('Tuan', None, -7))
print(name.find('n', None, None))
print(name.rfind('n', None, None))
print(name.index('Nguyen', None, None))
print(name.rindex('Tuan', None, None))

# Các phương thức xác thực
print(name.islower())
print(name.isupper())
print(name.istitle())
locate = 'HaTinh'
print(locate.isidentifier())
birth = '08032004'
print(birth.isdigit())
nothing = '\t \n'
print(nothing.isspace())
print(keyword.iskeyword('def'))
