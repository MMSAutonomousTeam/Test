#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.srv import SetPen
from turtlesim.srv import Spawn
from functools import partial
import time
printed = True
class NameDrawingE_Node(Node) :
    def __init__(self) :
        super().__init__("draw_e")
        self.time_needed = 0.0 
        self.cmd_vel_publisherE_ = self.create_publisher(Twist , "/LetterETurtle/cmd_vel" , 10)
        global printed
        if printed :
            self.spawnturtle_request()
            printed = False


    def cmd_vel_publisherE_func(self):
        msg_ = Twist()
        msg_.linear.x = 1.0
        msg_.angular.z =  0.0
        self.cmd_vel_publisherE_.publish(msg_)
        time.sleep(1.0)
        msg2_ = Twist()
        msg2_.linear.x = 0.0
        msg2_.angular.z = -1.57079632679
        self.cmd_vel_publisherE_.publish(msg2_)
        time.sleep(1.0)

        msg = Twist()
        msg.linear.x = 2.0
        msg.angular.z = 0.0
        self.cmd_vel_publisherE_.publish(msg)
        time.sleep(1.0)
        msg2 = Twist()
        msg2.linear.x = 0.0
        msg2.angular.z = -1.57079632679
        self.cmd_vel_publisherE_.publish(msg2)
        time.sleep(1.0)
        msg3 = Twist()
        msg3.linear.x = 1.0
        msg3.angular.z = 0.0
        self.cmd_vel_publisherE_.publish(msg3)
        time.sleep(1.0)
        msg4 = Twist()
        msg4.linear.x = 0.0
        msg4.angular.z =  -1.57079632679
        self.cmd_vel_publisherE_.publish(msg4)
        time.sleep(1.0)       
        msg5 = Twist()
        msg5.linear.x = 1.0
        msg5.angular.z = 0.0

        self.cmd_vel_publisherE_.publish(msg5)
        time.sleep(1.0)
        msg6 = Twist()
        msg6.linear.x = 0.0
        msg6.angular.z = -1.57079632679  
        self.cmd_vel_publisherE_.publish(msg6)
        time.sleep(1.0)
        msg7 = Twist()
        msg7.linear.x = 1.0
        msg7.angular.z = 0.0
        self.cmd_vel_publisherE_.publish(msg7)
        time.sleep(1.0)
        msg8 = Twist()
        msg8.linear.x = 0.0
        msg8.angular.z = 3.14159265359
        self.cmd_vel_publisherE_.publish(msg8)
        time.sleep(1.0)
        msg9 = Twist()
        msg9.linear.x = 1.4
        msg9.angular.z = 0.0
        self.cmd_vel_publisherE_.publish(msg9)
        time.sleep(1.0)

    def spawnturtle_request(self):
        client = self.create_client(Spawn ,"/spawn")
        self.get_logger().info("Waiting for turtle to spawn ......")
        client.wait_for_service()
        request = Spawn.Request()
        request.x = 7.5
        request.y = 3.5
        request.theta = 3.14159265359
        request.name = "LetterETurtle"
        future = client.call_async(request)
        future.add_done_callback(partial(self.callback_spawn))

    def callback_spawn(self , future) :
        try :
            res = future.result()
            self.call_set_pen_service()
            self.get_logger().info("Turtle Spawned successfully !!!!!")
        except Exception as e :
            self.get_logger().error(f"Service failed: {e}")        
 
    def call_set_pen_service(self) :
        client = self.create_client(SetPen , "/LetterETurtle/set_pen")
        self.get_logger().warn("Waiting for service ....")
        req = SetPen.Request()
        req.r = 0
        req.g = 255
        req.b = 255
        req.width = 7
        req.off = 0 

        future_ = client.call_async(req)
        future_.add_done_callback(partial(self.callback_set_pen))

    def callback_set_pen(self,future_):
        try :
            res = future_.result()
            self.cmd_vel_publisherE_func()
        except Exception as e :
            self.get_logger().error("Service Failed : %r % (e,)")       



def main(args=None):
    rclpy.init(args=args)
    node = NameDrawingE_Node()
    rclpy.spin(node)
    rclpy.shutdown()