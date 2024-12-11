from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        
        Node(
            package='ros_rl',
            executable='robot',
            name='robot',
            parameters=[{'robot_description': 'robot.urdf'}]
        ),
    ])