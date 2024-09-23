import turtle
import random

screen = turtle.Screen()
screen.bgcolor("white")

pookkalam = turtle.Turtle()
pookkalam.speed(0)

def draw_petal(radius, color):
    pookkalam.fillcolor(color)
    pookkalam.begin_fill()
    pookkalam.circle(radius, 60)
    pookkalam.left(120)
    pookkalam.circle(radius, 60)
    pookkalam.left(120)
    pookkalam.end_fill()

def draw_flower(radius, num_petals, color):
    pookkalam.color("black")
    pookkalam.fillcolor(color)
    pookkalam.begin_fill()
    
    for _ in range(num_petals):
        draw_petal(radius, color)
        pookkalam.right(360 / num_petals)
    
    pookkalam.end_fill()

def draw_pookkalam(layers):
    radius = 50
    colors = ["red", "yellow", "blue", "orange", "green", "purple", "pink", "cyan", "lightgreen", "gold", "darkblue"]
    
    for i in range(layers):
        num_petals = 6 + i * 6
        color = random.choice(colors)
        
        pookkalam.penup()
        pookkalam.goto(0, -radius)
        pookkalam.pendown()
        
        draw_flower(radius, num_petals, color)
        
        radius += 40

draw_pookkalam(7)
pookkalam.hideturtle()
turtle.done()
