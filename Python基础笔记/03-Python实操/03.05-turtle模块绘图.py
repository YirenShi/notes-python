"""
是一个简单的绘图工具
提供一个小海龟，可以在它了解为一个机器人，只能听懂有限的命令
绘图窗口的原点（0，0）在正中间，默认海龟的方向是右侧
运动命令
forward(d)  向前移动d长度
backward(d)  向后移动d长度
right(d)   向右转动d角度
goto（x，y）   移动到坐标为（x， y）的位置
speed(speed)   笔画绘制的速度[ 0 , 10 ] 越大越快

笔画控制命令
up（）   笔画抬起，在移动时候不会绘图
down（）  笔画落下
setheading（d）   改变海龟的朝向
pensize(d)   笔画的宽度
pencolor（colorstr）   笔画颜色
reset()  恢复所有设置，清空窗口，重置turtle 状态
clear（）  清空窗口，不会重置turtle
circle(r,e)   绘制一个圆形，r为半径，e为次数
#begin_fill()
#fillcolor("colorstr")   3个共同使用
#end_fill()
其它命令
1.done（）程序继续执行
2.undo（） 撤销上一次动作
3.hideturtle（）   隐藏海龟
4.showturtle()   显示海龟
5.screensize（x，y）
"""
#导入turtle
import turtle

turtle.screensize(400,400)
turtle.forward(100)
turtle.right(100)
turtle.forward(100)
turtle.pencolor("red")
turtle.goto(-100,200)
turtle.up()
turtle.goto(-200,200)
turtle.down()
turtle.goto(-0,200)
turtle.setheading(45)
#turtle.clear()
turtle.begin_fill()
turtle.fillcolor("blue")
turtle.circle(50,steps = 5)
turtle.end_fill()
turtle.hideturtle()
turtle.done()