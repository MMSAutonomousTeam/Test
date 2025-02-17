#!/usr/bin/env/python3

import rclpy
from rclpy.node import Node
from turtlesim.srv import Spawn, Kill, SetPen
from geometry_msgs.msg import Twist
import time

class my_name(Node):
    def __init__(self):
        super().__init__('my_name')
        
        # Create clients for spawning and killing turtles
        self.kill_client = self.create_client(Kill, '/kill')
        self.spawn_client = self.create_client(Spawn, '/spawn')
        self.vel_publishers = {}

        # Define turtles starting positions and colors
        turtles_data = [
           #( x ,  y  ,theta,  name ,    r ,  g ,  b )
            (0.5, 3.5, 0.0, 'A_turt' , 255,  0 ,  0 ),  # A - Red
            (2.7, 3.5, 0.0, 'R_turt' ,  0 , 255,  0 ),  # R - Green
            (4.9, 3.5, 0.0, 'A_turt2', 255, 255, 255),  # A - White
            (7.1, 3.5, 0.0, 'F_turt' , 255, 255,  0 ),  # F - Yellow
            (9.0, 3.5, 0.0, 'A_turt3',  0 ,  0 ,  0 ),  # A - Black
        ]

        # Spawn turtles, set pen colors and create publishers for each
        for x, y, theta, turtle_name, r, g, b in turtles_data:
            self.spawn_turt(x, y, theta, turtle_name)
            self.set_pen(r, g, b, turtle_name)
            self.creat_pup(turtle_name)
        
        # Kill the turtle that appears when the turtlesim is opened
        self.kill_turt('turtle1')
        
        # Draw each letter
        self.draw_A('A_turt' )
        self.draw_R('R_turt' )
        self.draw_A('A_turt2')
        self.draw_F('F_turt' )
        self.draw_A('A_turt3')

    def kill_turt(self, turtle_name):
        # To make sure this client done successfully
        if not self.kill_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().error("Kill service not available")

        request = Kill.Request()
        request.name = turtle_name

        future = self.kill_client.call_async(request)
        rclpy.spin_until_future_complete(self, future)
        if future.result():
            self.get_logger().info(f'Turtle "{turtle_name}" killed successfully!')
        else:
            self.get_logger().error(f'Failed to kill turtle {turtle_name}')

    def spawn_turt(self, x, y, theta, turtle_name):
        # To make sure this client done successfully
        if not self.spawn_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().error("Spaawn Service not available")

        request = Spawn.Request()
        request.x = x
        request.y = y
        request.theta = theta
        request.name = turtle_name

        future = self.spawn_client.call_async(request)
        rclpy.spin_until_future_complete(self, future)
        if future.result():
            self.get_logger().info(f'Turtle "{turtle_name}" spawned successfully!')
        else:
            self.get_logger().error('Failed to spawn turtle')

    def set_pen(self, r, g, b, turtle_name):
        # Create clients to set pen for each turtle
        self.setpen_client = self.create_client(SetPen, f'/{turtle_name}/set_pen')

        # To make sure this client done successfully
        if not self.setpen_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().error("SetPen service is not available")
        
        request = SetPen.Request()
        request.r = r
        request.g = g
        request.b = b
        request.width = 5
        request.off = 0   # 0 = pen on

        future = self.setpen_client.call_async(request)
        rclpy.spin_until_future_complete(self, future)

        if future.result():
            self.get_logger().info(f'Turtle "{turtle_name}" changed pen color successfully')
        else:
            self.get_logger().error(f'Turtle "{turtle_name}" failed to change pen color')

    def creat_pup(self, name):
        # Creates a velocity publisher (cmd_vel) for movement for each turtle topic
        self.vel_publishers[name] = self.create_publisher(Twist, f'/{name}/cmd_vel', 10)

    def draw_A(self, turtle_name):
        """ Draw the letter 'A' """
        self.move_turtle(turtle_name,  0.75 ,  4.0, 0.0) # Move diagonally up
        self.move_turtle(turtle_name,  0.375, -2.0, 0.0) # Move diagonally down
        self.move_turtle(turtle_name, -0.75 ,  0.0, 0.0) # Draw the crossbar
        self.move_turtle(turtle_name,  0.75 ,  0.0, 0.0) # Go back
        self.move_turtle(turtle_name,  0.375, -2.0, 0.0) # Move diagonally down

    def draw_R(self, turtle_name):
        """ Draw the letter 'R' """
        self.move_turtle(turtle_name,  0.0, 4.0,  0.0 )  # Move up
        self.move_turtle(turtle_name,  3.0, 0.0, -3.05)  # Draw the semicircle
        self.move_turtle(turtle_name, -1.3, 2.0,  0.0 )  # Move diagonally down

    def draw_F(self, turtle_name):
        """ Draw the letter 'F' """
        self.move_turtle(turtle_name,  0.0,  4.0, 0.0)  # Move up
        self.move_turtle(turtle_name,  1.5,  0.0, 0.0)  # Draw the top bar
        self.move_turtle(turtle_name, -1.5,  0.0, 0.0)  # Go back
        self.move_turtle(turtle_name,  0.0, -1.5, 0.0)  # Move down
        self.move_turtle(turtle_name,  1.5,  0.0, 0.0)  # Draw the bottom bar

    def move_turtle(self, turtle_name, linearx, lineary, angular):
        # create message and publishes velocity commands (cmd_vel) to move the turtle.
        msg = Twist()
        msg.linear.x = linearx
        msg.linear.y = lineary
        msg.angular.z = angular
        self.pub = self.vel_publishers[turtle_name]
        self.pub.publish(msg)
        
        time.sleep(1.5) # Small delay to conserve time, allowing the turtle to execute the required movements successfully

# Initialize ROS 2 and run the node
def main():
    rclpy.init()
    node = my_name()
    rclpy.spin_once(node)
    rclpy.shutdown()