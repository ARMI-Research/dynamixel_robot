import os
import time
import argparse

SCENE_XML = r'''<mujoco model="open_manipulator_x scene">
  <include file="open_manipulator_x.xml"/>

  <statistic center="0.3 0 0.4" extent="1"/>

  <visual>
    <headlight diffuse="0.6 0.6 0.6" ambient="0.3 0.3 0.3" specular="0 0 0"/>
    <rgba haze="0.15 0.25 0.35 1"/>
    <global azimuth="120" elevation="-20"/>
  </visual>

  <asset>
    <texture type="skybox" builtin="gradient" rgb1="0.3 0.5 0.7" rgb2="0 0 0" width="512" height="3072"/>
    <texture type="2d" name="groundplane" builtin="checker" mark="edge" rgb1="0.2 0.3 0.4" rgb2="0.1 0.2 0.3"
      markrgb="0.8 0.8 0.8" width="300" height="300"/>
    <material name="groundplane" texture="groundplane" texuniform="true" texrepeat="5 5" reflectance="0.2"/>
  </asset>

  <worldbody>
    <light pos="0 0 1.5" dir="0 0 -1" directional="true"/>
    <geom name="floor" size="0 0 0.05" type="plane" material="groundplane"/>
  </worldbody>
</mujoco>
'''

MODEL_XML = r'''<mujoco model="open_manipulator_x">
  <compiler angle="radian" meshdir="C:\Users\7a1do\Desktop\ARMI_LAB\Test\assets" autolimits="true"/>

  <option integrator="implicitfast"/>

  <default>
    <joint armature="0.1" damping="10.0"/>
    <position kp="1000" kv="200" forcerange="-100 100"/>
  </default>

  <asset>
    <mesh name="link1" file="link1.stl" scale="0.001 0.001 0.001"/>
    <mesh name="link2" file="link2.stl" scale="0.001 0.001 0.001"/>
    <mesh name="link3" file="link3.stl" scale="0.001 0.001 0.001"/>
    <mesh name="link4" file="link4.stl" scale="0.001 0.001 0.001"/>
    <mesh name="link5" file="link5.stl" scale="0.001 0.001 0.001"/>
    <mesh name="gripper_left_palm" file="gripper_left_palm.stl" scale="0.001 0.001 0.001"/>
    <mesh name="gripper_right_palm" file="gripper_right_palm.stl" scale="0.001 0.001 0.001"/>
  </asset>

  <worldbody>
    <geom type="mesh" mesh="link1"/>
    <body name="link2" pos="0.012 0 0.017">
      <inertial pos="-0.000301849 0.000540437 0.0474335" quat="0.999915 0.000960074 0.0122201 -0.00449872" mass="0.0984068" diaginertia="3.4553e-05 3.26892e-05 1.88409e-05"/>
      <joint name="joint1" pos="0 0 0" axis="0 0 1" range="-3.14159 3.14159"  />
      <geom pos="0 0 0.019" quat="1 0 0 0" type="mesh" mesh="link2"/>
      <body name="link3" pos="0 0 0.0595">
        <inertial pos="0.0103084 0.000377434 0.101702" quat="0.71133 0.0466763 0.0513691 0.699423" mass="0.138509" diaginertia="0.000342915 0.000335932 5.49578e-05"/>
        <joint name="joint2" pos="0 0 0" axis="0 1 0" range="-1.5 1.5"  />
        <geom type="mesh" mesh="link3"/>
        <body name="link4" pos="0.024 0 0.128">
          <inertial pos="0.0909096 0.000389298 0.000224133" quat="-0.00162881 0.706672 0.0026348 0.707535" mass="0.132746" diaginertia="0.000251551 0.000242311 3.06462e-05"/>
          <joint name="joint3" pos="0 0 0" axis="0 1 0" range="-1.5 1.4"  />
          <geom type="mesh" mesh="link4"/>
          <body name="link5" pos="0.124 0 0">
            <inertial pos="0.0442068 3.684e-07 0.00891422" quat="0.479052 0.479052 -0.520105 0.520105" mass="0.143276" diaginertia="9.3211e-05 8.07871e-05 7.59805e-05"/>
            <joint name="joint4" pos="0 0 0" axis="0 1 0" range="-1.7 1.97"  />
            <geom type="mesh" mesh="link5"/>
            <body name="gripper_left_link" pos="0.0817 0.021 0">
              <inertial pos="0 0 0" mass="0.001" diaginertia="1e-06 1e-06 1e-06"/>
              <joint name="gripper_left_joint" pos="0 0 0" axis="0 1 0" type="slide" range="-0.01 0.019"  />
              <geom type="mesh" mesh="gripper_left_palm"/>
            </body>
            <body name="gripper_right_link" pos="0.0817 -0.021 0">
              <inertial pos="0 0 0" mass="0.001" diaginertia="1e-06 1e-06 1e-06"/>
              <joint name="gripper_right_joint" pos="0 0 0" axis="0 -1 0" type="slide" range="-0.01 0.019"  />
              <geom type="mesh" mesh="gripper_right_palm"/>
            </body>
            <body name="end_effector_target" pos="0.14 0 0">
              <inertial pos="0 0 0" mass="0.001" diaginertia="1e-06 1e-06 1e-06"/>
              <geom type= "box" size="0.005 0.005 0.005" rgba="1 0 0 1" contype="0" conaffinity="0"/>
            </body>
          </body>
        </body>
      </body>
    </body>
  </worldbody>

  <!-- Exclude contact information -->
  <contact>
    <exclude body1="world" body2="link2"/>
  </contact>

  <!-- Define actuators -->
  <actuator>
    <position name="actuator_joint1" joint="joint1" ctrlrange="-3.142 3.142"/>
    <position name="actuator_joint2" joint="joint2" ctrlrange="-1.5 1.5"/>
    <position name="actuator_joint3" joint="joint3" ctrlrange="-1.5 1.4"/>
    <position name="actuator_joint4" joint="joint4" ctrlrange="-1.7 1.97"/>
    <position name="actuator_gripper_joint" joint="gripper_left_joint" ctrlrange="-0.01 0.019"/>
  </actuator>
  <equality>
    <joint name="equality_gripper" active="true" joint1="gripper_left_joint" joint2="gripper_right_joint" polycoef="0 1 0 0 0"/>
  </equality>
</mujoco>
'''


