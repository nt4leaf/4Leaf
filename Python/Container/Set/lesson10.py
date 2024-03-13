# Set không chứa nhiều hơn 1 phần tử trùng lặp
list_01 = [0, 1, 1, 2, 3, 5, 8, 11]
set_02 = set(list_01)
print(set_02)

# Set Comprehension
set_03 = {i for i in range(5)}
print(set_03)

# Constructor Set
name = "Nguyen Tuan"
set_04 = set(name)
print(set_04)

# Các phương thức đối sánh
# Phương thức union "|"
print(set_02.union(set_03))
# Phương thức intersection "&"
print(set_02.intersection(set_03))
# Phương thức difference "-"
print(set_02.difference(set_03))
# Phương thức