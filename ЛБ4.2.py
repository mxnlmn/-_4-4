import turtle

def koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order-1, size/3)
            t.left(angle)

def main():
    window = turtle.Screen()
    window.bgcolor("white")
    window.title("Koch Snowflake")

    t = turtle.Turtle()
    t.penup()
    t.goto(-150, 90)
    t.pendown()
    t.speed(0)  # Установка максимальної швидкості малювання

    # Введення рівня рекурсії
    order = int(turtle.numinput("Рівень рекурсії", "Введіть рівень рекурсії (ціле число):", default=3))

    # Малюємо крижинку Коха
    for _ in range(3):
        koch_snowflake(t, order, 300)
        t.right(120)

    window.mainloop()

if __name__ == "__main__":
    main()
