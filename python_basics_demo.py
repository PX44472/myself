# Python基础知识示例代码：数据类型、流程控制和类

# ========== 1. Python数据类型 ==========
print("\n===== Python数据类型示例 =====")

# 基本数据类型
basic_types = {
    "整数(int)": 42,
    "浮点数(float)": 3.14159,
    "字符串(str)": "Hello, Python!",
    "布尔值(bool)": True,
    "空值(None)": None
}

for type_name, value in basic_types.items():
    print(f"{type_name}: 值 = {value}, 类型 = {type(value)}")

# 复合数据类型 - 列表(list)
numbers_list = [1, 2, 3, 4, 5]
mixed_list = [1, "two", 3.0, [4, 5]]  # 列表可以包含不同类型的元素
print(f"\n列表(list): {numbers_list}")
print(f"列表长度: {len(numbers_list)}")
print(f"列表索引访问: {numbers_list[0]}, {numbers_list[-1]}")  # 正向索引和反向索引

# 复合数据类型 - 元组(tuple) - 不可变的列表
coordinates = (10, 20, 30)
print(f"\n元组(tuple): {coordinates}")
print(f"元组解包: x={coordinates[0]}, y={coordinates[1]}, z={coordinates[2]}")

# 复合数据类型 - 集合(set) - 无序且不包含重复元素
unique_numbers = {1, 2, 3, 4, 5, 3, 2, 1}  # 重复元素会被自动去除
print(f"\n集合(set): {unique_numbers}")
print(f"集合添加元素: {unique_numbers.add(6)} -> {unique_numbers}")

# 复合数据类型 - 字典(dict) - 键值对的集合
student_info = {
    "name": "张三",
    "age": 20,
    "major": "计算机科学",
    "courses": ["Python", "数据结构", "操作系统"]
}
print(f"\n字典(dict): {student_info}")
print(f"通过键访问值: 姓名 = {student_info['name']}, 年龄 = {student_info.get('age')}")

# ========== 2. 流程控制 ==========
print("\n\n===== Python流程控制示例 =====")

# 条件语句 (if-elif-else)
score = 85
print(f"\n条件语句示例 - 成绩等级判定 (分数: {score}):")
if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 70:
    print("中等")
elif score >= 60:
    print("及格")
else:
    print("不及格")

# 循环语句 - for循环
print("\nfor循环示例 - 遍历列表:")
for number in numbers_list:
    print(f"数字: {number}, 平方: {number ** 2}")

# for循环与range()函数
sum_result = 0
for i in range(1, 11):
    sum_result += i
print(f"\n1到10的和: {sum_result}")

# 循环语句 - while循环
count = 1
factorial = 1
print("\nwhile循环示例 - 计算5的阶乘:")
while count <= 5:
    factorial *= count
    count += 1
print(f"5的阶乘: {factorial}")

# 循环控制语句 - break和continue
evens_sum = 0
print("\n循环控制语句示例 - 计算10以内偶数的和:")
for i in range(1, 11):
    if i % 2 == 1:
        continue  # 跳过奇数
    evens_sum += i
    if evens_sum > 20:
        break  # 当和超过20时停止循环
print(f"偶数和: {evens_sum}")

# 列表推导式 - 一种简洁的循环构建列表的方式
squares = [x ** 2 for x in range(1, 6)]
print(f"\n列表推导式 - 1到5的平方: {squares}")

even_squares = [x ** 2 for x in range(1, 11) if x % 2 == 0]
print(f"列表推导式 - 1到10中的偶数的平方: {even_squares}")

# ========== 3. 类(Class) ==========
print("\n\n===== Python类(Class)示例 =====")

# 定义一个简单的类
class Person:
    # 类变量
    species = "Homo sapiens"
    
    # 初始化方法（构造函数）
    def __init__(self, name, age, occupation=None):
        # 实例变量
        self.name = name
        self.age = age
        self.occupation = occupation
        self.skills = []
    
    # 实例方法
    def introduce(self):
        base_info = f"大家好，我是{self.name}，今年{self.age}岁"
        if self.occupation:
            base_info += f"，我的职业是{self.occupation}"
        return base_info
    
    # 实例方法 - 添加技能
    def add_skill(self, skill):
        if skill not in self.skills:
            self.skills.append(skill)
            return True
        return False
    
    # 实例方法 - 展示所有技能
    def show_skills(self):
        if not self.skills:
            return f"{self.name}目前没有掌握任何技能"
        skills_str = ", ".join(self.skills)
        return f"{self.name}掌握的技能: {skills_str}"
    
    # 特殊方法（魔术方法）- 用于字符串表示
    def __str__(self):
        return self.introduce()

# 创建类的实例
person1 = Person("张三", 25, "软件工程师")
person2 = Person("李四", 22)

# 使用实例方法
print(f"\n创建实例并使用方法:")
print(person1.introduce())
person1.add_skill("Python编程")
person1.add_skill("机器学习")
print(person1.show_skills())

print(person2.introduce())
person2.add_skill("数据可视化")
print(person2.show_skills())

# 访问类变量和实例变量
print(f"\n类变量访问: 物种 = {Person.species}")
print(f"实例变量访问: {person1.name}的年龄 = {person1.age}")

# 类的继承
class Student(Person):
    def __init__(self, name, age, major, student_id):
        # 调用父类的初始化方法
        super().__init__(name, age, "学生")
        self.major = major
        self.student_id = student_id
        self.courses = []
    
    # 重写父类方法
    def introduce(self):
        base_info = super().introduce()
        return f"{base_info}，专业是{self.major}，学号{self.student_id}"
    
    # 添加新方法
    def enroll_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
            return True
        return False

# 创建子类的实例
student1 = Student("王五", 19, "人工智能", "2023001")
print(f"\n继承示例 - 子类实例:")
print(student1.introduce())
student1.enroll_course("Python基础")
student1.enroll_course("人工智能导论")
print(f"{student1.name}选修的课程: {student1.courses}")
student1.add_skill("算法设计")
print(student1.show_skills())

# ========== 综合示例 ==========
print("\n\n===== 综合示例: 学生管理系统模拟 =====")

# 简单的学生管理系统类
class StudentManagementSystem:
    def __init__(self):
        self.students = []
    
    def add_student(self, student):
        self.students.append(student)
        print(f"已添加学生: {student.name}")
    
    def find_student_by_id(self, student_id):
        for student in self.students:
            if hasattr(student, 'student_id') and student.student_id == student_id:
                return student
        return None
    
    def get_students_by_major(self, major):
        return [student for student in self.students if hasattr(student, 'major') and student.major == major]
    
    def display_all_students(self):
        if not self.students:
            print("当前没有学生记录")
            return
        
        print("\n所有学生信息:")
        for i, student in enumerate(self.students, 1):
            print(f"{i}. {student}")
            if hasattr(student, 'courses'):
                print(f"   课程: {student.courses}")

# 创建学生管理系统实例
management_system = StudentManagementSystem()

# 添加学生
management_system.add_student(student1)
management_system.add_student(Student("赵六", 20, "计算机科学", "2023002"))
management_system.add_student(Student("钱七", 21, "人工智能", "2023003"))

# 显示所有学生
management_system.display_all_students()

# 查找特定专业的学生
ai_students = management_system.get_students_by_major("人工智能")
print(f"\n人工智能专业学生数量: {len(ai_students)}")

print("\nPython基础知识示例演示完毕!")