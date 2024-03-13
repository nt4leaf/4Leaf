# Đây là List Comprehension.
even_number = [i for i in range(0, 9, 2)]
print(even_number)

# constructor List.
name = list("My name is Tuan Nguyen")
print(name)

# Toán tử với list: +, *, in,...
# Indexing với list, điểm đặc biệt là ta có thể thay đổi từng phần từ trong list.
# Ma trận.
matrix = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
for row in matrix:
    print(row)
print(matrix[1][1])

# Khi gán list này trực tiếp cho list khác, có nghĩa hai biến cùng tham chiếu tới cùng 1 dữ liệu.
# Để kiểm tra có tham chiếu cùng 1 dữ liệu/ đối tượng không, dùng toán tử 'is'.
# Dùng toán tử is khi so sánh các list, hay None.
# Có các cách gán gián tiếp:
a = [0, 1, 2]
b = a[:]
c = list(a)
d = a.copy()
print(a is b)
print(a is c)
print(a is d)

# Khi gán ma trận cho ma trận bằng gián tiếp, các list con vẫm cùng tham chiếu tới 1 dữ liệu.
# Cách xử lý là sử dụng vòng lặp...
