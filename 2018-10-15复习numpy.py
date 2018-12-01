# -*-coding:utf-8 -*-
import numpy as np
arr=np.arange(10)
print(arr)
#arr[5]
print(arr[5])
print(arr[3:6])
arr[3:6]=8
print(arr)
arr_2=arr[3:5]
arr_2[1]=11111
print(arr)
arr_2[:]=88
print(arr)
arr_3=arr[3:5].copy()
arr_3[:]=100
print(arr)
#多维数组，定位某个元素直接索引就可以
arr2d=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr2d[0])
print(arr2d[0][1])
print(arr2d[0,1])
#切片索引

print(arr[1:6])
print(arr2d)
print(arr2d[:1])
print(arr2d[:2,1:])
print(arr2d[:,:1])
#通用函数运算
arr=np.arange(10)
print(np.sqrt(arr))
print(np.exp(arr))
x=np.random.randn(8)
y=np.random.randn(8)
print(x)
print(y)
print(np.maximum(x,y))#元素极大值
arr=np.random.randn(5)*5
print(np.modf(arr))#将小数与整数分为两个数组显示出来
arr=np.random.randn(3,3)
print(arr)
print(np.where(arr>0,1,-1))
print(np.where(arr<0,0,arr))

arr=np.arange(10)
np.save('test_function',arr)
np.load('test_function.npy')