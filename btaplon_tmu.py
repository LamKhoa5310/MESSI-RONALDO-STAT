DS_KH = []

def input_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Lỗi! Mời nhập lại.")

def input_customer_info():
    while True:
        makh = input("Mã khách hàng: ")
        existing_customer = [customer for customer in DS_KH if customer[0].lower() == makh.lower()]
        if existing_customer:
            print("Mã khách hàng đã tồn tại. Vui lòng nhập lại.")
        else:
            break

    name = input("Tên khách hàng: ")
    age = input_int("Tuổi: ")
    address = input("Địa chỉ: ")
    phone = input_int("SĐT: ")
    email = input("Email: ")
    return [makh, name, age, address, phone, email]

def print_customer_list():
    print("=" * 100)
    print("STT Mã KH Tên KH                Tuổi Địa chỉ                   SĐT          Email   ")
    for i, customer in enumerate(DS_KH):
         print("{}   {}  {}       {}   {} {}    {}".format(i + 1, *customer))

def add_customer():
    while True:
        num_customer = input_int("Nhập số lượng khách hàng cần thêm: ")
        if num_customer > 0:
            break
    for _ in range(num_customer):
        print("=" * 60)
        customer_info = input_customer_info()
        DS_KH.append(customer_info)
    print_customer_list()

def delete_customer():
    print()
    if not DS_KH:
        print("Danh sách trống!")
        return
    print_customer_list()
    while True:
        search_makh = input("Nhập mã khách hàng muốn xóa: ")
        matching_customer = []
        for i, customer in enumerate(DS_KH):
            if search_makh.lower() == customer[0].lower():
                matching_customer.append((i, customer))
        if matching_customer:
            print("Bạn muốn xóa khách hàng '{}'".format(matching_customer[0][1][0]))
            index = matching_customer[0][0]
            DS_KH.pop(index)
            break
        else:
            print("Không tìm thấy khách hàng với mã '{}'! Mời nhập lại.".format(search_makh))
    print("\n======= Danh sách khách hàng sau khi chỉnh sửa =======")
    print_customer_list()

def update_customer():
    print()
    if not DS_KH:
        print("Danh sách trống!")
        return
    print_customer_list()
    while True:
        search_makh = input("Nhập mã khách hàng muốn cập nhật thông tin: ")
        matching_customer = []
        for i, customer in enumerate(DS_KH):
            if search_makh.lower() == customer[0].lower():
                matching_customer.append((i, customer))
        if matching_customer:
            print("Bạn muốn sửa thông tin của khách hàng '{}'".format(matching_customer[0][1][0]))
            index = matching_customer[0][0]
            break
        else:
            print("Không tìm thấy khách hàng với mã '{}'! Mời nhập lại.".format(search_makh))
    while True:
        print("Thông tin bạn muốn sửa (1-Mã KH, 2-Tên, 3-Tuổi, 4-Địa chỉ, 5-SĐT, 6-Email):")
        option = input_int("Lựa chọn (1-6): ")
        if 1 <= option <= 6:
            info_labels = ["Mã KH", "Tên", "Tuổi", "Địa chỉ", "SĐT", "Email"]
            print("Vậy bạn muốn sửa {}: {}".format(info_labels[index], info_labels[option - 1]))
            new_info = input("Nhập thông tin thay đổi: ")
            DS_KH[index][option - 1] = new_info
            break
        else:
            print("Lỗi! Mời nhập lại.")
    print("\n======= Danh sách khách hàng sau khi chỉnh sửa =======")
    print_customer_list()


def search_customer():
    print("=" * 60)
    search_makh = input("Tìm bằng mã khách hàng: ")
    matching_customer = []
    for customer in DS_KH:
        if search_makh.lower() == customer[0].lower():
            matching_customer.append(customer)
    print("Thông tin tìm kiếm được: {}".format(matching_customer))
    print("=" * 60)

def menu():
    print("""
=============== QUẢN LÍ KHÁCH HÀNG ================
=  * Bắt buộc ( Nhập khách hàng vào danh sách     =
=    trước khi tiến hành các thao tác khác )      =
=  1. Thêm khách hàng vào danh sách               =
=  2. Xóa khách hàng khỏi danh sách               =               
=  3. Cập nhật thông tin khách hàng               =
=  4. Tìm kiếm thông tin khách hàng               =
=  5. Exit                                        =
===================================================""")

    while True:
        option = input_int("Chọn theo số (1-5) để tiếp tục tiến trình: ")
        if option == 1:
            add_customer()
        elif option == 2:
            delete_customer()
        elif option == 3:
            update_customer()
        elif option == 4:
            search_customer()
        elif option == 5:
            break
        else:
            print("Lỗi! Mời nhập lại.")

menu()


