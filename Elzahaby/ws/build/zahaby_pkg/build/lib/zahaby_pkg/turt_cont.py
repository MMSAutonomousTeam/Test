#!/usr/bin/env/python3

import rclpy
from rclpy.duration import Duration
from rclpy.node import Node
from turtlesim.srv import Spawn, Kill, SetPen
from geometry_msgs.msg import Twist

class turtle_node(Node):
    def __init__(self):
        super().__init__('turtle_node')
        self.spawn_client = self.create_client(Spawn, '/spawn')
        self.kill_client = self.create_client(Kill, '/kill')

        self.cmd_vel_publishers = {
            'z_turt': self.create_publisher(Twist, '/z_turt/cmd_vel', 10),
            'a_turt': self.create_publisher(Twist, '/a_turt/cmd_vel', 10),
            'h_turt': self.create_publisher(Twist, '/h_turt/cmd_vel', 10),
            'a_turt2': self.create_publisher(Twist, '/a_turt2/cmd_vel', 10),
            'b_turt': self.create_publisher(Twist, '/b_turt/cmd_vel', 10),
            'y_turt': self.create_publisher(Twist, '/y_turt/cmd_vel', 10),
        }


    def spawn_turt(self, x, y, theta, name):    
        if not self.spawn_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().error("Spaawn Service not available")

        request = Spawn.Request()
        request.x = x
        request.y = y
        request.theta = theta
        request.name = name

        future = self.spawn_client.call_async(request)
        rclpy.spin_until_future_complete(self, future)
        if future.result():
            self.get_logger().info(f'Turtle "{name}" spawned successfully!')
        else:
            self.get_logger().error('Failed to spawn turtle')
        
    def kill_turt(self, name):
        if not self.kill_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().error("Kill service not available")

        request = Kill.Request()
        request.name = name

        future = self.kill_client.call_async(request)
        rclpy.spin_until_future_complete(self, future)
        if future.result():
            self.get_logger().info(f'Turtle "{name}" killed successfully!')
        else:
            self.get_logger().error(f'Failed to kill turtle {name}')

    def set_pen(self, r, g, b, width, off, name):
        setpen_service = f'/{name}/set_pen'
        self.setpen_client = self.create_client(SetPen, setpen_service)

        if not self.setpen_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().error("SetPen service is not available")
        
        request = SetPen.Request()
        request.r = r
        request.g = g
        request.b = b
        request.width = width
        request.off = off

        future = self.setpen_client.call_async(request)
        rclpy.spin_until_future_complete(self, future)

        if future.result():
            self.get_logger().info(f'Turtle "{name}" changed pen color successfully')
        else:
            self.get_logger().error(f'Turtle "{name}" failed to change pen color')

    def stop_turt(self, publisher):
        stop_msg = Twist()
        publisher.publish(stop_msg)

    def move_for_duration(self, publisher, msg, duration):
        duration = Duration(seconds = duration)
        start_time = self.get_clock().now()
        
        while (self.get_clock().now() - start_time < duration):
            publisher.publish(msg)
        else:
            self.stop_turt(publisher)

    def draw_z(self, name):
        publisher = self.cmd_vel_publishers[name]
        msg = Twist()

        #straight
        msg.linear.x = 1.0
        self.move_for_duration(publisher, msg, 1.5)
        
        #diagonal
        msg.linear.x = 0.0
        msg.angular.z = -2.25
        self.move_for_duration(publisher, msg, 1.0)
        
        msg.linear.x = 1.0
        msg.angular.z = 0.0
        self.move_for_duration(publisher, msg, 2.2)
        
        #straight
        msg.linear.x = 0.0
        msg.angular.z = 2.25
        self.move_for_duration(publisher, msg, 1.0)

        msg.linear.x = 1.0
        msg.angular.z = 0.0
        self.move_for_duration(publisher, msg, 1.3)

    def draw_a(self, name):
        publisher = self.cmd_vel_publishers[name]
        msg = Twist()

        msg.linear.x = 1.0
        msg.angular.z = 0.0
        self.move_for_duration(publisher,msg, 2.0)

        msg.linear.x = 0.0
        msg.angular.z = -2.4
        self.move_for_duration(publisher, msg, 1.0)

        msg.linear.x = 1.0
        msg.angular.z = 0.0
        self.move_for_duration(publisher,msg, 2.0)

        msg.linear.x = -1.0
        msg.angular.z = 0.0
        self.move_for_duration(publisher,msg, 1.1)

        msg.linear.x = 0.0
        msg.angular.z = -1.97
        self.move_for_duration(publisher,msg, 1.0)

        msg.linear.x = 1.0
        msg.angular.z = 0.0
        self.move_for_duration(publisher,msg, 1.0)

    def draw_h(self, name):
        publisher = self.cmd_vel_publishers[name]
        msg = Twist()

        msg.linear.x = 1.0
        msg.angular.z  = 0.0
        self.move_for_duration(publisher, msg, 1.9)

        msg.linear.x = -1.0
        msg.angular.z  = 0.0
        self.move_for_duration(publisher, msg, 0.95)

        msg.linear.x = 0.0
        msg.linear.y = 1.0
        msg.angular.z  = 0.0
        self.move_for_duration(publisher, msg, 0.95)

        msg.linear.x = 1.0
        msg.linear.y = 0.0
        msg.angular.z  = 0.0
        self.move_for_duration(publisher, msg, 0.95)

        msg.linear.x = -1.0
        msg.angular.z  = 0.0
        self.move_for_duration(publisher, msg, 1.9)

    def draw_b(self, name):
        publisher = self.cmd_vel_publishers[name]
        msg = Twist()

        msg.linear.x = 1.0
        msg.angular.z = 0.0
        self.move_for_duration(publisher, msg, 2.0)

        msg.linear.x = 0.0
        msg.linear.y = 1.0
        self.move_for_duration(publisher, msg, 1.0)

        msg.linear.x = -1.0
        msg.linear.y = 0.0
        self.move_for_duration(publisher, msg, 1.0)

        msg.linear.x = 0.0
        msg.linear.y = -1.0
        self.move_for_duration(publisher, msg, 1.0)

        msg.linear.x = 0.0
        msg.linear.y = 1.0
        self.move_for_duration(publisher, msg, 1.0)

        msg.linear.x = -1.0
        msg.linear.y = 0.0
        self.move_for_duration(publisher, msg, 1.0)

        msg.linear.x = 0.0
        msg.linear.y = -1.0
        self.move_for_duration(publisher, msg, 1.0)

    def draw_y(self, name):
        publisher = self.cmd_vel_publishers[name]
        msg = Twist()

        msg.linear.x = 1.0
        msg.linear.y = 0.0
        self.move_for_duration(publisher, msg, 1.0)

        msg.linear.x = 0.0
        msg.angular.z = -0.65
        self.move_for_duration(publisher, msg, 1.0)

        msg.linear.x = 1.0
        msg.angular.z = 0.0
        self.move_for_duration(publisher, msg, 1.0)

        msg.linear.x = -1.0
        msg.angular.z = 0.0
        self.move_for_duration(publisher, msg, 1.0)

        msg.linear.x = 0.0
        msg.angular.z = 0.65
        self.move_for_duration(publisher, msg, 2.0)

        msg.linear.x = 1.0
        msg.angular.z = 0.0
        self.move_for_duration(publisher, msg, 1.0)

    def draw_name(self):
        self.draw_z('z_turt')
        self.draw_a('a_turt')
        self.draw_h('h_turt')
        self.draw_a('a_turt2')
        self.draw_b('b_turt')
        self.draw_y('y_turt')

def main():
    rclpy.init()
    node = turtle_node()

    node.kill_turt('turtle1')

    turtles = [
        (0.2, 7.0, 0.0, 'z_turt'),
        (2.0, 5.25, 1.2, 'a_turt'),
        (3.8, 7.15, 4.71239, 'h_turt'),
        (5.5, 5.25, 1.2, 'a_turt2'),
        (7.2, 7.0, 4.71239, 'b_turt'),
        (9.35, 5.25, 1.5708, 'y_turt')
    ]

    for x, y, theta, name in turtles:
        node.spawn_turt(x, y, theta, name)
        node.set_pen(255, 215, 0, 3, 0, name)

    node.draw_name()

    rclpy.spin(node)
    rclpy.shutdown()