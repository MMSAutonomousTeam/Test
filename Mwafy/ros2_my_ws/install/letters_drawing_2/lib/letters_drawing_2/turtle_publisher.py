#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import Point
from letters_drawing_2.msg import TurtleInfo
from turtlesim.srv import Spawn
from turtlesim.srv import Kill
from collections import deque
import random
import time
from functools import partial
printed = True

class TurtlePublisher(Node):
    def __init__(self):
        super().__init__('turtle_publisher')
        self.publisher_ = self.create_publisher(TurtleInfo, 'turtle_info', 10)
        self.get_logger().info('Node started. Waiting for user input.')
        self.queue = deque(maxlen=5)  # Create a deque with max size of 5

        global printed
        if printed :
            self.spawnturtle_request()
            printed = False
        self.timer = self.create_timer(1.0, self.publish_message)  # Publish every second

    def process_string(self, input_string):
        for char in input_string:
            self.queue.append(char)  # Add character to the queue
            self.get_logger().info(f"Current Queue: {list(self.queue)}")  # Log the current state of the queue

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
        request.x = 0.5
        request.y = 0.5
        request.theta = 1.5
        request.name = "Turtle_1"
        future = client.call_async(request)
        future.add_done_callback(partial(self.callback_spawn))

    def callback_spawn(self , future) :
        try :
            res = future.result()
            self.killturtle_request()
            self.spawnturtle2_request()
            self.get_logger().info("Turtle Spawned successfully !!!!!")
        except Exception as e :
            self.get_logger().error(f"Service failed: {e}")  


    def spawnturtle2_request(self):
        client = self.create_client(Spawn ,"/spawn")
        self.get_logger().info("Waiting for turtle to spawn ......")
        client.wait_for_service()
        request = Spawn.Request()
        request.x = 2.5
        request.y = 0.5
        request.theta = 1.5
        request.name = "Turtle_2"
        future2 = client.call_async(request)
        future2.add_done_callback(partial(self.callback2_spawn))

    def callback2_spawn(self , future2) :
        try :
            res = future2.result()
            self.spawnturtle3_request()
            self.get_logger().info("Turtle Spawned successfully !!!!!")
        except Exception as e :
            self.get_logger().error(f"Service failed: {e}")

    def spawnturtle3_request(self):
        client = self.create_client(Spawn ,"/spawn")
        self.get_logger().info("Waiting for turtle to spawn ......")
        client.wait_for_service()
        request = Spawn.Request()
        request.x = 4.5
        request.y = 0.5
        request.theta = 1.5
        request.name = "Turtle_3"
        future3 = client.call_async(request)
        future3.add_done_callback(partial(self.callback3_spawn))

    def callback3_spawn(self , future3) :
        try :
            res = future3.result()
            self.spawnturtle4_request()
            self.get_logger().info("Turtle Spawned successfully !!!!!")
        except Exception as e :
            self.get_logger().error(f"Service failed: {e}")  

    def spawnturtle4_request(self):
        client = self.create_client(Spawn ,"/spawn")
        self.get_logger().info("Waiting for turtle to spawn ......")
        client.wait_for_service()
        request = Spawn.Request()
        request.x = 6.5
        request.y = 0.5
        request.theta = 1.5
        request.name = "Turtle_4"
        future4 = client.call_async(request)
        future4.add_done_callback(partial(self.callback4_spawn))

    def callback4_spawn(self , future4) :
        try :
            res = future4.result()
            self.spawnturtle5_request()
            self.get_logger().info("Turtle Spawned successfully !!!!!")
        except Exception as e :
            self.get_logger().error(f"Service failed: {e}")  

    def spawnturtle5_request(self):
        client = self.create_client(Spawn ,"/spawn")
        self.get_logger().info("Waiting for turtle to spawn ......")
        client.wait_for_service()
        request = Spawn.Request()
        request.x = 8.5
        request.y = 0.5
        request.theta = 1.5
        request.name = "Turtle_5"
        future5= client.call_async(request)
        future5.add_done_callback(partial(self.callback5_spawn))

    def callback5_spawn(self , future5) :
        try :
            res = future5.result()
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
    input_string = input("Enter a string: ")
    node = TurtlePublisher()
    node.process_string(input_string)
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
