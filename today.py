is_pressed = False  # Nút bấm KHÔNG được nhấn

# Dùng not để kiểm tra: "Nếu nút bấm KHÔNG ĐƯỢC NHẤN"
if not is_pressed:
    print("Nút chưa được bấm! Đang chờ người dùng...")
else:
    print("Nút đã được bấm!")

co_tai_khoan = True
mat_khau_dung = False

if co_tai_khoan:
    if mat_khau_dung:
        print("Đăng nhập thành công")
    else:
        print("Sai mật khẩu")
else:
    print("Tài khoản không tồn tại")