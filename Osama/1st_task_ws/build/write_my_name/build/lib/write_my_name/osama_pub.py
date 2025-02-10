#!/usr/bin/env python3
import rclpy
from turtlesim.msg import Pose
from rclpy.node import Node
from geometry_msgs.msg import Twist

class Draw(Node):
    def __init__(self):
        super().__init__("name_writer")

        self.get_logger().info("im writing the name")
        self.publisher1 = self.create_publisher(Twist , "/turtle1/cmd_vel" , 10)
        self.timer1 = self.create_timer (1.0 , self.o_fun)
        self.s = 0
        self.publisher2= self.create_publisher(Twist , "/turtle2/cmd_vel" , 10)
        self.su2 = self.create_subscription(Pose,"/turtle2/pose",self.s_fun,10)
        self.a = False
        self.publisher3= self.create_publisher(Twist , "/turtle3/cmd_vel" , 10)
        self.publisher5= self.create_publisher(Twist , "/turtle5/cmd_vel" , 10)
        self.pub35 = self.create_subscription(Pose,"/turtle3/pose",self.a_fun,10)
        self.m = True
        self.publisher4= self.create_publisher(Twist , "/turtle4/cmd_vel" , 10)
        self.su4 = self.create_subscription(Pose,"/turtle4/pose",self.m_fun,10)
        
        


    def o_fun(self):
        snd = Twist()
        snd.linear.x = 3.0
        snd.angular.z = 3.0
        self.publisher1.publish(snd)

    def s_fun (self,pose:Pose):
        output = Twist()
        if pose.y <= 6.7 :
            output.linear.x = 0.0
            output.angular.z = 0.0
            self.s += 1

        elif self.s <= 0 and 6.5 < pose.y <= 7.57 :
            output.linear.x = 3.0
            output.angular.z = -6.0

        elif self.s <= 0 and pose.y > 7.5  :
            output.linear.x = 3.0
            output.angular.z = 6.0

        self.publisher2.publish(output)
        

    def a_fun(self,pose:Pose) :
        output2 = Twist()
        if pose.theta <= 1.57 :
            self.a = True
            
        if self.a == False :
            output2.linear.x = 3.0
            output2.angular.z = -6.0
        
        else :
            output2.linear.x = 6.0
            output2.angular.z = 6.0

        self.publisher3.publish(output2)
        self.publisher5.publish(output2)
    
    def m_fun(self,pose:Pose):
        output3 = Twist()
        if pose.x >= 8.49 :
                self.m = False
        if pose.y > 4.5 and -1.58 <= pose.theta <= -1.56 :
            output3.linear.x = 3.0
            output3.angular.z = 0.0
        
        elif pose.y <= 4.5 and pose.theta <= 1.57:      
            output3.linear.x = 0.0
            output3.angular.z = 1.0

        elif self.m == True :     
            output3.linear.x = 3.0
            output3.angular.z = -6.0
                
        self.publisher4.publish(output3)


        



def main(args=None):
    rclpy.init(args=args)
    node = Draw()
    rclpy.spin(node)
    rclpy.shutdown()