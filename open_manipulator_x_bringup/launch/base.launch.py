#!/usr/bin/env python3
#
# Copyright 2024 ROBOTIS CO., LTD.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Author: Wonho Yoon, Sungho Woo

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import RegisterEventHandler
from launch.conditions import IfCondition
from launch.conditions import UnlessCondition
from launch.event_handlers import OnProcessExit
from launch.substitutions import Command
from launch.substitutions import FindExecutable
from launch.substitutions import LaunchConfiguration
from launch.substitutions import PathJoinSubstitution

from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    declared_arguments = []
    declared_arguments.append(
        DeclareLaunchArgument(
            'start_rviz',
            default_value='false',
            description='Whether execute rviz2'
        )
    )

    declared_arguments.append(
        DeclareLaunchArgument(
            'prefix',
            default_value='""',
            description='Prefix of the joint and link names'
        )
    )

    declared_arguments.append(
        DeclareLaunchArgument(
            'use_sim',
            default_value='true',
            description='Start robot in Gazebo simulation.'
        )
    )

    declared_arguments.append(
        DeclareLaunchArgument(
            'use_fake_hardware',
            default_value='false',
            description='Start robot with fake hardware mirroring command to its states.'
        )
    )

    declared_arguments.append(
        DeclareLaunchArgument(
            'fake_sensor_commands',
            default_value='false',
            description='Enable fake command interfaces for sensors used for simple simulations. \
            Used only if "use_fake_hardware" parameter is true.'
        )
    )

    declared_arguments.append(
        DeclareLaunchArgument(
            'port_name',
            default_value='/dev/ttyUSB0',
            description='The port name to connect to hardware.'
        )
    )

    declared_arguments.append(
        DeclareLaunchArgument(
            'description_package',
            default_value='open_manipulator_x_description',
            description='The name package that contains the XACRO files'
        )
    )

    declared_arguments.append(
        DeclareLaunchArgument(
            'xacro_folder',
            default_value='urdf',
            description='The folder name that contains the main xacro file'
        )
    )

    declared_arguments.append(
        DeclareLaunchArgument(
            'xacro_name',
            default_value='open_manipulator_x_robot.urdf.xacro',
            description='The name of the xacro file. Mandatory to add its extensions'
        )
    )

    declared_arguments.append(
        DeclareLaunchArgument(
            'enable_effort_controller',
            default_value='false',
            description='Enable the effort controller of arm \
                and disable position controller'
        )
    )

    declared_arguments.append(
        DeclareLaunchArgument(
            'enable_gripper_controller',
            default_value='true',
            description='Enable the gripper controller of arm'
        )
    )

    declared_arguments.append(
        DeclareLaunchArgument(
            'ic_joints',
            default_value='[0, 1.57, -1.57, 0]',
            description='Initial Conditions of the arm joints'
        )
    )


    start_rviz = LaunchConfiguration('start_rviz')
    prefix = LaunchConfiguration('prefix')
    use_sim = LaunchConfiguration('use_sim')
    use_fake_hardware = LaunchConfiguration('use_fake_hardware')
    fake_sensor_commands = LaunchConfiguration('fake_sensor_commands')
    port_name = LaunchConfiguration('port_name')
    description_package = LaunchConfiguration('description_package')
    xacro_folder = LaunchConfiguration('xacro_folder')
    xacro_name = LaunchConfiguration('xacro_name')
    ic_joints = LaunchConfiguration('ic_joints')


    urdf_file = Command(
        [
            PathJoinSubstitution([FindExecutable(name='xacro')]),
            ' ',
            PathJoinSubstitution(
                [
                    FindPackageShare(description_package),
                    xacro_folder,
                    xacro_name
                ]
            ),
            ' ',
            'prefix:=',
            prefix,
            ' ',
            'use_sim:=',
            use_sim,
            ' ',
            'use_fake_hardware:=',
            use_fake_hardware,
            ' ',
            'fake_sensor_commands:=',
            fake_sensor_commands,
            ' ',
            'port_name:=',
            port_name,
            ' ',    
            'ic_joints:=\'',
            ic_joints,
            '\''
        ]
    )

    controller_manager_config = PathJoinSubstitution(
        [
            FindPackageShare('open_manipulator_x_bringup'),
            'config',
            'hardware_controller_manager.yaml',
        ]
    )

    rviz_config_file = PathJoinSubstitution(
        [
            FindPackageShare('open_manipulator_x_bringup'),
            'rviz',
            'open_manipulator_x.rviz'
        ]
    )

    control_node = Node(
        package='controller_manager',
        executable='ros2_control_node',
        parameters=[
            {'robot_description': urdf_file, 'use_sim_time': use_sim},
            controller_manager_config
        ],
        output="both",
        condition=UnlessCondition(use_sim))

    robot_state_pub_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{'robot_description': urdf_file, 'use_sim_time': use_sim}],
        output='screen'
    )

    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        parameters=[{'use_sim_time': use_sim}],
        arguments=['-d', rviz_config_file],
        output='screen',
        condition=IfCondition(start_rviz)
    )

    joint_state_broadcaster_spawner = Node(
        package='controller_manager',
        executable='spawner',
        parameters=[{'use_sim_time': use_sim}],
        arguments=['joint_state_broadcaster', '--controller-manager', '/controller_manager'],
        output='screen',
    )

    arm_controller_spawner = Node(
        package='controller_manager',
        executable='spawner',
        parameters=[{'use_sim_time': use_sim}],
        arguments=['arm_controller'],
        output='screen',
        condition=UnlessCondition(LaunchConfiguration('enable_effort_controller'))
    )

    arm_controller_effort_spawner = Node(
        package='controller_manager',
        executable='spawner',
        parameters=[{'use_sim_time': use_sim}],
        arguments=['arm_controller_effort'],
        output='screen',
        condition=IfCondition(LaunchConfiguration('enable_effort_controller'))
    )

    gripper_controller_spawner = Node(
        package='controller_manager',
        executable='spawner',
        parameters=[{'use_sim_time': use_sim}],
        arguments=['gripper_controller'],
        output='screen',
        condition=IfCondition(LaunchConfiguration('enable_gripper_controller'))
    )

    delay_rviz_after_joint_state_broadcaster_spawner = RegisterEventHandler(
        event_handler=OnProcessExit(
            target_action=joint_state_broadcaster_spawner,
            on_exit=[rviz_node],
        )
    )

    delay_arm_controller_spawner_after_joint_state_broadcaster_spawner = \
        RegisterEventHandler(
            event_handler=OnProcessExit(
                target_action=joint_state_broadcaster_spawner,
                on_exit=[arm_controller_spawner],
            )
        )

    delay_arm_controller_spawner_effort_after_joint_state_broadcaster_spawner = \
        RegisterEventHandler(
            event_handler=OnProcessExit(
                target_action=joint_state_broadcaster_spawner,
                on_exit=[arm_controller_effort_spawner],
            )
        )

    delay_gripper_controller_spawner_after_joint_state_broadcaster_spawner = \
        RegisterEventHandler(
            event_handler=OnProcessExit(
                target_action=joint_state_broadcaster_spawner,
                on_exit=[gripper_controller_spawner],
            )
        )

    nodes = [
        control_node,
        robot_state_pub_node,
        joint_state_broadcaster_spawner,
        delay_rviz_after_joint_state_broadcaster_spawner,
        delay_arm_controller_spawner_after_joint_state_broadcaster_spawner,
        delay_arm_controller_spawner_effort_after_joint_state_broadcaster_spawner,
        delay_gripper_controller_spawner_after_joint_state_broadcaster_spawner,
    ]

    return LaunchDescription(declared_arguments + nodes)
