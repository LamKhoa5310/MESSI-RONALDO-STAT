import sqlite3

# Kết nối cơ sở dữ liệu SQLite
def connect_db():
    conn = sqlite3.connect('product_management.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                      id TEXT PRIMARY KEY,
                      name TEXT,
                      brand TEXT,
                      price INTEGER,
                      quantity INTEGER,
                      description TEXT)''')
    conn.commit()
    return conn


def add_product():
    conn = connect_db()
    cursor = conn.cursor()

    # Hàm phụ để lấy đầu vào từ người dùng và kiểm tra
    def get_input(prompt, is_integer=False, check_exists=False):
        while True:
            value = input(f"{prompt} (hoặc nhập '0' để quay lại menu): ")
            if value.lower() == '0':
                return None
            if check_exists and is_id_exists(value):
                print("Lỗi: ID sản phẩm đã tồn tại. Vui lòng nhập ID khác.")
            elif is_integer:
                try:
                    value = int(value)
                    return value
                except ValueError:
                    print("Lỗi: Vui lòng nhập một số nguyên.")
            elif value.strip() == "":
                print("Lỗi: Trường này không được để trống.")
            else:
                return value

    # Nhập các thông tin sản phẩm
    product_id = get_input("Nhập ID sản phẩm", check_exists=True)
    if product_id is None:
        return
    name = get_input("Nhập tên sản phẩm")
    if name is None:
        return
    brand = get_input("Nhập nhà cung cấp")
    if brand is None:
        return
    price = get_input("Nhập giá", is_integer=True)
    if price is None:
        return
    quantity = get_input("Nhập số lượng", is_integer=True)
    if quantity is None:
        return
    description = get_input("Nhập mô tả")
    if description is None:
        return

    # Thêm sản phẩm vào cơ sở dữ liệu
    cursor.execute("INSERT INTO products (id, name, brand, price, quantity, description) VALUES (?, ?, ?, ?, ?, ?)",
                   (product_id, name, brand, price, quantity, description))
    conn.commit()
    conn.close()
    print("Thêm sản phẩm thành công.")


def edit_product():
    def get_positive_integer(prompt):
        while True:
            try:
                value = int(input(prompt))
                if value < 0:
                    print("Lỗi: Giá trị phải là số không âm. Vui lòng nhập lại.")
                    continue
                return value
            except ValueError:
                print("Lỗi: Giá trị phải là số nguyên. Vui lòng nhập lại.")

    conn = connect_db()
    cursor = conn.cursor()

    product_id = input("Nhập ID sản phẩm cần sửa: ")
    # Truy vấn sản phẩm trực tiếp và kiểm tra kết quả
    cursor.execute("SELECT * FROM products WHERE id=?", (product_id,))
    product = cursor.fetchone()

    if not product:
        print("Lỗi: ID sản phẩm không tồn tại.")
        return
    print("\nThông tin sản phẩm hiện tại:")
    print(f"1. Tên sản phẩm: {product[1]}")
    print(f"2. Nhà cung cấp: {product[2]}")
    print(f"3. Giá: {product[3]}")
    print(f"4. Số lượng: {product[4]}")
    print(f"5. Mô tả: {product[5]}")
    name, brand, price, quantity, description = product[1], product[2], product[3], product[4], product[5]

    while True:
        choice = input("Chọn mục cần sửa (hoặc nhập '0' để lưu và thoát): ")
        if choice == "1":
            name = input("Nhập tên sản phẩm mới: ")
        elif choice == "2":
            brand = input("Nhập nhà cung cấp mới: ")
        elif choice == "3":
            price = get_positive_integer("Nhập giá mới: ")
        elif choice == "4":
            quantity = get_positive_integer("Nhập số lượng mới: ")
        elif choice == "5":
            description = input("Nhập mô tả mới: ")
        elif choice == "0":
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

    # Cập nhật thông tin sản phẩm trong cơ sở dữ liệu
    cursor.execute('''UPDATE products SET name=?, brand=?, price=?, quantity=?, description=? 
                      WHERE id=?''', (name, brand, price, quantity, description, product_id))
    conn.commit()
    conn.close()
    print("Cập nhật sản phẩm thành công.")


# Xóa sản phẩm
def delete_product():
    conn = connect_db()
    cursor = conn.cursor()

    while True:
        product_id = input("Nhập ID sản phẩm cần xóa (hoặc nhập '0' để quay lại menu): ")
        if product_id.lower() == '0':
            return

        # Kiểm tra ID sản phẩm có tồn tại trong cơ sở dữ liệu không
        cursor.execute("SELECT * FROM products WHERE id=?", (product_id,))
        product = cursor.fetchone()

        if not product:
            print("Lỗi: ID sản phẩm không tồn tại. Vui lòng nhập lại.")
        else:
            # Nếu tồn tại, tiến hành xóa
            cursor.execute("DELETE FROM products WHERE id=?", (product_id,))
            conn.commit()
            conn.close()
            print("Xóa sản phẩm thành công.")
            break  # Thoát khỏi vòng lặp sau khi xóa thành công


# Tìm kiếm sản phẩm
def search_product():
    conn = connect_db()
    cursor = conn.cursor()

    while True:
        search_query = input("Nhập ID, tên hoặc nhà cung cấp sản phẩm (hoặc nhập '0' để quay lại menu): ")
        if search_query.lower() == '0':
            conn.close()
            return

        # Chuyển tất cả về chữ thường khi tìm kiếm để không phân biệt chữ hoa chữ thường
        cursor.execute("SELECT * FROM products WHERE LOWER(id)=? OR LOWER(name)=? OR LOWER(brand)=?",
                       (search_query.lower(), search_query.lower(), search_query.lower()))
        products = cursor.fetchall()

        if products:
            for product in products:
                print(f"ID: {product[0]}")
                print(f"Tên SP: {product[1]}")
                print(f"Nhà cung cấp: {product[2]}")
                print(f"Giá: {product[3]}")
                print(f"Số lượng: {product[4]}")
                print(f"Mô tả: {product[5]}")
            break  # Thoát vòng lặp nếu tìm thấy sản phẩm
        else:
            print("Không tìm thấy sản phẩm. Vui lòng nhập lại thông tin tìm kiếm.")


# Theo dõi hàng tồn kho
def track_inventory():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products WHERE quantity < 10")
    low_stock_products = cursor.fetchall()
    conn.close()

    if low_stock_products:
        print("Các sản phẩm có số lượng dưới 10:")
        for product in low_stock_products:
            print(f"ID: {product[0]}")
            print(f"Tên SP: {product[1]}")
            print(f"Nhà cung cấp: {product[2]}")
            print(f"Giá: {product[3]}")
            print(f"Số lượng: {product[4]}")
            print(f"Mô tả: {product[5]}")
            print("-" * 40)  # Dòng ngăn cách giữa các sản phẩm
    else:
        print("Không có sản phẩm nào dưới mức cảnh báo.")


# Hàm kiểm tra sự tồn tại của ID sản phẩm
def is_id_exists(product_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT 1 FROM products WHERE id=?", (product_id,))
    result = cursor.fetchone()
    conn.close()
    return result is not None


# Menu chính
def main():
    while True:
        print("1. Thêm sản phẩm")
        print("2. Sửa sản phẩm")
        print("3. Xóa sản phẩm")
        print("4. Tìm kiếm sản phẩm")
        print("5. Theo dõi hàng tồn kho")
        print("0. Thoát")

        choice = input("Chọn một tùy chọn: ")

        if choice == "1":
            add_product()
        elif choice == "2":
            edit_product()
        elif choice == "3":
            delete_product()
        elif choice == "4":
            search_product()
        elif choice == "5":
            track_inventory()
        elif choice == "0":
            break
        else:
            print("Tùy chọn không hợp lệ. Vui lòng thử lại.")


if __name__ == "__main__":
    main()
