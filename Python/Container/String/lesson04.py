""" Đây là phương thức dùng để encode một chuỗi với phương thức mã hóa mặc định là utf-8.
Còn về errors mặc định là strict, có thông báo lỗi hiện lên nếu có vấn đề xuất hiện trong quá trình encode chuỗi.
Một số giá trị ngoài strict là ignore, replace, xmlcharrefreplace. """
inform = 'Nguyễn Tuấn'
s1 = inform.encode(encoding='utf-8', errors='strict')
print(s1)
s2 = s1.decode()
print(s2)

#  Trả về một chuỗi bằng cách nối các phần tử trong iterable bằng kí tự nối.
#  Một iterable có thể là một tuple, list,… hoặc là một iterator.
number = ', '.join(['1', '2', '3', '4'])
print(number)
s3 = 'like'
s4 = 'love'
print('I like you'.replace(s3, s4))

# Trả về một chuỗi với phần đầu và phần đuôi của chuỗi được bỏ đi các kí tự chars.
print('abactoiyeuemcab'.strip('abc'))
# Tương tự có rstrip() và lstrip()

# Trả về một chuỗi với phần đầu hoặc phần đuôi của chuỗi được bỏ đi 1 kí tự char.
msg = 'aanhyeuemnhieuu'.removeprefix('a').removesuffix('u')
print(msg)
