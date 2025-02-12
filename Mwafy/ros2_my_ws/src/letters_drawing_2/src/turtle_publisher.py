#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import Point
from letters_drawing_2.msg import TurtleInfo
from turtlesim.srv import Spawn
from turtlesim.srv import Kill
import random
import time
from functools import partial
printed = True

class TurtlePublisher(Node):
    def __init__(self):
        super().__init__('turtle_publisher')
        self.publisher_ = self.create_publisher(TurtleInfo, 'turtle_info', 10)
        global printed
        if printed :
            self.spawnturtle_request()
            printed = False
        self.timer = self.create_timer(1.0, self.publish_message)  # Publish every second


    def publish_message(self):
        message = TurtleInfo()
        message.turtle_name = "Turtle_1"
        message.letter = "A"
        message.target_coords.x = random.uniform(0.0, 11.0)
        message.target_coords.y = random.uniform(0.0, 11.0)
        message.target_coords.z = 0.0

        self.publisher_.publish(message)
        self.get_logger().info(f'Published message: {message}')
           
           
    def spawnturtle_request(self):
        client = self.create_client(Spawn ,"/spawn")
        self.get_logger().info("Waiting for turtle to spawn ......")
        client.wait_for_service()
        request = Spawn.Request()
        request.x = 1.0
        request.y = 1.0
        request.theta = 1.5
        request.name = "Turtle_1"
        future = client.call_async(request)
        future.add_done_callback(partial(self.callback_spawn))

    def callback_spawn(self , future) :
        try :
            res = future.result()
            self.killturtle_request()
            self.get_logger().info("Turtle Spawned successfully !!!!!")
        except Exception as e :
            self.get_logger().error(f"Service failed: {e}")        
 
    def killturtle_request(self):
        client = self.create_client(Kill ,"/kill")
        self.get_logger().info("Waiting for turtle to spawn ......")
        client.wait_for_service()
        request = Kill.Request()
        request.name = "turtle1"
        future1 = client.call_async(request)
        future1.add_done_callback(partial(self.call_back_kill))

    def call_back_kill(self , future1) :
        try :
            res = future1.result()
            self.get_logger().info("Turtle Spawned successfully !!!!!")
        except Exception as e :
            self.get_logger().error(f"Service failed: {e}")   

def main(args=None):
    rclpy.init(args=args)
    node = TurtlePublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
