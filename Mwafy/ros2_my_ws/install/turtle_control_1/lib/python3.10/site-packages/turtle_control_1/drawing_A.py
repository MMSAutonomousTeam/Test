#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.srv import SetPen
from turtlesim.srv import Spawn
from turtlesim.srv import Kill
from functools import partial
import time
printed = True

class NameDrawingNode(Node) :
    def __init__(self) :
        super().__init__("drawing_A")
        self.time_needed = 0.0 
        self.cmd_vel_publisherA_ = self.create_publisher(Twist , "/LetterATurtle/cmd_vel" , 10)
        global printed
        if printed :
            self.spawnturtle_request()
            printed = False


    def cmd_vel_publisherA_func(self):
        msg = Twist()
        msg.linear.x = 6.0
        msg.angular.z = 0.0
        self.cmd_vel_publisherA_.publish(msg)
        time.sleep(1.0)
        msg2 = Twist()
        msg2.linear.x = 0.0
        msg2.angular.z = -2.8
        self.cmd_vel_publisherA_.publish(msg2)
        time.sleep(1.0)
        msg3 = Twist()
        msg3.linear.x = 6.0
        msg3.angular.z = 0.0
        self.cmd_vel_publisherA_.publish(msg3)
        time.sleep(1.0)
        msg4 = Twist()
        msg4.linear.x = 0.0
        msg4.angular.z = 3.14159265359
        self.cmd_vel_publisherA_.publish(msg4)
        time.sleep(1.0)       
        msg5 = Twist()
        msg5.linear.x = 2.5
        msg5.angular.z = 0.0
        self.cmd_vel_publisherA_.publish(msg5)
        time.sleep(1.0)
        msg6 = Twist()
        msg6.linear.x = 0.0
        msg6.angular.z = 1.2
        self.cmd_vel_publisherA_.publish(msg6)
        time.sleep(1.0)
        msg7 = Twist()
        msg7.linear.x = 1.5
        msg7.angular.z = 0.0
        self.cmd_vel_publisherA_.publish(msg7)
        time.sleep(1.0)



    def spawnturtle_request(self):
        client = self.create_client(Spawn ,"/spawn")
        self.get_logger().info("Waiting for turtle to spawn ......")
        client.wait_for_service()
        request = Spawn.Request()
        request.x = 1.0
        request.y = 1.0
        request.theta = 1.5
        request.name = "LetterATurtle"
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
            self.call_set_pen_service()
            self.get_logger().info("Turtle Spawned successfully !!!!!")
        except Exception as e :
            self.get_logger().error(f"Service failed: {e}")        
 
 
    def call_set_pen_service(self) :
        client = self.create_client(SetPen , "/LetterATurtle/set_pen")
        self.get_logger().warn("Waiting for service ....")
        req = SetPen.Request()
        req.r = 255
        req.g = 0
        req.b = 0
        req.width = 7
        req.off = 0 

        future__ = client.call_async(req)
        future__.add_done_callback(partial(self.callback_set_pen))

    def callback_set_pen(self,future__):
        try :
            res = future__.result()
            self.cmd_vel_publisherA_func()
        except Exception as e :
            self.get_logger().error("Service Failed : %r % (e,)")       



def main(args=None):
    rclpy.init(args=args)
    node = NameDrawingNode()
    rclpy.spin(node)
    rclpy.shutdown()