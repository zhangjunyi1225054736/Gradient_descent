#!/usr/bin/env python
# coding=utf-8
from scipy import *
import matplotlib
import matplotlib.pyplot as plt
from random import choice

points = rand(2000,2)
#print(points)

#画出散点图
plt.figure(1)
plt.plot(points[:,0],points[:,1],'.')
#plt.show()

#计算损失
def cost(x):
    cost_ = sum(sum((x-points)**2,axis = 1)**0.5)
    return cost_
    #print(cost_)

#求梯度
def get_gredient(x):
    dx_ = sum((x[0] - points[:,0]) / sum((x - points)**2,axis=1)**0.5)
    dy_ = sum((x[1] - points[:,1]) / sum((x - points)**2,axis=1)**0.5) 
    s = (dx_**2+dy_**2)**0.5
    dx = dx_/s
    dy = dy_/s
    return array([dx,dy])


def get_stochastic_gredient(x):
    points_ = choice(points)
    dx_ = (x[0] - points_[0]) / sum((x - points_)**2)**0.5
    dy_ = (x[1] - points_[1]) / sum((x - points_)**2)**0.5 
    s = (dx_**2+dy_**2)**0.5
    dx = dx_/s
    dy = dy_/s
    return array([dx,dy])



x = array([0,1])
theta = 0.001
max = 10000
thread = 1e-6

xb = x

for i in range(max):
    cost_ = cost(x)
    #x = x - theta*get_gredient(x)
    x = x - theta*get_stochastic_gredient(x)
    print(cost_)
    xb = vstack((xb,x))
c = x
print(c)
plt.figure(2)
plt.plot(points[:,0],points[:,1],'.')
plt.plot(xb[:,0],xb[:,1],'r.')
plt.plot(xb[:,0],xb[:,1],'k-')
plt.xlabel('c = (%.3f,%.3f)'%(c[0],c[1]))

plt.show()
