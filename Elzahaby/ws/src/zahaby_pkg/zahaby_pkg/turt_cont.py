#!/usr/bin/env/python3

import rclpy
from rclpy.node import Node
from turtlesim.srv import Spawn, Kill

class turtle_node(Node):
    def __init__(self):
        super().__init__('turtle_node')
        self.spawn_client = self.create_client(Spawn, '/spawn')
        self.kill_client = self.create_client(Kill, '/kill')

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

def main():
    rclpy.init()
    z_node = turtle_node()
    z_node.kill_turt('turtle1')
    z_node.spawn_turt(0.2, 7.0, 0.0, 'z_turt')

    a_node = turtle_node()
    a_node.spawn_turt(2.0, 5.0, 1.3, 'a_turt')

    h_node = turtle_node()
    h_node.spawn_turt(3.6, 7.0, 4.71239, 'h_turt')

    a_node2 = turtle_node()
    a_node2.spawn_turt(6.0, 5.0, 1.3, 'a_turt2')

    b_node = turtle_node()
    b_node.spawn_turt(8.0, 7.0, 4.71239, 'b_turt')

    y_node = turtle_node()
    y_node.spawn_turt(9.7, 5.0, 1.5708, 'y_turt')

    rclpy.spin(z_node)
    rclpy.spin(a_node)
    rclpy.spin(h_node)
    rclpy.spin(a_node2)
    rclpy.spin(b_node)
    rclpy.spin(y_node)

    rclpy.shutdown()