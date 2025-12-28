import matplotlib.pyplot as plt
import numpy as np

"""
Дерево Піфагора — це класичний приклад фрактала,
який створюється шляхом рекурсивного поділу гілок.

На кожному рівні рекурсії від кінця гілки будуються
дві нові гілки під різними кутами, а їх довжина зменшується
на фіксований коефіцієнт.

Процес повторюється доти, доки не буде досягнута
задана користувачем глибина рекурсії.
"""

def draw_branch(x, y, angle, length, depth):
    if depth == 0:
        return

    # Використовуємо тригонометричні функції cos і sin, щоб знайти нові координати кінця гілки за заданим кутом та довжиною
    x_end = x + length*np.cos(np.radians(angle))
    y_end = y + length*np.sin(np.radians(angle))

    # малюємо гілку
    plt.plot([x, x_end], [y, y_end],'black', linewidth=2)

    # Рекурсивно малюємо ліву та праву гілки
    # Ліва гілка: кут +45 градусів
    new_length = length * 0.7
    draw_branch(x_end, y_end, angle+45, new_length, depth-1)

    # Права гілка: кут -45 градусів
    draw_branch(x_end, y_end, angle-45, new_length, depth-1)


if __name__ == '__main__':
    while True:
        depth = int(input("Enter the recursion depth: "))
        if depth < 0:
            print("Please enter a non-negative number")
        else:
            break

    # Налаштування вікна для малювання
    plt.figure(figsize=(8, 8))
    plt.axis('off')
    plt.title(f'Дерево Піфагора - Глибина: {depth}')

    start_x = 0
    start_y = 0
    start_angle = 90
    start_length = 100

    draw_branch(start_x, start_y, start_angle, start_length, depth)

    plt.show()
