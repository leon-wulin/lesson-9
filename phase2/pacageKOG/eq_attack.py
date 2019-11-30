# -*- coding: UTF-8 -*-
# writen by leon
# writen time: 2019/11/23
import globalVAR as GLV
import random
from class_equipment import Equipment


class eq_attack(Equipment):
    critical_strike = 0.0
    physical_suck = 0.0

    def show_me_unique(self):
        print('-----独有加成-----')
        print('       +暴击率:%0.2f' % (self.critical_strike))
        print('     +物理吸血:%0.2f' % (self.physical_suck))
        print('-----------------')
        return

    def __set_name(self):

        all_eq_name = (
            '铁剑',
            '匕首',
            '搏击拳套',
            '吸血之镰',
            '鸣刃',
            '冲能拳套',
            '风暴巨剑',
            '日冕',
            '狂暴双刃',
            '陨星',
            '碎星锤',
            '末世',
            '名刀·司命',
            '冰霜长矛',
            '速击之枪',
            '制裁之刃',
            '泣血之刃',
            '无尽战刃',
            '宗师之力',
            '闪电匕首',
            '影刃',
            '暗影战斧',
            '破军',
            '纯净苍穹',
            '逐日之弓',
            '破魔刀',
            '穿云弓',
            '破晓'
        )

        return random.choice(all_eq_name)

    def __init__(self):
        '按规则生成攻击道具'
        self.name = self.__set_name()

        for i in range(GLV.MAX_FORGE_TIMES):
            n=random.randint(0,10)
            self.__forge_eq(n)
        return

    def __forge_eq(self, skill_num):
        '''锻造道具'''
        if skill_num == 0:
            self.add_physical_attack += 0.05 * GLV.MAX_ATTACK
        elif skill_num == 1:
            pass
        elif skill_num == 2:
            self.add_mana_defense += 0.05 * GLV.MAX_DEFENSE
        elif skill_num == 3:
            pass
        elif skill_num == 4:
            self.add_move_speed += 0.05 * GLV.MAX_MOVE_SPEED
        elif skill_num == 5:
            self.add_life_force += 0.05 * GLV.MAX_LIFE_FORCE
        elif skill_num == 6:
            self.add_mana_power += 0.05 * GLV.MAX_MANA_POWER
        elif skill_num == 7:
            self.critical_strlike = random.uniform(0.1, 0.5)
            if self.critical_strike >= 0.5:
                self.critical_strike = 0.5
        elif skill_num == 8:
            self.physical_suke = random.uniform(0.01, 0.1)
            if self.physical_suck >= 0.1:
                self.physical_suck = 0.1
        elif skill_num == 9:
            pass
        elif skill_num == 10:
            pass
        else:
            pass
        return

if __name__ == '__main__':
    eq = eq_attack()
    eq.show_me()
    eq.show_me_unique()
