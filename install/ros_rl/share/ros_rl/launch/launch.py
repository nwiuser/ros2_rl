from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
        ),

        ExecuteProcess(
            cmd=['gz', 'launch', 'gazebo.world'],
            output='screen'
        ),
        
        Node(
            package='ros_rl',
            executable='robot',
            name='robot',
            parameters=[{'robot_description': 'robot.urdf'}]
        ),
    ])