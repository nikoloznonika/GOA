from turtle import*

#we want to paint a squire 

#step 1: draw a squire

begin_fill()
width(7)
speed(5)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#end of square 

#drawing a door 

forward(70)
begin_fill()
color("yellow")
left(90)
forward(120)
right(90)
forward(50)
right(90)
forward(120)
end_fill()

penup()
goto(200,200)
pendown()
 
color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

left(30)
color("purple")
begin_fill()
forward(80)
left(90)
color("brown")
forward(50)
left(90)
forward(70)
left(90)
forward(50)
end_fill()

penup()
goto(200,190)
pendown()

begin_fill()
forward(50)
left(90)
forward(70)
left(90)
forward(50)
end_fill()

   
exitonclick()