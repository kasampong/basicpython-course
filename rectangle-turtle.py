import turtle
tao = turtle.Pen() #ดึงความสามารถใช้ปากกา
tao.shape('turtle') #แปลงร่างเป็นเต่า

def Rectangle():
    ''' ฟังก์ชันนี้ไว้วาดรูปสี่เหลี่ยม '''
    for i in range(4):
        tao.forward(100)
        tao.left(90)

def Go(x,y):
    tao.penup()
    tao.goto(x,y)
    tao.pendown()

Go(200,200)
Rectangle()

#สร้างโปรแกรมturtleอะไรก็แต่ แต่ต้องใช้ loop และ function
