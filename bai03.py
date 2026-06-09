# (1) Phân tích và thiết kế giải pháp
# Input/Output cho từng hàm:
# - display_students(student_list): Input list học viên, Output in ra danh sách hoặc thông báo trống.
# - validate_score(score_input): Input chuỗi nhập điểm, Output True/False (hợp lệ hay không).
# - add_student(student_list): Input list học viên, Output thêm học viên mới vào list nếu hợp lệ.
# - find_student_by_id(student_list, student_id): Input list và mã HV, Output index hoặc None.
# - update_score(student_list): Input list học viên, Output cập nhật điểm cho HV theo mã.
# - get_rank(average_score): Input điểm trung bình, Output chuỗi xếp loại.
# - evaluate_students(student_list): Input list học viên, Output in ra ĐTB và xếp loại.
#
# Giải pháp:
# - Tách nhỏ thành nhiều hàm giúp code rõ ràng, dễ bảo trì, dễ kiểm thử.
# - Các hàm phụ trợ (validate_score, find_student_by_id, get_rank) tái sử dụng nhiều lần, tránh lặp code.
# - Vòng lặp chính chỉ điều hướng menu, không chứa logic nghiệp vụ dài dòng.
#
# Edge cases:
# - Trùng mã HV khi thêm mới → kiểm tra trước bằng find_student_by_id.
# - Nhập điểm không hợp lệ → validate_score bắt lỗi bằng if, yêu cầu nhập lại.
# - Nhập sai lựa chọn menu → báo lỗi và yêu cầu nhập lại.
# - Tên học viên rỗng → yêu cầu nhập lại.

# (2) Triển khai code

students = [
    {
        "student_id": "RA001",
        "name": "Nguyễn Văn A",
        "math_score": 8.5,
        "english_score": 7.0
    },
    {
        "student_id": "RA002",
        "name": "Trần Thị B",
        "math_score": 9.0,
        "english_score": 9.5
    }
]

def display_students(student_list):
    """Hiển thị danh sách học viên"""
    if not student_list:
        print("Danh sách học viên hiện đang trống.")
    else:
        for i, st in enumerate(student_list, start=1):
            print(f"{i}. Mã: {st['student_id']} | Tên: {st['name']} | Toán: {st['math_score']} | Anh: {st['english_score']}")

def validate_score(score_input):
    """Kiểm tra điểm hợp lệ (0-10)"""
    if score_input.replace('.', '', 1).isdigit():  # kiểm tra có phải số (cho phép số thực)
        score = float(score_input)
        if 0 <= score <= 10:
            return True
        else:
            print("Điểm không hợp lệ, phải là số từ 0 đến 10.")
            return False
    else:
        print("Điểm không hợp lệ, phải là số từ 0 đến 10.")
        return False

def add_student(student_list):
    """Thêm học viên mới"""
    student_id = input("Nhập mã học viên: ").strip().upper()
    if find_student_by_id(student_list, student_id) is not None:
        print("Mã học viên đã tồn tại, vui lòng nhập mã khác!")
        return
    name = input("Nhập tên học viên: ").strip().title()
    if not name:
        print("Tên học viên không được để trống!")
        return
    math_input = input("Nhập điểm Toán: ")
    if not validate_score(math_input): return
    english_input = input("Nhập điểm Anh: ")
    if not validate_score(english_input): return
    student_list.append({
        "student_id": student_id,
        "name": name,
        "math_score": float(math_input),
        "english_score": float(english_input)
    })
    print("Thêm học viên thành công!")

def find_student_by_id(student_list, student_id):
    """Tìm học viên theo mã"""
    for idx, st in enumerate(student_list):
        if st["student_id"] == student_id:
            return idx
    return None

def update_score(student_list):
    """Cập nhật điểm thi theo mã học viên"""
    student_id = input("Nhập mã học viên cần cập nhật: ").strip().upper()
    idx = find_student_by_id(student_list, student_id)
    if idx is None:
        print(f"Không tìm thấy học viên mang mã {student_id}!")
        return
    math_input = input("Nhập điểm Toán mới: ")
    if not validate_score(math_input): return
    english_input = input("Nhập điểm Anh mới: ")
    if not validate_score(english_input): return
    student_list[idx]["math_score"] = float(math_input)
    student_list[idx]["english_score"] = float(english_input)
    print("Cập nhật điểm thành công!")

def get_rank(average_score):
    """Xếp loại học lực theo điểm trung bình"""
    if average_score >= 8.0:
        return "Giỏi"
    elif average_score >= 6.5:
        return "Khá"
    elif average_score >= 5.0:
        return "Trung bình"
    else:
        return "Yếu"

def evaluate_students(student_list):
    """Đánh giá học lực toàn bộ học viên"""
    for st in student_list:
        avg = (st["math_score"] + st["english_score"]) / 2
        rank = get_rank(avg)
        print(f"Mã: {st['student_id']} | Tên: {st['name']} | ĐTB: {avg:.2f} | Xếp loại: {rank}")

# Vòng lặp chính
while True:
    print("\n===== HỆ THỐNG QUẢN LÝ ĐIỂM THI RIKKEI ACADEMY =====")
    print("1. Hiển thị danh sách học viên")
    print("2. Thêm học viên mới")
    print("3. Cập nhật điểm thi theo mã học viên")
    print("4. Đánh giá học lực của toàn bộ học viên")
    print("5. Thoát chương trình")
    choice = input("Nhập lựa chọn của bạn: ")
    if choice == "1":
        display_students(students)
    elif choice == "2":
        add_student(students)
    elif choice == "3":
        update_score(students)
    elif choice == "4":
        evaluate_students(students)
    elif choice == "5":
        print("Cảm ơn bạn đã sử dụng hệ thống!")
        break
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
