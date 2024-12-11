import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class RobotController(Node):
    def __init__(self):
        super().__init__('robot_controller')

        # Publisher to send velocity commands to the robot
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)

        # Timer to periodically send commands
        self.timer_period = 0.1  # seconds
        self.timer = self.create_timer(self.timer_period, self.move_robot)

        # Command variables
        self.linear_velocity = 0.2  # m/s
        self.angular_velocity = 0.5  # rad/s

        self.get_logger().info('Robot controller node started')

    def move_robot(self):
        # Create a Twist message
        msg = Twist()

        # Set linear and angular velocities
        msg.linear.x = self.linear_velocity
        msg.linear.y = 0.0
        msg.linear.z = 0.0

        msg.angular.x = 0.0
        msg.angular.y = 0.0
        msg.angular.z = self.angular_velocity

        # Publish the message
        self.publisher_.publish(msg)
        self.get_logger().info(f'Published cmd_vel: linear={msg.linear.x}, angular={msg.angular.z}')

def main(args=None):
    rclpy.init(args=args)
    
    robot_controller = RobotController()
    rclpy.spin(robot_controller)

    # Cleanup
    robot_controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
