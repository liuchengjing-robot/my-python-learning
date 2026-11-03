import mujoco
import mujoco.viewer
import time

if __name__ == '__main__':
    print("--- 开始加载模型 ---")
    try:
        # 直接读取当前目录下的场景文件
        model = mujoco.MjModel.from_xml_path("scene_walk.xml")
        data = mujoco.MjData(model)
        print("--- 模型加载成功！---")
    except Exception as e:
        print(f"\n❌ 加载失败！报错信息如下：\n{e}")
        exit()

    print("--- 正在启动 3D 窗口 ---")
    # 启动一个标准的被动视图窗口
    with mujoco.viewer.launch_passive(model, data) as viewer:
            # 只要你不关窗口，就一直运行
            while viewer.is_running():
                mujoco.mj_step(model, data)
                viewer.sync()
                time.sleep(0.01)