# Các phương thức tiện ích.
student_id = [int(i) for i in '22010508']
print(student_id)
print(student_id.count(2))
print(student_id.index(1))
msg = student_id.copy()
print(msg is student_id)
# Phương thức clear tác động lên vùng dữ liệu. còn gán [] thì không.
msg.clear()
print(msg)

# Các phương thức cập nhật.
# Phương thức append, không được phép append chính nó.
msg.append(2024)
print(msg)
# Phương thức extend.
msg.extend((3, 8))
print(msg)
msg.insert(0, 'my next birthday')
print(msg)
# Phương thức pop và remove loại bỏ phần tử khỏi chuỗi.

# Các phương thức xử lí.
msg.reverse()
print(msg)
student_id.sort()
print(student_id)