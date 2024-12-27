import mujoco_py
from urdfpy import URDF

# 加载URDF文件
urdf = URDF.load('../balance_infantry_urdf/urdf/balance_infantry.urdf')

# 将URDF转换为MuJoCo XML格式
mjcf_model = urdf.to_mjcf()

# 保存MuJoCo XML文件
with open('model.xml', 'w') as f:
    f.write(mjcf_model.xml_string)

# 加载MuJoCo模型
model = mujoco_py.load_model_from_path('model.xml')
sim = mujoco_py.MjSim(model)

# 创建渲染器
viewer = mujoco_py.MjViewer(sim)

# 运行模拟并渲染
while True:
    sim.step()
    viewer.render()