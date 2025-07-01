import math


def square(side):
    area = side * side
    if not isinstance(side, int):
        area = math.ceil(area)
    return area


# Примеры использования
print(square(4))    # 16 (целое число)
print(square(4.5))  # 21 (округление вверх 20.25 → 21)
