#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.srv import SetPen
from turtlesim.srv import Spawn
from functools import partial
import time
printed = True
class NameDrawingD_Node(Node) :
    def __init__(self) :
        super().__init__("draw_D")
        self.time_needed = 0.0 
        self.cmd_vel_publisherD_ = self.create_publisher(Twist , "/LetterDTurtle/cmd_vel" , 10)
        global printed
        if printed :
            self.spawnturtle_request()
            printed = False


    def cmd_vel_publisherD_func(self):
        msg = Twist()
        msg.linear.x = 3.0
        msg.angular.z = 0.0
        self.cmd_vel_publisherD_.publish(msg)
        time.sleep(1.0)
        msg2 = Twist()
        msg2.linear.x = 0.0
        msg2.angular.z = -1.57079632679
        self.cmd_vel_publisherD_.publish(msg2)
        time.sleep(1.0)
        msg3 = Twist()
        msg3.linear.x = 1.0
        msg3.angular.z = 0.0
        self.cmd_vel_publisherD_.publish(msg3)
        time.sleep(1.0)
        msg4 = Twist()
        msg4.linear.x = 0.0
        msg4.angular.z =  -1.57079632679
        self.cmd_vel_publisherD_.publish(msg4)
        time.sleep(1.0)       
        msg5 = Twist()
        msg5.linear.x = 1.0
        msg5.angular.z = 0.0

        self.cmd_vel_publisherD_.publish(msg5)
        time.sleep(1.0)
        msg6 = Twist()
        msg6.linear.x = 0.0
        msg6.angular.z = -1.57079632679
        self.cmd_vel_publisherD_.publish(msg6)
        time.sleep(1.0)
        msg7 = Twist()
        msg7.linear.x = 1.65
        msg7.angular.z = 0.0
        self.cmd_vel_publisherD_.publish(msg7)

    def spawnturtle_request(self):
        client = self.create_client(Spawn ,"/spawn")
        self.get_logger().info("Waiting for turtle to spawn ......")
        client.wait_for_service()
        request = Spawn.Request()
        request.x = 9.5
        request.y = 6.5
        request.theta = -1.57079632679
        request.name = "LetterDTurtle"
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
        client = self.create_client(SetPen , "/LetterDTurtle/set_pen")
        self.get_logger().warn("Waiting for service ....")
        req = SetPen.Request()
        req.r = 255
        req.g = 0
        req.b = 255
        req.width = 7
        req.off = 0 

        future_ = client.call_async(req)
        future_.add_done_callback(partial(self.callback_set_pen))

    def callback_set_pen(self,future_):
        try :
            res = future_.result()
            self.cmd_vel_publisherD_func()
        except Exception as e :
            self.get_logger().error("Service Failed : %r % (e,)")       



def main(args=None):
    rclpy.init(args=args)
    node = NameDrawingD_Node()
    rclpy.spin(node)
    rclpy.shutdown()