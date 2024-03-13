# Đây là tuple(Generator Expression)
even_number = tuple(i for i in range(0, 9, 2))
print(even_number)
# Các toán từ và phương thức của tuple tương tự list.
'''
Tuple khác List ở chỗ Tuple không cho phép bạn sửa chữa nội dung, còn List thì có. 
Vì đặc điểm đó, Tuple mạnh hơn List ở những điểm sau:
    Tốc độ truy xuất của Tuple nhanh hơn so với List
    Dung lượng chiếm trong bộ nhớ của Tuple nhỏ hơn so với List
    Bảo vệ dữ liệu của bạn sẽ không bị thay đổi
    Có thể dùng làm key của Dictonary. 
    Điều mà List không thể vì List là unhash object.
'''