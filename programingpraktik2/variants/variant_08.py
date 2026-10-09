"""
Варіант 08. Циклічний зсув списку.
"""

def solve(list_str: str, k_str: str, direction_str: str) -> str:
    raise NotImplementedError  # TODO: реалізуйте розв'язок за карткою

if __name__ == "__main__":
    s_list = input("Введіть список: ")
    s_k = input("Введіть зсув: ")
    s_dir = input("Введіть напрямок (вліво/вправо): ")
    print(solve(s_list, s_k, s_dir))
