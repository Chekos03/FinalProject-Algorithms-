import turtle


t = turtle.Turtle()
t.speed(0)         
t.left(90)              

def draw_tree(length, depth):
    if depth == 0:
        return
    t.forward(length)
    t.left(30)
    draw_tree(length * 0.7, depth - 1)

    t.right(60)
    draw_tree(length * 0.7, depth - 1)

    t.left(30)
    t.backward(length)


level = int(input("Введіть рівень рекурсії: "))
draw_tree(80,level)
turtle.done()  

