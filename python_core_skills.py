# Python核心知识点示例代码

# 1. 面向对象编程
class Student:
    # 类变量
    school_name = "北京大学"
    
    def __init__(self, name, age, major=None):
        # 实例变量
        self.name = name
        self.age = age
        self.major = major
        self.courses = []
    
    # 实例方法
    def add_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
            return True
        return False
    
    # 静态方法
    @staticmethod
    def is_valid_age(age):
        return 16 <= age <= 30
    
    # 类方法
    @classmethod
    def change_school_name(cls, new_name):
        cls.school_name = new_name
    
    # 特殊方法（魔术方法）
    def __str__(self):
        return f"学生: {self.name}, 年龄: {self.age}, 专业: {self.major or '未确定'}"

# 2. 继承与多态
class GraduateStudent(Student):
    def __init__(self, name, age, major, supervisor):
        super().__init__(name, age, major)
        self.supervisor = supervisor
        self.research_topic = None
    
    def set_research_topic(self, topic):
        self.research_topic = topic
    
    def __str__(self):
        base_info = super().__str__()
        return f"{base_info}, 导师: {self.supervisor}, 研究方向: {self.research_topic or '未确定'}"

# 3. 异常处理
def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("错误: 除数不能为零!")
        return None
    except TypeError:
        print("错误: 请输入数字类型!")
        return None
    finally:
        print("除法运算完成")

# 4. 上下文管理器（with语句）
class FileHandler:
    def __init__(self, file_path, mode='r'):
        self.file_path = file_path
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        try:
            self.file = open(self.file_path, self.mode)
            return self.file
        except IOError:
            print(f"无法打开文件: {self.file_path}")
            return None
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

# 5. 数据结构与算法
def find_unique_elements(arr):
    # 使用集合（set）查找唯一元素
    unique_elements = set(arr)
    return list(unique_elements)

def count_word_frequency(text):
    # 使用字典（dictionary）统计词频
    words = text.lower().split()
    frequency = {}
    
    for word in words:
        # 去除标点符号
        clean_word = ''.join(char for char in word if char.isalnum())
        if clean_word:
            frequency[clean_word] = frequency.get(clean_word, 0) + 1
    
    return frequency

# 6. 函数式编程
from functools import reduce

def calculate_factorial(n):
    if n < 0:
        raise ValueError("输入必须是非负整数")
    return reduce(lambda x, y: x * y, range(1, n + 1), 1)

# 7. 生成器与迭代器
def fibonacci_generator(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

# 8. 装饰器
def log_function(func):
    def wrapper(*args, **kwargs):
        print(f"调用函数: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"函数 {func.__name__} 返回: {result}")
        return result
    return wrapper

@log_function
def add(a, b):
    return a + b

# 9. 模块与包的导入
import random
import math

# 10. 列表推导式与生成器表达式
def generate_squares(n):
    # 列表推导式
    return [i * i for i in range(n)]

# 测试代码
if __name__ == "__main__":
    print("===== Python核心知识点示例 =====")
    
    # 测试面向对象编程
    print("\n1. 面向对象编程测试:")
    s1 = Student("张三", 20, "计算机科学")
    s1.add_course("Python编程")
    s1.add_course("数据结构")
    print(s1)
    print(f"是否是有效年龄: {Student.is_valid_age(20)}")
    
    # 测试继承
    print("\n2. 继承与多态测试:")
    gs = GraduateStudent("李四", 25, "人工智能", "王教授")
    gs.set_research_topic("机器学习")
    print(gs)
    
    # 测试异常处理
    print("\n3. 异常处理测试:")
    result = divide_numbers(10, 0)
    
    # 测试文件操作（这里仅做演示，不会实际创建文件）
    print("\n4. 上下文管理器测试:")
    # with FileHandler('test.txt', 'w') as f:
    #     if f:
    #         f.write("Hello, Python!")
    
    # 测试数据结构
    print("\n5. 数据结构测试:")
    numbers = [1, 2, 2, 3, 4, 4, 5]
    print(f"唯一元素: {find_unique_elements(numbers)}")
    
    # 测试函数式编程
    print("\n6. 函数式编程测试:")
    print(f"5的阶乘: {calculate_factorial(5)}")
    
    # 测试生成器
    print("\n7. 生成器测试:")
    print("斐波那契数列前10项:", end=" ")
    for num in fibonacci_generator(10):
        print(num, end=" ")
    print()
    
    # 测试装饰器
    print("\n8. 装饰器测试:")
    add(3, 5)
    
    # 测试列表推导式
    print("\n9. 列表推导式测试:")
    print(f"0-9的平方: {generate_squares(10)}")
    
    print("\n测试完成!")