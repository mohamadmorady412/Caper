from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glBegin(GL_TRIANGLES)
    glColor3f(1, 0, 0)
    glVertex2f(-0.5, -0.5)
    glColor3f(0, 1, 0)
    glVertex2f(0.5, -0.5)
    glColor3f(0, 0, 1)
    glVertex2f(0.0, 0.5)
    glEnd()
    glFlush()

glutInit(sys.argv)                              # ✅ اول مقداردهی اولیه
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)     # ✅ مشخص‌کردن مد
glutInitWindowSize(500, 500)                    # ✅ تعیین اندازه پنجره
glutInitWindowPosition(100, 100)                # ✅ موقعیت پنجره
glutCreateWindow(b"Simple OpenGL Triangle")     # ✅ ساخت پنجره => اینجا context ساخته میشه

glutDisplayFunc(draw)                           # ✅ حالا می‌تونیم تابع نمایش رو تنظیم کنیم

glutMainLoop()                                  # ✅ اجرای حلقه اصلی
