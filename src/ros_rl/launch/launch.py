from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='gazebo_ros',
            executable='gzserver',
            arguments=['--verbose', 'gazebo.world']
        ),
        Node(
            package='ros_rl',
            executable='robot_controller',
            name='robot_controller',
            parameters=[{'robot_description': 'robot.urdf'}]
        ),
    ])