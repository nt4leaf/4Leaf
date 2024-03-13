# Đây là 1 chuỗi có chứa Escape Sequence \t
print("\tSay Hello")
# Đây là 1 chuỗi bỏ qua các Escape Sequence
print(r"\\tHello World")
# Bằng cách bổ sung thêm 1 dấu \ vào trước mỗi Escape Sequence.
print("\\\\tHello World")
# Phương pháp indexing, với a là điểm bắt đầu, b-1 là điểm kết thúc, c là bước nhảy.
s1 = "Hello World"
a = 0
b = len(s1)
c = 2
print(s1[a:b:c])
# Cách chuyển một số thực dạng chuỗi sang dạng int. Gián tiếp chuyển đổi bằng float.
s2 = "3.14"
s2 = int(float(s2))
print(s2)
# Chuyển ngược lại từ số sang chuỗi ta dùng hàm str().
s3 = str(123456789)
print(type(s3))
# Để có thể thay đổi nội dung chuỗi, ta không thể dùng phương pháp indexing.
s4 = "Hello World"
s4 = s4[:6] + "Future"
print(s4)
