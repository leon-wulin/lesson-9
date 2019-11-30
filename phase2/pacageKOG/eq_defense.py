# -*- coding: UTF-8 -*-
# writen by leon
# writen time: 2019/11/30

import sys
from class_equipment import Equipment


class eq_defense(Equipment):

    restore_life_force=0.0

    def show_me_unique(self):
        print('----------独有加成-------------')
        print('          +回血:%0.2f'%(self.restore_life_force))
        print('------------------------------')
        return
    def __set_name(self):


        return random.choice(all_eq_name)

    def __init__(self):
        '按规则生成防御道具'
        self.name = self.__set_name()

        for i in range(GLV.MAX_FORGE_TIMES):
            n=random.randint(0,10)
            self.__forge_eq(n)
        return

    def __forge_eq(self, skill_num):
        '''锻造道具'''
        if skill_num == 0:#物攻
            pass
        elif skill_num == 1:#物防
            pass
        elif skill_num == 2:#法防
            self.add_mana_defense += 0.05 * GLV.MAX_DEFENSE
        elif skill_num == 3:#回蓝
            pass
        elif skill_num == 4:#移速
            self.add_move_speed += 0.05 * GLV.MAX_MOVE_SPEED
        elif skill_num == 5:#生命
            self.add_life_force += 0.05 * GLV.MAX_LIFE_FORCE
        elif skill_num == 6:#法力
            self.add_mana_power += 0.05 * GLV.MAX_MANA_POWER
        elif skill_num == 7:#暴击
            self.critical_strlike = random.uniform(0.1, 0.5)
            if self.critical_strike >= 0.5:
                self.critical_strike = 0.5
        elif skill_num == 8:#吸血
            self.physical_suke = random.uniform(0.01, 0.1)
            if self.physical_suck >= 0.1:
                self.physical_suck = 0.1
        elif skill_num == 9:#法攻
            self.add_+=0.05*GLV.MAX_
        elif skill_num == 10:#回血
            pass
        else:
            pass
        return

if __name__ == '__main__':
    eq=eq_defense()
    eq.show_me()
    eq.show_me_unique()
