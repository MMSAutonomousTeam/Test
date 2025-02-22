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
        self.step_index0 = 0
        self.timer = self.create_timer(1.0, self.publish_message1)  # Publish every second
        self.step_index1 = 0
        self.timer = self.create_timer(1.0, self.publish_message2)  # Publish every second
        self.step_index2 = 0
        self.timer = self.create_timer(1.0, self.publish_message3)  # Publish every second
        self.step_index3 = 0        
        self.timer = self.create_timer(1.0, self.publish_message4)  # Publish every second
        self.step_index4 = 0

    def process_string(self, input_string):
        for char in input_string:
            self.queue.append(char)  # Add character to the queue
            self.get_logger().info(f"Current Queue: {list(self.queue)}")  # Log the current state of the queue

    def publish_message(self):
        # Create message to be published
        self.step_index0 += 1
        message = TurtleInfo()
        message.turtle_name = "Turtle_1"
        message.letter = self.queue[0] 
        
        if(message.letter == 'A' or message.letter == 'a') :
            message = self.draw_A(message,0 ,self.step_index0)  # Modify the message to draw the letter "A"
        
        elif(message.letter == 'H' or message.letter == 'h') :
            message = self.draw_H(message,0,self.step_index0)  # Modify the message to draw the letter "H"

        elif(message.letter == 'M' or message.letter == 'm') :
            message = self.draw_M(message,0,self.step_index0)  # Modify the message to draw the letter "M"
        
        elif(message.letter == 'E' or message.letter == 'e') :
            message = self.draw_E(message,0,self.step_index0)  # Modify the message to draw the letter "E"

        elif(message.letter == 'Y' or message.letter == 'y') :
            message = self.draw_Y(message,0,self.step_index0)  # Modify the message to draw the letter "Y"
        elif(message.letter == 'D' or message.letter == 'd') :
            
            message = self.draw_D(message,0,self.step_index0)  # Modify the message to draw the letter "Y" 
        else :
            pass
        
            
        message.target_coords.z = 0.0

        self.publisher_.publish(message)

        self.get_logger().info(f'Published message: {message}')   
        
        
    def publish_message2(self):
        # Create message to be published
        self.step_index2 += 1
        message = TurtleInfo()
        message.turtle_name = "Turtle_3"
        message.letter = self.queue[2] 
        
        if(message.letter == 'A' or message.letter == 'a') :
            message = self.draw_A(message,2 ,self.step_index2)  # Modify the message to draw the letter "A"
        
        elif(message.letter == 'H' or message.letter == 'h') :
            message = self.draw_H(message,2,self.step_index2)  # Modify the message to draw the letter "H"

        elif(message.letter == 'M' or message.letter == 'm') :
            message = self.draw_M(message,2,self.step_index2)  # Modify the message to draw the letter "M"
        
        elif(message.letter == 'E' or message.letter == 'e') :
            message = self.draw_E(message,2,self.step_index2)  # Modify the message to draw the letter "E"

        elif(message.letter == 'Y' or message.letter == 'y') :
            message = self.draw_Y(message,2,self.step_index2)  # Modify the message to draw the letter "Y"
        elif(message.letter == 'D' or message.letter == 'd') :
            
            message = self.draw_D(message,2,self.step_index2)  # Modify the message to draw the letter "Y" 
        else :
            pass
        
            
        message.target_coords.z = 0.0

        self.publisher_.publish(message)

        self.get_logger().info(f'Published message: {message}')
    def publish_message3(self):
        # Create message to be published
        self.step_index3 += 1
        message = TurtleInfo()
        message.turtle_name = "Turtle_4"
        message.letter = self.queue[3] 
        
        if(message.letter == 'A' or message.letter == 'a') :
            message = self.draw_A(message,3 ,self.step_index3)  # Modify the message to draw the letter "A"
        
        elif(message.letter == 'H' or message.letter == 'h') :
            message = self.draw_H(message,3,self.step_index3)  # Modify the message to draw the letter "H"

        elif(message.letter == 'M' or message.letter == 'm') :
            message = self.draw_M(message,3,self.step_index3)  # Modify the message to draw the letter "M"
        
        elif(message.letter == 'E' or message.letter == 'e') :
            message = self.draw_E(message,3,self.step_index3)  # Modify the message to draw the letter "E"

        elif(message.letter == 'Y' or message.letter == 'y') :
            message = self.draw_Y(message,3,self.step_index3)  # Modify the message to draw the letter "Y"
        elif(message.letter == 'D' or message.letter == 'd') :
            message = self.draw_D(message,3,self.step_index3)  # Modify the message to draw the letter "Y" 
        else :
            pass
        
            
        message.target_coords.z = 0.0

        self.publisher_.publish(message)

        self.get_logger().info(f'Published message: {message}')
   
    def publish_message4(self):
        # Create message to be published
        self.step_index4 += 1
        message = TurtleInfo()
        message.turtle_name = "Turtle_5"
        message.letter = self.queue[4] 
        
        if(message.letter == 'A' or message.letter == 'a') :
            message = self.draw_A(message,4 ,self.step_index4)  # Modify the message to draw the letter "A"
        
        elif(message.letter == 'H' or message.letter == 'h') :
            message = self.draw_H(message,4,self.step_index4)  # Modify the message to draw the letter "H"

        elif(message.letter == 'M' or message.letter == 'm') :
            message = self.draw_M(message,4,self.step_index4)  # Modify the message to draw the letter "M"
        
        elif(message.letter == 'E' or message.letter == 'e') :
            message = self.draw_E(message,4,self.step_index4)  # Modify the message to draw the letter "E"

        elif(message.letter == 'Y' or message.letter == 'y') :
            message = self.draw_Y(message,4,self.step_index4)  # Modify the message to draw the letter "Y"
        elif(message.letter == 'D' or message.letter == 'd') :
            message = self.draw_D(message,4,self.step_index4)  # Modify the message to draw the letter "Y" 
        else :
            pass
        
            
        message.target_coords.z = 0.0

        self.publisher_.publish(message)

        self.get_logger().info(f'Published message: {message}')
        
    def publish_message1(self):
        # Create message to be published
        self.step_index1 += 1
        message = TurtleInfo()
        message.turtle_name = "Turtle_2"
        message.letter = self.queue[1] 
        
        if(message.letter == 'A' or message.letter == 'a') :
            message = self.draw_A(message,1 ,self.step_index1)  # Modify the message to draw the letter "A"
        
        elif(message.letter == 'H' or message.letter == 'h') :
            message = self.draw_H(message,1,self.step_index1)  # Modify the message to draw the letter "H"

        elif(message.letter == 'M' or message.letter == 'm') :
            message = self.draw_M(message,1,self.step_index1)  # Modify the message to draw the letter "M"
        
        elif(message.letter == 'E' or message.letter == 'e') :
            message = self.draw_E(message,1,self.step_index1)  # Modify the message to draw the letter "E"

        elif(message.letter == 'Y' or message.letter == 'y') :
            message = self.draw_Y(message,1,self.step_index1)  # Modify the message to draw the letter "Y"
        elif(message.letter == 'D' or message.letter == 'd') :
            
            message = self.draw_D(message,1,self.step_index1)  # Modify the message to draw the letter "Y" 
        else :
            pass
        
            
        message.target_coords.z = 0.0
        self.publisher_.publish(message)
        self.get_logger().info(f'Published message: {message}')
    

    def draw_A( self , message , letter_num , time_index ) :
        message.letter = "A"

        if letter_num == 0 :
            x_s = 1.0
            y_s = 3.0
        elif letter_num == 1 :
            x_s = 3.0
            y_s = 3.0
        elif letter_num == 2 :
            x_s = 3.0
            y_s = 3.0
        elif letter_num == 3 :
            x_s = 7.0
            y_s = 3.0     
        elif letter_num == 4 :
            x_s = 9.0
            y_s = 3.0
        else : 
            pass


        if time_index < 5 :
            message.target_coords.x = x_s + 0.5
            message.target_coords.y = y_s + 5.0
        elif time_index >= 5 and time_index < 10 :
            message.target_coords.x = x_s + 1.0
            message.target_coords.y = y_s + 2.5
        elif time_index >= 10 and time_index < 15 :
            message.target_coords.x = x_s 
            message.target_coords.y = y_s + 2.5
        elif time_index >= 15 and time_index < 20 :
            message.target_coords.x = x_s + 1.0
            message.target_coords.y = y_s + 2.5
        else :
            message.target_coords.x = x_s + 1.5
            message.target_coords.y = y_s 
            
        return message


    def draw_H(self , message , letter_num , time_index) :
        message.letter = "H"

        if letter_num == 0 :
            x_s = 1.0
            y_s = 3.0
        elif letter_num == 1 :
            x_s = 3.0
            y_s = 3.0
        elif letter_num == 2 :
            x_s = 5.0
            y_s = 3.0
        elif letter_num == 3 :
            x_s = 7.0
            y_s = 3.0     
        elif letter_num == 4 :
            x_s = 9.0
            y_s = 3.0
        else : 
            pass


        if time_index < 5 :
            message.target_coords.x = x_s 
            message.target_coords.y = y_s + 5.0
        elif time_index >= 5 and time_index < 10 :
            message.target_coords.x = x_s 
            message.target_coords.y = y_s + 2.5
        elif time_index >= 10 and time_index < 15 :
            message.target_coords.x = x_s + 1.5
            message.target_coords.y = y_s + 2.5
        elif time_index >= 15 and time_index < 20 :
            message.target_coords.x = x_s + 1.5
            message.target_coords.y = y_s + 5
        else :
            message.target_coords.x = x_s + 1.5
            message.target_coords.y = y_s 
            
        return message

    def draw_M(self , message , letter_num , time_index) :
        message.letter = "M"

        if letter_num == 0 :
            x_s = 1.0
            y_s = 3.0
        elif letter_num == 1 :
            x_s = 3.0
            y_s = 3.0
        elif letter_num == 2 :
            x_s = 5.0
            y_s = 3.0
        elif letter_num == 3 :
            x_s = 7.0
            y_s = 3.0     
        elif letter_num == 4 :
            x_s = 9.0
            y_s = 3.0
        else : 
            pass

        if time_index < 5 :
            message.target_coords.x = x_s + 0.25
            message.target_coords.y = y_s + 5.0
        elif time_index >= 5 and time_index < 10 :
            message.target_coords.x = x_s + 0.5
            message.target_coords.y = y_s + 2.5
        elif time_index >= 10 and time_index < 15 :
            message.target_coords.x = x_s + 1.0
            message.target_coords.y = y_s + 5.0
        elif time_index >= 15 and time_index < 20 :
            message.target_coords.x = x_s + 1.25
            message.target_coords.y = y_s 
        else :
            message.target_coords.x = x_s + 1.25
            message.target_coords.y = y_s 
            
        return message

    def draw_E(self , message , letter_num , time_index) :
        message.letter = "E"

        if letter_num == 0 :
            x_s = 1.0
            y_s = 3.0
        elif letter_num == 1 :
            x_s = 3.0
            y_s = 3.0
        elif letter_num == 2 :
            x_s = 5.0
            y_s = 3.0
        elif letter_num == 3 :
            x_s = 7.0
            y_s = 3.0     
        elif letter_num == 4 :
            x_s = 9.0
            y_s = 3.0
        else : 
            pass

        if time_index < 5 :
            message.target_coords.x = x_s 
            message.target_coords.y = y_s + 5.0
        elif time_index >= 5 and time_index < 10 :
            message.target_coords.x = x_s + 1.5
            message.target_coords.y = y_s + 5.0
        elif time_index >= 10 and time_index < 15 :
            message.target_coords.x = x_s 
            message.target_coords.y = y_s + 5.0
        elif time_index >= 15 and time_index < 20 :
            message.target_coords.x = x_s 
            message.target_coords.y = y_s + 2.5
        elif time_index >= 20 and time_index < 25 :
            message.target_coords.x = x_s + 1.5
            message.target_coords.y = y_s + 2.5
        elif time_index >= 25 and time_index < 30 :
            message.target_coords.x = x_s 
            message.target_coords.y = y_s + 2.5 
        elif time_index >= 30 and time_index < 35 :
            message.target_coords.x = x_s 
            message.target_coords.y = y_s 
        else :
            message.target_coords.x = x_s + 1.5
            message.target_coords.y = y_s 
            
        return message
    
    def draw_Y(self , message , letter_num , time_index) :
        message.letter = "Y"

        if letter_num == 0 :
            x_s = 1.0
            y_s = 3.0
        elif letter_num == 1 :
            x_s = 3.0
            y_s = 3.0
        elif letter_num == 2 :
            x_s = 5.0
            y_s = 3.0
        elif letter_num == 3 :
            x_s = 7.0
            y_s = 3.0     
        elif letter_num == 4 :
            x_s = 9.0
            y_s = 3.0
        else : 
            pass

        if time_index < 5 :
            message.target_coords.x = x_s + 1.5
            message.target_coords.y = y_s 
        elif time_index >= 5 and time_index < 10 :
            message.target_coords.x = x_s + 1.5
            message.target_coords.y = y_s + 5.0
        elif time_index >= 10 and time_index < 15 :
            message.target_coords.x = x_s + 1.5
            message.target_coords.y = y_s + 3.5
        elif time_index >= 15 and time_index < 20 :
            message.target_coords.x = x_s 
            message.target_coords.y = y_s + 3.5
        elif time_index >= 20 and time_index < 25 :
            message.target_coords.x = x_s 
            message.target_coords.y = y_s + 5.0
        else :
            message.target_coords.x = x_s 
            message.target_coords.y = y_s + 5.0
            
        return message
    
    def draw_D(self , message , letter_num , time_index) :
        message.letter = "D"

        if letter_num == 0 :
            x_s = 1.0
            y_s = 3.0
        elif letter_num == 1 :
            x_s = 3.0
            y_s = 3.0
        elif letter_num == 2 :
            x_s = 5.0
            y_s = 3.0
        elif letter_num == 3 :
            x_s = 7.0
            y_s = 3.0     
        elif letter_num == 4 :
            x_s = 9.0
            y_s = 3.0
        else : 
            pass

        if time_index < 5 :
            message.target_coords.x = x_s 
            message.target_coords.y = y_s + 5.0
        elif time_index >= 5 and time_index < 10 :
            message.target_coords.x = x_s + 1.5
            message.target_coords.y = y_s + 5.0
        elif time_index >= 10 and time_index < 15:
            message.target_coords.x = x_s + 1.5
            message.target_coords.y = y_s 
        else :
            message.target_coords.x = x_s 
            message.target_coords.y = y_s 
            
        return message
    def spawnturtle_request(self):
        client = self.create_client(Spawn ,"/spawn")
        self.get_logger().info("Waiting for turtle to spawn ......")
        client.wait_for_service()
        request = Spawn.Request()
        request.x = 1.0
        request.y = 3.0
        request.theta = 0.0
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
        request.x = 3.0
        request.y = 3.0
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
        request.x = 5.0
        request.y = 3.0
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
        request.x = 7.0
        request.y = 3.0
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
        request.x = 9.0
        request.y = 3.0
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
