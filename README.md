# OpenMANIPULATOR-X
<img src="https://github.com/ROBOTIS-GIT/emanual/blob/master/assets/images/platform/openmanipulator_x/OpenManipulator.png">
<img src="https://github.com/ROBOTIS-GIT/emanual/blob/master/assets/images/platform/openmanipulator_x/OpenManipulator_Chain_Capture.png" width="500">

The 4-DOF Open Manipulator-X now supports MoveIt 2, enabling enhanced motion planning and control for advanced robotic applications. This update also brings significant improvements to the teleoperation features, example use cases, and the graphical user interface (GUI), providing a more seamless and user-friendly experience for developers and researchers.

- Active Branches: noetic, humble, main
- Legacy Branches: *-devel

# Warning: porting in Gz Harmonic

For the moment the following packages are skipped during the compilation:
- open_manipulator_x_teleop
- open_manipulator_x_playground
- open_manipulator_x_moveit_config
- open_manipulator_x_gui

because they are useless for our goals. For each package, in the CMakeLists.txt there is a variable called **SKIP_BUILD**:

```shell
set(SKIP_BUILD OFF) # Build the package
# set(SKIP_BUILD ON) # Doesn't build the package
```

**Dependences**:
- [MoveIt2](https://moveit.ai/install-moveit2/binary/) 
    - `sudo apt install ros-humble-moveit`

## Example test
-  move arm with **the trajectory/position controller**
```bash
------
```
-  move arm with **the effort controller**
```bash
ros2 topic pub /effort_controller/commands std_msgs/msg/Float64MultiArray '{data: [1.0, -0.5, 0.3, 0.0]}'
```

## Link 
### Gz (Gazebo)

**Information gives by manufacturer**

| Link        | Mass (kg)     | Ixx       | Ixy       | Ixz       | Iyy       | Iyz       | Izz       |
|------------|--------------|-----------|-----------|-----------|-----------|-----------|-----------|
| Link 1     | 0.079119962  | 1.2505e-05 | 0.0       | -1.7855e-07 | 2.1898e-05 | 0.0       | 1.9267e-05 |
| Link 2     | 0.098406837  | 3.4543e-05 | -1.6031e-08 | -3.8375e-07 | 3.2689e-05 | 2.8512e-08 | 1.8850e-05 |
| Link 3     | 0.13850917   | 3.3055e-04 | -9.7941e-08 | -3.8506e-05 | 3.4290e-04 | -1.5718e-06 | 6.0346e-05 |
| Link 4     | 0.13274562   | 3.0654e-05 | -1.2764e-06 | -2.6874e-07 | 2.4230e-04 | 1.1559e-08 | 2.5155e-04 |
| Link 5     | 0.14327573   | 8.0871e-05 | 0.0       | -1.0158e-06 | 7.5980e-05 | 0.0       | 9.3127e-05 |
| Gripper L  | 0.001        | 1.0e-06   | 0.0       | 0.0       | 1.0e-06   | 0.0       | 1.0e-06   |
| Gripper R  | 0.001        | 1.0e-06   | 0.0       | 0.0       | 1.0e-06   | 0.0       | 1.0e-06   |

Our computation of the inertia:
🚧 WIP 🚧


## Joint limits
### Gz (Gazebo)

| Joint      | Max velocity (rad/s) | Effort (Nm) | Lower Limit (rad) | Upper Limit (rad) |
|------------|----------------|-------------|-------------------|-------------------|
| Joint 1    | 4.8            | 1           | -3.14             | 3.14              |
| Joint 2    | 4.8            | 1           | -1.5              | 1.5               |
| Joint 3    | 4.8            | 1           | -1.5              | 1.4               |
| Joint 4    | 4.8            | 1           | -1.7              | 1.97              |
| Gripper    | 4.8            | 1           | -0.010            | 0.019             |




### TODO:
- [ ] Resolve problem  `[Err] [Physics.cc:1785] Attempting to create a mimic constraint for joint [gripper_right_joint] but the chosen physics engine does not support mimic constraints, so no constraint will be created.`
    -   see [this example](https://github.com/gazebosim/gz-sim/blob/gz-sim8/examples/worlds/mimic_fast_slow_pendulums_world.sdf)
- [ ] Add torque control on the gripper
- [ ] Implement the torque control for the real hardware
- [ ] Do the porting of the following package:
    - [ ] open_manipulator_x_teleop
    - [ ] open_manipulator_x_playground
    - [ ] open_manipulator_x_moveit_config
    - [ ] open_manipulator_x_gui
- [ ] Remove dependence custom gz_ros2_control when this [PR](https://github.com/ros-controls/gz_ros2_control/pull/515#issuecomment-2749199964) will add the next version (current there is 2.0.6)

# ROBOTIS e-Manual for OpenMANIPULATOR-X
- [http://emanual.robotis.com/docs/en/platform/openmanipulator/](http://emanual.robotis.com/docs/en/platform/openmanipulator/)

# Open Source related to OpenMANIPULATOR-X
- [open_manipulator](https://github.com/ROBOTIS-GIT/open_manipulator)
- [open_manipulator_y](https://github.com/ROBOTIS-GIT/open_manipulator_y)
- [open_manipulator_p](https://github.com/ROBOTIS-GIT/open_manipulator_p)
- [dynamixel_sdk](https://github.com/ROBOTIS-GIT/DynamixelSDK)
- [dynamixel_workbench](https://github.com/ROBOTIS-GIT/dynamixel-workbench)
- [dynamixel_hardware_interface](https://github.com/ROBOTIS-GIT/dynamixel_hardware_interface)

# Documents and Videos related to OpenMANIPULATOR-X
- [ROBOTIS e-Manual for OpenMANIPULATOR-X](http://emanual.robotis.com/docs/en/platform/openmanipulator/)
- [ROBOTIS e-Manual for OpenMANIPULATOR-P](https://emanual.robotis.com/docs/en/platform/openmanipulator_p/overview/)
- [ROBOTIS e-Manual for DYNAMIXEL SDK](http://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_sdk/overview/)
- [ROBOTIS e-Manual for DYNAMIXEL Workbench](http://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_workbench/)
- [YouTube Play List for OpenMANIPULATOR](https://www.youtube.com/playlist?list=PLRG6WP3c31_WpEsB6_Rdt3KhiopXQlUkb)
