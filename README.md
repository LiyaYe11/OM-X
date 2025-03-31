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

## Joint limits

| Joint   | Min   | Max   |
|---------|-------|-------|
| Joint 1 | -3.14 |  3.14 |
| Joint 2 | -1.5  |  1.5  |
| Joint 3 | -1.5  |  1.4  |
| Joint 4 | -1.7  |  1.97 |


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
