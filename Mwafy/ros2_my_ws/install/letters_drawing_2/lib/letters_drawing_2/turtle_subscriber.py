#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, Point
from turtlesim.msg import Pose
from letters_drawing_2.msg import TurtleInfo
import math

kp = 1.0

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
        self.create_subscription(Pose, '/Turtle_3/pose', self.pose_callback2, 10)
        self.publisher2_ = self.create_publisher(Twist, '/Turtle_3/cmd_vel', 10)
        self.current_pose2 = Pose()
        self.create_subscription(Pose, '/Turtle_4/pose', self.pose_callback3, 10)
        self.publisher3_ = self.create_publisher(Twist, '/Turtle_4/cmd_vel', 10)
        self.current_pose3 = Pose()
        self.create_subscription(Pose, '/Turtle_5/pose', self.pose_callback4, 10)
        self.publisher4_ = self.create_publisher(Twist, '/Turtle_5/cmd_vel', 10)
        self.current_pose4 = Pose()

    def turtle_info_callback(self, msg: TurtleInfo):
        global kp
        target_coords = msg.target_coords
        self.get_logger().info(f"Received message: {msg}")
        if msg.turtle_name == "Turtle_1" :
            pose = self.current_pose
        elif msg.turtle_name == "Turtle_2" :
            pose = self.current_pose1
        elif msg.turtle_name == "Turtle_3" :
            pose = self.current_pose2
        elif msg.turtle_name == "Turtle_4" :
            pose = self.current_pose3
        elif msg.turtle_name == "Turtle_5" :
            pose = self.current_pose4
        else :
            pass

        vel_msg = Twist()        
        # Calculate error
        dx = target_coords.x - pose.x
        dy = target_coords.y - pose.y
        # Calculate linear speed based on distance "Vethagorth"
        distance = math.sqrt(dx**2 + dy**2)
        vel_msg.linear.x = kp * distance  # Proportional controller for linear speed
        angle_to_target = math.atan2(dy, dx)
        angular_error = angle_to_target - pose.theta

        input_value = vel_msg.linear.x
        input_range = (0, 10)
        output_range = (0, 5)

        #yarab tenf3 b2a
        vel_msg.linear.x = self.map_range(input_value, input_range[0], input_range[1], output_range[0], output_range[1])

        # Calculate angular spesed to rotate towards target
        vel_msg.angular.z = kp * angular_error  # Proportional controller for angular speed
       
        if abs(angular_error) >= 0.03 :
            vel_msg.linear.x= 0.0
        # Proportional control      

        if msg.turtle_name == "Turtle_1" :
            self.publisher_.publish(vel_msg)
        elif msg.turtle_name == "Turtle_2" :
            self.publisher1_.publish(vel_msg)
        elif msg.turtle_name == "Turtle_3" :
            self.publisher2_.publish(vel_msg)
        elif msg.turtle_name == "Turtle_4" :
            self.publisher3_.publish(vel_msg)
        elif msg.turtle_name == "Turtle_5" :
            self.publisher4_.publish(vel_msg)

    def map_range(self,x, in_min, in_max, out_min, out_max):
        return (x - in_min) / (in_max - in_min) * (out_max - out_min) + out_min


    def pose_callback(self, msg: Pose):
        self.current_pose = msg
    def pose_callback1(self, msg: Pose):
        self.current_pose1 = msg
    def pose_callback2(self, msg: Pose):
        self.current_pose2 = msg
    def pose_callback3(self, msg: Pose):
        self.current_pose3 = msg
    def pose_callback4(self, msg: Pose):
        self.current_pose4 = msg

def main(args=None):
    rclpy.init(args=args)
    node = TurtleSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
'''
import math
from geometry_msgs.msg import Twist

global kp
target_coords = msg.target_coords
self.get_logger().info(f"Received message: {msg}")

if msg.turtle_name == "Turtle_1":
    pose = self.current_pose
elif msg.turtle_name == "Turtle_2":
    pose = self.current_pose1

vel_msg = Twist()

# Calculate error
dx = target_coords.x - pose.x
dy = target_coords.y - pose.y
distance = math.sqrt(dx**2 + dy**2)

# Linear velocity based on distance
vel_msg.linear.x = kp * distance  # Proportional control for linear speed

# Calculate angle to target and angular error
angle_to_target = math.atan2(dy, dx)
angular_error = angle_to_target - pose.theta

# Normalize angular error to be between -pi and pi
angular_error = math.atan2(math.sin(angular_error), math.cos(angular_error))

# When rotating, don't apply linear velocity, only angular
if angular_error > 0.0:
    vel_msg.linear.x = 0.0

# Proportional controller for angular speed
vel_msg.angular.z = kp * angular_error

# Check if close to target and within threshold for both distance and angular error
if distance < 0.4 and abs(angular_error) < 0.4:
    vel_msg.linear.x = 0.0
    vel_msg.angular.z = 0.0  # Stop both linear and angular velocity when close to the target

# Publish velocities based on the turtle's name
if msg.turtle_name == "Turtle_1":
    self.publisher_.publish(vel_msg)
elif msg.turtle_name == "Turtle_2":
    self.publisher1_.publish(vel_msg)

'''