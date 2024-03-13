# Hashable
number1 = 4
number2 = 3.14
str1 = 'Tuan Nguyen'
tuple1 = (0, 1, 2, 3)

# Unhashable
list1 = [0, 1, 2, 3]
set1 = {0, 1, 2, 3}
dict1 = {'a': 1, 'b': 2, 'c': 3}

# Lưu ý, không nên sử dụng toán tử + với Unhashable objecct
# Thay vào đó sử dụng toán tử += hay phương thức .append(), .__iadd__()

'''
Khi bạn khởi tạo một giá trị, nó sẽ được lưu trong bộ nhớ máy tính.
Khi khởi tạo 1 hashable object, Python sẽ cung cấp một vùng bộ nhớ vừa đủ để lưu trữ dữ liệu. Tiết kiệm bộ nhớ của bạn.
Khi dùng thay đổi nội dung của 1 hashable object , Python sẽ phải tìm một vùng nhớ mới để thay thế.

Còn khi khởi tạo 1 unhashable object, Python sẽ cung cấp một vùng nhớ dư, để lưu trữ thêm dữ liệu sau này.
'''

