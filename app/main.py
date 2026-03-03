from app.modules.mon_module import addition, multiplication


def main():
    result_add = addition(3, 5)
    result_mul = multiplication(3, 5)
    print(f"Addition : {result_add}")
    print(f"Multiplication : {result_mul}")
    return result_add, result_mul
