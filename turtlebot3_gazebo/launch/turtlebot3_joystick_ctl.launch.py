#!/usr/bin/env python3
#
# Copyright 2019 ROBOTIS CO., LTD.
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
# Authors: Joep Tool

from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    
    joystick_node_cmd = Node(
        package='joystick_node',
        executable='joystick_node',
        name='joystick_node',
        output='screen',
        parameters=[{
            'joystick_type': 'ps5',
            'joystick_device': '/dev/input/js0',
            'joystick_bits': 16
        }],
        remappings=[
            ('/joystick_msg', '/robot_control/joystick_msgs'),
            # ('cmd_vel', '/cmd_vel')
        ]
    )
    
    joystick_to_cmdvel_node_cmd = Node(
        package='joystick_to_cmdvel',
        executable='joystick_to_cmdvel_node',
        name='joystick_to_cmdvel_node',
        output='screen',
        remappings=[
            ('joy', '/robot_control/joystick_msgs'),
            ('cmd_vel', '/cmd_vel')
        ]
    )

    ld = LaunchDescription()

    # Add the commands to the launch description
    ld.add_action(joystick_node_cmd)
    ld.add_action(joystick_to_cmdvel_node_cmd)

    return ld
