from main import funct
from main import funct1
from main import funct2


if __name__ == "__main__":
    a = 1.0
    b = 3.0
    E = 0.006
    if funct1(b)*funct2(b) > 0:
        prev_x = None

        while True:
            x = a - (funct(a) * (b - a)) / (funct(b) - funct(a))
            x1 = x - (funct(x) - (b - x)) / (funct(b) - funct(x))
            a = x1
            print("x=", x, "x1=", x1)
            if abs(x1 - x) < E:
                print("Операцію завершено задана точність знайдена")
                break
            # Проверка на сходимость по разнице между текущим и предыдущим x
            if prev_x is not None and abs(x - prev_x) < E:
                print("Функція зайшла у нескінченний цикл і повинна бути зупинена")
                break

            prev_x = x

    else:
        prev_x = None

        while True:
            x = b - (funct(b) * (b - a)) / (funct(b) - funct(a))
            x1 = x - (funct(x)*(x - a)) / (funct(x) - funct(a))
            b = x1
            print("x=", x, "x1=", x1)
            if abs(x1 - x) < E:
                print("Операцію завершено задана точність знайдена")
                break
            # Проверка на сходимость по разнице между текущим и предыдущим x
            if prev_x is not None and abs(x - prev_x) < E:
                print("Функція зайшла у нескінченний цикл і повинна бути зупинена")
                break

            prev_x = x
