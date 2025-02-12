#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, Point
from turtlesim.msg import Pose
from letters_drawing_2.msg import TurtleInfo
import math

kp = 0.5

class TurtleSubscriber(Node):
    def __init__(self):
        super().__init__('turtle_subscriber')
        self.create_subscription(TurtleInfo, 'turtle_info', self.turtle_info_callback, 10)
        self.create_subscription(Pose, '/Turtle_1/pose', self.pose_callback, 10)
        self.publisher_ = self.create_publisher(Twist, '/Turtle_1/cmd_vel', 10)
        self.current_pose = Pose()

    def turtle_info_callback(self, msg: TurtleInfo):
        global kp
        target_coords = msg.target_coords
        self.get_logger().info(f"Received message: {msg}")

        # Calculate error
        dx = target_coords.x - self.current_pose.x
        dy = target_coords.y - self.current_pose.y
        angle_to_target = math.atan2(dy, dx)
        angular_error = angle_to_target - self.current_pose.theta

        # Proportional control
        vel_msg = Twist()

        # Calculate angular speed to rotate towards target
        vel_msg.angular.z = kp * angular_error  # Proportional controller for angular speed

        # Calculate linear speed based on distance "Vethagorth"
        distance = math.sqrt(dx**2 + dy**2)
        vel_msg.linear.x = kp * distance  # Proportional controller for linear speed

        # Publish the velocity command
        self.publisher_.publish(vel_msg)

    def pose_callback(self, msg: Pose):
        self.current_pose = msg

def main(args=None):
    rclpy.init(args=args)
    node = TurtleSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
