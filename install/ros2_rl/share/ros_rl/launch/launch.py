from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()
    
    test_node = Node(package="ros_rl", executable="test_node")
    
    ld.add_action(test_node)
    
    return ld


