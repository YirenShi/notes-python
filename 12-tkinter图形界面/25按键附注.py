"""
char  从键盘输入的和按键事件相关的字符
keycode  从键盘输入的和按键事件相关的键的键代码（即统一码）
keysym   从键盘输入的和按键事件相关的键符号（即字符）
num    按键数字（1，2，3）表明按下的是那个鼠标键
widget  触发这个事件的小构件对象
x 和 y   当前鼠标在小构件中以像素为单位的位置
x_root 和y_root    当前鼠标相对于屏幕左上角的以像素为单位的位置

<B1-Motion>      当鼠标左键被按住在小构件且移动鼠标时事件发生
<Button-1>       Button-1，Button-2，Button-3表明左键 中  右，当在小构件上单击鼠标左键使Tkinter
会自动抓到鼠标指针的位置，ButtonPressed-i是Button-i的代名词
<ButtonRelease-1>   当释放鼠标左键时事件发生
<Double-Button-1>
<Enter>            当鼠标光标进入小构件时事件发生
<Key>              当单击一个键时事件发生
<Leave>           当鼠标光标离开小构件时事件发生
<Return>        当单击'Enter“键时事件发生，可以将键盘上任意键（像"A","B","UP")和一个事件绑定
<Shift-A>      当单击'Shift-A“键时事件发生，可以将Alt，Shift和Control和其他键组合
<Triple-Button>    当三次单击鼠标左键是事件发生


"""