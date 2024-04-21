import turtle

def draw_fractal(t, order, size):
    if order == 0:
        for _ in range(4):
            t.forward(size)
            t.left(90)
    else:
        draw_fractal(t, order-1, size/3)
        t.forward(size/3)
        draw_fractal(t, order-1, size/3)
        t.forward(size/3)
        draw_fractal(t, order-1, size/3)
        t.backward(size/3)
        t.left(90)
        t.forward(size/3)
        t.right(90)
        draw_fractal(t, order-1, size/3)
        t.forward(size/3)
        draw_fractal(t, order-1, size/3)
        t.backward(size/3)
        t.left(90)
        t.backward(size/3)
        t.right(90)

def main():
    window = turtle.Screen()
    window.bgcolor("white")
    window.title("Sierpinski Carpet")

    t = turtle.Turtle()
    t.penup()
    t.goto(-150, -150)
    t.pendown()
    t.speed(0)  # Установка максимальної швидкості малювання

    order = int(turtle.numinput("Рівень рекурсії", "Введіть рівень рекурсії (ціле число):", default=3))

    # Малюємо килим Серпінського
    draw_fractal(t, order, 300)

    window.mainloop()

if __name__ == "__main__":
    main()
