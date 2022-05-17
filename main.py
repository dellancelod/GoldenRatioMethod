import math

print("~Golden Ratio Method on Python~")

a = float(input("Enter a >> "))
b = float(input("Enter b >> "))
eps = float(input("Set precision ε >> "))


def f(x):
    return math.exp(6 * x - pow(x, 2))


def f_omega(w):
    x = (b - a) * w + a
    return f(x)


# Початкові значення
tau = 1.618
a_w = 0
b_w = 1
print("Interval: 0 ≤ w ≤ 1")
print(f"f(0) = {f_omega(0):.3}, f(1) = {f_omega(1):.3}")

# Перша ітерація:

iteration = 1
print("Iteration " + str(iteration))
w1 = a_w + (1 - 1. / tau) * (b_w - a_w)
w2 = a_w + 1. / tau * (b_w - a_w)
print(f"f({w1:.3}) = {f_omega(w1):.3}")
print(f"f({w2:.3}) = {f_omega(w2):.3}")

# Ітеративний процес
while abs(w2 - w1) > eps:
    iteration += 1
    print(f"Iteration {iteration}:")
    if f_omega(w1) > f_omega(w2):
        a_w = w1
        w1 = w2
        w2 = a_w + 1 / tau * (b_w - a_w)
        print(f"New point = {w2:.3}, f({w2:.3}) = {f_omega(w2):.3}")
    else:
        b_w = w2
        w2 = w1
        w1 = a_w + (1 - 1 / tau) * (b_w - a_w)
        print(f"New point = {w1:.3}, f({w1:.3}) = {f_omega(w1):.3}")


# Підсумок
wm = (w1 + w2)/2
xm = (b - a) * wm + a

print(f"Found minimum of function with precision {eps}: x_min = {xm:.3} f({xm:.3}) = {f(xm):.3}")
