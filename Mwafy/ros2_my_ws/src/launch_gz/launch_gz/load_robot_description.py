import os
import rclpy
from rclpy.node import Node
from rclpy.parameter import Parameter
from ament_index_python.packages import get_package_share_directory

class RobotDescriptionPublisher(Node):
    def __init__(self):
        super().__init__('robot_description_publisher')

        # Get the package share directory using get_package_share_directory
        pkg_share_directory = get_package_share_directory('launch_gz')  # Change to your package name
        sdf_file = os.path.join(pkg_share_directory, 'models', 'rrbot', 'Mwafy_Robot.sdf')  # Update path to your model

        # Read the content of the SDF file
        with open(sdf_file, 'r') as infp:
            robot_desc = infp.read()

        # Declare and load the robot description into the parameter server
        self.declare_parameter('robot_description', '')
        self.get_parameter('robot_description').set_parameter(Parameter('robot_description', Parameter.Type.STRING, robot_desc))

        self.get_logger().info("Robot description loaded onto parameter server.")

def main(args=None):
    rclpy.init(args=args)
    node = RobotDescriptionPublisher()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
