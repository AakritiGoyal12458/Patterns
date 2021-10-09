import turtle as t
colors=('red','orange','blue','green','yellow','purple','white')
rainbow=t.Pen()
t.bgcolor('black')
for i in range(360):
    rainbow.pencolor(colors[i%6])
    rainbow.width(i/100+1)
    rainbow.forward(i)
    rainbow.left(59)
t.done()

