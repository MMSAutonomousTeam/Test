#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, Point
from turtlesim.msg import Pose
from letters_drawing_2.msg import TurtleInfo
import math

kp = 1.09

class TurtleSubscriber(Node):
    def __init__(self):
        super().__init__('turtle_subscriber')
        self.create_subscription(TurtleInfo, 'turtle_info', self.turtle_info_callback, 10)
        self.create_subscription(Pose, '/Turtle_1/pose', self.pose_callback, 10)
        self.publisher_ = self.create_publisher(Twist, '/Turtle_1/cmd_vel', 10)
        self.current_pose = Pose()
        self.create_subscription(Pose, '/Turtle_2/pose', self.pose_callback1, 10)
        self.publisher1_ = self.create_publisher(Twist, '/Turtle_2/cmd_vel', 10)
        self.current_pose1 = Pose()

    def turtle_info_callback(self, msg: TurtleInfo):
        global kp
        target_coords = msg.target_coords
        self.get_logger().info(f"Received message: {msg}")
        if msg.turtle_name == "Turtle_1" :
            pose = self.current_pose
        elif msg.turtle_name == "Turtle_2" :
            pose = self.current_pose1
            

        vel_msg = Twist()

        # Calculate error
        dx = target_coords.x - pose.x
        dy = target_coords.y - pose.y
        # Calculate linear speed based on distance "Vethagorth"
        distance = math.sqrt(dx**2 + dy**2)
        vel_msg.linear.x = kp * distance  # Proportional controller for linear speed
        angle_to_target = math.atan2(dy, dx)
        angular_error = angle_to_target - pose.theta
        if angular_error > 0.0 :
            vel_msg.linear.x= 0.0
        # Proportional control
    
        # Calculate angular spesed to rotate towards target
        vel_msg.angular.z = kp * angular_error  # Proportional controller for angular speed

        if angular_error > 0.4 :
            vel_msg.linear.x= 0.0
        if distance < 0.4  and angular_error <= 0.4 :
            vel_msg.linear.x = 0.0
            vel_msg.angular.z = 0.0# Proportional controller for angular speed
        else :
            pass

        if msg.turtle_name == "Turtle_1" :
            self.publisher_.publish(vel_msg)

        elif msg.turtle_name == "Turtle_2" :
            self.publisher1_.publish(vel_msg)

    def pose_callback(self, msg: Pose):
        self.current_pose = msg
    def pose_callback1(self, msg: Pose):
        self.current_pose1 = msg

def main(args=None):
    rclpy.init(args=args)
    node = TurtleSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
