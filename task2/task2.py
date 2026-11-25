import sys
from fractions import Fraction

def parse_fraction(token):
    try:
        return Fraction(token)
    except (ValueError, ZeroDivisionError):
        pass
    try:
        return Fraction(token.replace(',', '.'))
    except ValueError:
        pass
    raise ValueError(f"не удалось распознать число: {token}")

def read_numbers(path):
    numbers = []
    with open(path, "r", encoding="utf-8") as f:
        for lineno, line in enumerate(f):
            for token in line.split():
                try:
                    numbers.append(parse_fraction(token))
                except ValueError as e:
                    raise ValueError(f"{path}:{lineno}: {e}")
    return numbers

def main():
    if len(sys.argv) != 3:
        print("Использование: python script.py <файл_эллипса> <файл_точек>")
        return 

    ellipse_path = sys.argv[1]
    points_path = sys.argv[2]

    try:
        ellipse = read_numbers(ellipse_path)
        points = read_numbers(points_path)
    except Exception as e:
        print(f"Ошибка чтения: {e}")
        return

    if len(ellipse) != 4:
        print(f"Ошибка: в файле эллипса должно быть ровно 4 числа, найдено {len(ellipse)}")
        return

    if len(points) % 2 != 0:
        print(f"Ошибка: в файле точек должно быть чётное число координат "
              f"(x y), найдено {len(points)}")
        return

    x0, y0, rx, ry = ellipse
    rx = abs(rx)
    ry = abs(ry)

    if rx == 0 or ry == 0:
        print("Ошибка: радиусы эллипса должны быть ненулевыми")
        return

    for i in range(0, len(points), 2):
        x, y = points[i], points[i + 1]

        dx = x - x0
        dy = y - y0

        lhs = dx * dx * ry * ry + dy * dy * rx * rx
        rhs = rx * rx * ry * ry

        if lhs == rhs:
            print(0)  
        elif lhs < rhs:
            print(1)  
        else:
            print(2)  

if __name__ == "__main__":
    main()