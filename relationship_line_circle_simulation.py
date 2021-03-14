# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 23:19:16 2021

@author: 帅比唐尧
"""

#编写类实现直线和圆的位置关系

import math


class Point:
    """模拟坐标"""
    
    def __init__(self,x=0,y=0):
        """初始化横纵坐标"""
        self.x=x
        self.y=y


def Distance_Point_Point(p1,p2):
    """模拟两点距离"""
    d=math.sqrt((p1.x-p2.x)*(p1.x-p2.x)+(p1.y-p2.y)*(p1.y-p2.y))
    return round(d,4)#保留四位小数


class Line:
    """模拟直线"""

    def __init__(self,a=0,b=0,c=0):
        """用直线一般式(ax+by+c=0)表示且a,b不同时为0"""
        self.a=a
        self.b=b
        self.c=c


def Distance_Line_Point(line,point):
    """模拟点到直线距离"""
    d=abs(line.a*point.x+line.b*point.y+line.c)/(math.sqrt(line.a*line.a+line.b*line.b))
    return round(d,4)


class Circle:
    """模拟圆"""
    
    def __init__(self,x=0,y=0,r=1):
        """圆心c(x,y),半径r"""
        self.c=Point(x,y)
        self.r=r
    

def Relationship_Line_Circle(line,circle):
    """模拟直线与圆位置关系"""
    d=Distance_Line_Point(line,circle.c)#圆心到直线距离
    if d>circle.r:
        print(f"直线{line.a}x+{line.b}y+{line.c}=0与圆心在({circle.c.x},{circle.c.y}),半径为{circle.r}的圆相离")
    elif d==circle.r:
        print(f"直线{line.a}x+{line.b}y+{line.c}=0与圆心在({circle.c.x},{circle.c.y}),半径为{circle.r}的圆相切")
    else:
        print(f"直线{line.a}x+{line.b}y+{line.c}=0与圆心在({circle.c.x},{circle.c.y}),半径为{circle.r}的圆相交")
        
        
p1=Point(3,4)
p2=Point()
print(p1.x,p1.y) 
d1=Distance_Point_Point(p1, p2) 
print(d1)    
l=Line(a=1,b=1,c=2)
d2=Distance_Line_Point(l, p2)
print(d2)
c=Circle(r=2)
Relationship_Line_Circle(l,c)
  