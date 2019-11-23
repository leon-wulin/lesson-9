# -*- coding: UTF-8 -*-
#writen by leon
#writen time: 2019/11/23
#--------------------------(max to 80 words)------------------------------------

from classplanet import Planet

#Mercury=(4878,3.02E+23)

p=Planet('Mercury',4878,3.02E+23)

'''
p=Planet()
p.name='Mercury'
p.D=Mercury[0]
p.M=Mercury[1]
'''

#print('Planet %s:Volume is %0.2e stere'%(p.name,p.cal_V()))
p.report()
