# Gradient_descent
题目描述： 

1.Generate n = 2,000 points uniformly at random in the two-dimensional unit square.Which point do you expect the centroid to be?  
2.What objective does the centroid of the points optimize?  
3.Apply gradient descent to find the centroid.  
4.Apply stochastic gradient descent to find the centroid. Can you say in simple words,what the algorithm is doing?  
1、所谓质心，就是找到到所有点距离之和最小的点。由于点的生成都是随机的，所以期望的点是 : (0.5，0.5)。

2.已知质心到其他点的距离和是最短的，即找到这样一个点 C(x,y) 使得 f(x,y)最小即可。所以目标函数可以表示成计算质心到其他点的欧式距离开方，优化目标函数就是min f(x,y)

3.关键在于求梯度

4.随机梯度下降和梯度下降的区别：梯度下降是所有点都参与梯度更新，而随机梯度下降是每次循环随机选取点进行。这样的话可以解决一次性加载数据量太大内存不够的问题，跟普通梯度下降不同的是，随机梯度下降采用了随机选点。

Please run Homework1.2.py to get the result


