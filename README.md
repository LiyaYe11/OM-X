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
