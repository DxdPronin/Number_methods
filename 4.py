from main import fi
from main import fi1


if __name__ == "__main__":
    a = 1.0
    b = 3.0
    E = 0.001
    if fi1(a) > fi1(b):
        q = fi1(a)
    else:
        q = fi1(b)
    r = q
    prev_x = None
    while True:
        x = fi(r)
        x1 = fi(x)
        r = x1
        print("x=", x, "x1=", x1)
        if abs(x1 - x) < (E*(1-q))/q:
            print("Операцію завершено задана точність знайдена")
            break
        if prev_x is not None and abs(x - prev_x) < E:
            print("Функція зайшла у нескінченний цикл і повинна бути зупинена")
            break

        prev_x = x





