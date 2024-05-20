from turtle import *


#we want to paint a house

#step 1: draw a squar
width(7)
color("green")

speed(3)
forward(200)
left(90)  

forward(200)
left(90)
forward(200)
left(90)


forward(200) 
left(90)
forward(90)
left(90)
forward(90)
right(90)    
forward(40)       
right(90)
forward(90)
left(90)
forward(70)
left(90)
forward(200)
color("green")
begin_fill()
left(45)
forward(150)
left(95)
forward(150)
end_fill()

penup()
goto(50, 100)
pendown()



right(50)
forward(42)
right(90)
forward(60)
right(90)
forward(42)
right(90)
forward(60)
right(90)
forward(20)
right(90)
forward(60)
left(180)
forward(30)
left(90)
forward(20)
left(180)
forward(41)


penup()
goto(180, 100)
pendown()

forward(41)
right(90)
forward(60)
right(90)
forward(41)
right(90)
forward(60)
right(90)
forward(20)
right(90)
forward(60)
left(180)
forward(30)
left(90)
forward(20)
left(180)
forward(41)
exitonclick()