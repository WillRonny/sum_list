# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 20:48:57 2018
已知深渊有N层台阶，（0<N<1000）,每次能上的台阶都是2的整数次幂的台阶数，问上N阶有多少种方法
输入N，代表有多少组数据，接下来的为N个情况下的台阶数
@author: Will
"""
import numpy as np
A = []
N = int(input())
while N > 0:
    A.append(int(input()))
    N-=1    
x = []   # 一个解（长度不固定，1-2数组，表示该步走的台阶数）
X = []   # 一组解
# 冲突检测
for n in A:
    count = 0
    def conflict(k):
        global n, x, X
        
        # 部分解步的步数之和超过总台阶数
        if sum(x[:k+1]) > n:
            return True
        return False # 无冲突  
        
    # 回溯法（递归版本）
    def climb_stairs(k): # 走第k步
        global n, x, X,count
        
        if sum(x) == n:  # 已走的所有步数之和等于楼梯总台阶数
            count+=1

            #X.append(x[:]) # 保存（一个解）
        else:
            base = [2**i for i in range(int(np.log2(n))+1)]
            for i in base: # 第k步这个元素的状态空间为[1,2]
                x.append(i)
                if not conflict(k): # 剪枝
                    climb_stairs(k+1)
                x.pop()              # 回溯
        return count
    print(climb_stairs(0))