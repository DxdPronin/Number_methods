from main import funct
from main import funct1
from main import funct2

if __name__ == "__main__":
    a = 1.0
    b = 3.0
    E = 0.001
    if funct1(b)*funct2(b) > 0:
        prev_x = None
        while True:
            x = b - funct(b)/funct1(b)
            x1 = x - funct(x)/funct1(x)
            b = x1
            print("x=", x, "x1=", x1)
            if abs(x1 - x) < E:
                print("Операцію завершено задана точність знайдена")
                break
            if prev_x is not None and abs(x - prev_x) < E:
                print("Функція зайшла у нескінченний цикл і повинна бути зупинена")
                break

            prev_x = x

    else:
        prev_x = None
        while True:
            x = a - funct(a) / funct1(a)
            x1 = x - funct(x) / funct1(x)
            a = x1
            print("x=", x, "x1=", x1)
            if abs(x1 - x) < E:
                print("Операцію завершено задана точність знайдена")
                break
            if prev_x is not None and abs(x - prev_x) < E:
                print("Функція зайшла у нескінченний цикл і повинна бути зупинена")
                break

            prev_x = x
            print("x=", x, "x1=", x1)

