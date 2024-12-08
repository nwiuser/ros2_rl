from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()
    
    talker_node = Node(package="demo_nodes_cpp", executable="talker")
    
    ld.add_action(talker_node)
    
    return ld