def write_files(outdir: str):
    os.makedirs(outdir, exist_ok=True)
    scene_path = os.path.join(outdir, 'scene.xml')
    model_path = os.path.join(outdir, 'open_manipulator_x.xml')

    with open(scene_path, 'w', encoding='utf-8') as f:
        f.write(SCENE_XML)

    with open(model_path, 'w', encoding='utf-8') as f:
        f.write(MODEL_XML)

    print(f'Wrote XML files to: {outdir}')
    print('If your model references meshes, place them under: {}/assets/'.format(outdir))
    return scene_path


def run_with_mujoco(scene_path: str, duration: float): #headless: bool       (for safety)
    import mujoco
    import mujoco.viewer


    print('Using `mujoco` Python bindings (new API).')
    model = mujoco.MjModel.from_xml_path(scene_path)
    data = mujoco.MjData(model)

    # if headless:
    #   print('Running headless for {:.2f}s ({} steps)'.format(
    #       duration, int(duration / model.opt.timestep)))
    #   steps = int(duration / model.opt.timestep)
    #   for _ in range(steps):
    #       mujoco.mj_step(model, data)
    #   print('Headless run finished.')
    #   return

    print('Launching MuJoCo viewer (new API)...')
    with mujoco.viewer.launch_passive(model, data):
      t_end = time.time() + duration
      while time.time() < t_end:
        mujoco.mj_step(model, data)



# def run_with_mujoco_py(scene_path: str, duration: float, headless: bool):
#     # This is repurposed to use the new `mujoco` API so the fallback name remains but uses new binding.
#     import mujoco
    

#     model = mujoco.MjModel.from_xml_path(scene_path)
#     data = mujoco.MjData(model)

#     if headless:
#       print('Running headless for {:.2f}s ({} steps)'.format(
#         duration, int(duration / model.opt.timestep)))
#       steps = int(duration / model.opt.timestep)
#       for _ in range(steps):
#         mujoco.mj_step(model, data)
#       print('Headless run finished.')
#       return

#     print('Launching MuJoCo viewer (new API)...')
#     with mujoco.viewer.launch_passive(model, data):
#       t_end = time.time() + duration
#       while time.time() < t_end:
#         mujoco.mj_step(model, data)




def main():
    parser = argparse.ArgumentParser(description='Run open_manipulator_x scene (writes XML then runs MuJoCo).')
    parser.add_argument('--outdir', default=r'C:\Users\7a1do\Desktop\ARMI_LAB\Test\assets', help='Directory to write XML and put assets')
    parser.add_argument('--duration', type=float, default=10.0, help='Run duration in seconds (default 10s)')
    # parser.add_argument('--headless', action='store_true', help='Run without opening a viewer')
    args = parser.parse_args()

    scene_path = write_files(args.outdir)

    try:
        run_with_mujoco(scene_path, args.duration) #args.headless
        return
    except Exception as e:
        print('Failed to run with new `mujoco` bindings: {}'.format(e))
        print('Trying fallback to `mujoco_py`...')

    # try:
    #     run_with_mujoco_py(scene_path, args.duration, args.headless)
    #     return
    # except Exception as e:
    #     print('Failed to run with `mujoco_py`: {}'.format(e))
    #     print('\nCould not start MuJoCo. Please check that MuJoCo is installed and one of the Python bindings is available.')
    #     print('Also ensure any referenced assets (meshes) are present at: {}/assets/'.format(args.outdir))
    #     raise


if __name__ == '__main__':
    main()



'''
Remember to change the file location to where you save it
Then change the URL in this code into the address where the file is located

'''
