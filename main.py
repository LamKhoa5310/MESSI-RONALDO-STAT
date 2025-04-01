class HinhChuNhat:
    def __init__(self, chieu_dai, chieu_rong):
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong

    # Phương thức tính diện tích
    def tinh_dien_tich(self):
        return self.chieu_dai * self.chieu_rong

    # Phương thức tính chu vi
    def tinh_chu_vi(self):
        return 2 * (self.chieu_dai + self.chieu_rong)

# Tạo đối tượng HinhChuNhat và tính diện tích, chu vi
hcn = HinhChuNhat(5, 3)
print("Diện tích:", hcn.tinh_dien_tich())  # Output: 15
print("Chu vi:", hcn.tinh_chu_vi())        # Output: 16


class Person {
public $name;

public function sayHello() {
echo "Hello, my name is ".$this->name;
}
}

$person = new
Person();
$person->name = "John";
$person->sayHello();
