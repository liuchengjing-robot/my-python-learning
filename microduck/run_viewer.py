import time
import mujoco
import mujoco.viewer
import env
import numpy as np

if __name__ == '__main__':
    print("正在加载鸭子模型...")
    e = env.MicroduckEnv(seed=0)
    e.reset(seed=0)
    
    print("启动 3D 物理窗口...")
    with mujoco.viewer.launch_passive(e.model, e.data) as viewer:
        # 强制让摄像机对准鸭子的位置
        viewer.cam.lookat[:] = [0, 0, 0.1] 
        viewer.cam.distance = 0.5  # 拉近一点
        viewer.cam.elevation = -20 # 俯视一点
        
        while viewer.is_running():
            # 只刷新画面，不进行物理步进（这样鸭子就不会掉下去了）
            # 相当于把时间暂停了
            mujoco.mj_forward(e.model, e.data)
            viewer.sync()
            time.sleep(0.01)