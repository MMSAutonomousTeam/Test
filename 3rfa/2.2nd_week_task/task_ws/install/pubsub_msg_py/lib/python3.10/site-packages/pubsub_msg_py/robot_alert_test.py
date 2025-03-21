#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from roboy_info_system_msg.msg import RobotAlert

class AlertPublisher(Node):

    def __init__(self):
        super().__init__('alert_publisher')
        self.publisher_ = self.create_publisher(RobotAlert, 'alert_topic', 10)
        timer_period = 1.0
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = RobotAlert()
        
        alert_levels = [1, 2, 3]
        alert_messages = ["Battery Low!", "Battery medium!", "Battery high"]

        msg.alert_level = alert_levels[self.i % 3]
        msg.alert_message = alert_messages[self.i % 3]

        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: Level={msg.alert_level}, Message="{msg.alert_message}"')

        self.i += 1


def main(args=None):
    rclpy.init(args=args)
    node = AlertPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
