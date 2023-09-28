from main import funct

if __name__ == "__main__":
    a = 1.0
    b = 3.0
    E = 0.001
    while b - a > E:
        x = (a+b)/2
        f_a = funct(a)
        f_x = funct(x)
        if f_x*f_a < 0:
            b = x
        else:
            a = x
        result = a, b, x
        print("a=", a, "b=", b, "x=", x)
