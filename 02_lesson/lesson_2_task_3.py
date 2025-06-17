import math
side = 4.1


def square(side):
    # Проверка, является ли переданный аргумент числом
    if not isinstance(side, (int, float)):
        raise ValueError("Аргумент должен быть числом.")

    # Вычисление площади квадрата
    area = side ** 2

    # Округление результата вверх, если он не является целым
    return math.ceil(area) if not area.is_integer() else int(area)


print(square(side))
