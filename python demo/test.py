import random
import time

class Microduck:
    def __init__(self,name,color):
        self.name=name
        self.color=color
        self.battery=30
        self.is_tired=False
        self.action_log=[]

    def walk(self):
        self.battery-=10
        self.action_log.append('走了一步')
        print(f'{self.name}正在走路，剩余电量{self.battery}%')

        if random.randint(1,10)<=3:
            self.is_tired-True
            print(f'{self.name}走累了')
    def charge(self):
        self.battery+=20
        if self.battery>=100:
            self.battery=100
        self.action_log.append('充了一次电')
        print(f'{self.name}正在充电，电量恢复到{self.battery}%了')
    def rest(self):
        self.battery+=5
        self.is_tired = False
        self.action_log.append('累了，休息一下')
        print(f'{self.name}累了，正在休息，电量恢复到{self.battery}%了')

#主程序
microduck1 = Microduck('小黄鸭','黄色')
print(f'{microduck1.name},启动！颜色是{microduck1.color}')
step_count = 1
while microduck1.battery > 0 and step_count<=10:
    print(f'\n[第{step_count}决策]')

    if microduck1.battery<20:
        microduck1.charge()
    elif microduck1.is_tired:
        microduck1.rest()
    else:
        microduck1.walk()
    step_count+=1
    time.sleep(1)
print('\n---电池耗尽，机器鸭子关机---')
print(f'总共执行了{step_count-1}次决策')

print('\n机器鸭的一生(动作日志)')
for action in microduck1.action_log:
    print(f'-{action}')
