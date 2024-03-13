# Các cách định dạng chuỗi.

# Định dạng bằng toán tử %
inform = "my name is %s. I'm %d years old." % ('Tuan Nguyen', 20)
print(inform)

# Định dạng bằng chuỗi f-string
name = 'Tuan Nguyen'
ages = 20
s1 = f"My name is {name}. I'm {ages} years old."
print(s1)

# Để bỏ qua cặp ký tự {} trong chuỗi, ta sử dụng cặp ký tự {{}}
variable = 'Three'
s2 = f'1: {{one}}, 2: {{two}}, 3: {variable}'
print(s2)

# Định dạng bằng phương thức format
s3 = 'a:{2}, b:{1}, c:{0}, d:{1}'.format('one', 'two', 'three')
print(s3)
s4 = 'a:{one}, b:{two}, c:{one}'.format(one='1', two='2')
print(s4)
# Thao tác căn lề bằng phương thức format {:(c)^(n)}
row_1 = '+ {:-<12} + {:-^30} + {:->12} +'.format('', '', '')
row_2 = '| {:<12} | {:^30} | {:>12} |'.format('ID', 'Ho va ten', 'Noi sinh')
row_3 = '| {:<12} | {:^30} | {:>12} |'.format('042204004789', 'Nguyen Pham Quoc Tuan', 'Ha Tinh')
print(row_1)
print(row_2)
print(row_3)