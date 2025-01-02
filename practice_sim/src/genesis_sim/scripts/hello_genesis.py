import genesis as gs
gs.init(seed                = None,
    precision           = '32',
    debug               = False,
    eps                 = 1e-12,
    logging_level       = None,
    backend             = gs.gpu,
    theme               = 'dark',
    logger_verbose_time = False)

scene = gs.Scene(sim_options=gs.options.SimOptions(
        dt=0.001,
        gravity=(0, 0, -9.8),
    ),
    show_viewer=True,
    viewer_options=gs.options.ViewerOptions(
        camera_pos=(3.5, 0.0, 2.5),
        camera_lookat=(0.0, 0.0, 0.5),
        camera_fov=40,
    ),)
plane = scene.add_entity(gs.morphs.Plane())
franka = scene.add_entity(
    # gs.morphs.MJCF(file='xml/franka_emika_panda/panda.xml'),
    gs.morphs.URDF(file='/home/lin/PRACTICE-Simulator/practice_sim/src/practice3_urdf/urdf/practice3.urdf',pos=(0,0,0.5)),
)

scene.build()

for i in range(1000):
    scene.step()