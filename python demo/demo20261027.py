import time
import random
# 1. 定义机器鸭的初始状态（用到了你学的字典）
duck = {
    "name": "小黄鸭",
    "battery": 80,
    "is_tired": False,
    "action_log": []  # 记录动作的列表
}

# 2. 定义机器鸭的动作函数（用到了你刚学的 def）
def walk(steps):
    print(f"🦆 {duck['name']} 正在往前走 {steps} 步...")
    duck["battery"]-= steps * 2  # 走一步耗2%电
    duck["action_log"].append(f"走了{steps}步")

def charge():
    print(f"⚡ {duck['name']} 开始充电...")
    duck["battery"] = 100
    duck["is_tired"] = False
    duck["action_log"].append("充了一次电")

def rest():
    print(f"💤 {duck['name']} 累了，原地休息...")
    duck["battery"] += 5
    duck["is_tired"] = False
    duck["action_log"].append("休息了一下")

# 3. 主控循环（这就是机器人的“大脑循环”）
print(f"--- 启动机器鸭：{duck['name']} ---")
step_count = 1

while duck["battery"] > 0:
    print(f"\n[第 {step_count} 次决策] 当前电量: {duck['battery']}%")
    
    # 核心逻辑判断：根据电量决定动作
    if duck["battery"] < 20:
        charge()
    elif duck["is_tired"]:
        rest()
    else:
        walk(5)  # 每次走5步
        # 每次走完，有30%的概率会累（这里简单模拟一下）
        if random.randint(1,10)<=3:
            duck["is_tired"] = True
            
    step_count += 1
    
    # 每次循环停一秒，模拟真实时间
    time.sleep(1)

print("\n--- 电池耗尽，机器鸭关机 ---")
print(f"本次运行共执行了 {step_count-1} 次循环。")
print(f"动作日志记录：{duck['action_log']}")