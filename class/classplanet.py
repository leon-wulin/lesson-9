# -*- coding: UTF-8 -*-
# writen by leon
# writen time: 2019/11/23
import math


class Planet:
    name = '某行星'
    D = 0
    M = 0

    def __init__(self, planet_name, diameter, mass):
        "初始化函数"
        self.name = planet_name
        self.D = diameter
        self.r = self.D * 0.5
        self.M = mass
        self.V = self.cal_V()
        self.p = self.cal_p()
        self.g = self.cal_g()
        self.Ve = self.cal_Ve()
        return

    def cal_p(self):
        '根据天体质量和体积计算天体密度'

        return self.M / self.V / 1000000000000

    def cal_g(self):
        '根据天体质量和半径计算天体引力系数'
        G = 6.67259E-11
        g = self.M * G / self.r / self.r / 1000000
        return g

    def cal_Ve(self):
        G = 6.67259E-11
        Ve = math.sqrt(2 * G * self.M / self.r / 1000) / 1000
        return Ve
    def cal_V(self):
        '输入天体的半径，返回行星的体积'
        # r=self.D*0.5
        v = 4 / 3 * math.pi * (self.r**3)
        return v

    def report(self):
        "自行汇报"
        print('My name is %s' % self.name)
        print('My diameter is %d km, my mass is %0.2e kg' % (self.D, self.M))
        print('My volumeis %0.2e' % (self.V))
        print('My density is %f' % self.p)
        print('My gravity is %f' % self.g)
        print('My escape velocity is %f' % self.Ve)
        return
