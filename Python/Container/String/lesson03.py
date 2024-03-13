# Các phương thức biến đổi chuỗi

# Trả về một chuỗi với kí tự đầu tiên được viết hoa và viết thường tất cả những kí tự còn lại.
s1 = 'hello world'
print(s1.capitalize())
# Trả về một chuỗi với tất cả các kí tự được chuyển thành các kí tự viết hoa
s2 = 'hello'
print(s2.upper())
# Trả về một chuỗi với tất cả các kí tự được chuyển thành các kí tự viết thường
s3 = 'TUAN NGUYEN'
print(s3.lower())
# Đảo ngược ký tự viết thường và ký tự viết hoa
s4 = 'Hi there'
print(s4.swapcase())
# Trả về một chuỗi với định dạng tiêu đề
s5 = 'this is a title'
print(s5.title())

# Các phương thức định dạng:
s6 = 'Hello'
print(s6.center(15, '-'))
print(s6.rjust(15, '-'))
print(s6.ljust(15, '-'))
