import turtle

t = turtle.Pen()

ros = int(input("Rosetas: "))

for x in range(ros):
    t.circle(100)
    t.left((90 - ros))

input()