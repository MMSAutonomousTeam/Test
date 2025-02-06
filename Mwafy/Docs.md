# Autonomous-Training-Tasks

Welcome to the repository for the **Autonomous Training Tasks.**

### SELF INTRODUCTION

**Name :** Ahmed Mwafy

**Department** : Mechatronics lv200

**Autonomous member in 2024**

### Task 1: Drawing Ahmed "my name" with Turtlesim in ROS2

In this project, I’ve used ROS2 to create a fun and interactive demonstration of my name, “Ahmed”, drawn with the help of the **Turtlesim** package. The goal was to implement a system in which each letter of my name is drawn by controlling a turtle. To achieve this, I created a **package** containing  **five separate nodes** , with each node responsible for drawing a single letter of my name.

The structure of the project is as follows:

* **Each node** is responsible for controlling a turtle to draw one letter of my name.
* **Turtlesim** provides a simple 2D simulation environment where we can control the movement of the turtle to create shapes, patterns, and in this case, letters.
* By combining the movements and commands across multiple nodes, the complete name "Ahmed" is rendered step-by-step on the simulation screen.

This project demonstrates the use of ROS2 concepts such as nodes, topics, and servicesfor inter-node communication, and highlights the simplicity and power of the Turtlesim package in a fun and educational manner.

```python
#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.srv import SetPen
from turtlesim.srv import Spawn
from turtlesim.srv import Kill
from functools import partial
import time
```

* **`rclpy`** : The ROS 2 Python client library used to interact with ROS nodes and services.
* **`geometry_msgs.msg.Twist`** : Defines the `Twist` message type used for controlling linear and angular velocities of the turtle.
* **`turtlesim.srv.SetPen`, `Spawn`, `Kill`** : Service types for controlling the turtle in `turtlesim` (setting pen, spawning a turtle, killing a turtle).
* **`functools.partial`** : A utility for pre-setting parameters in a function, used for handling asynchronous callbacks.
* **`time`** : Used to introduce delays (`time.sleep()`).

```python
  class NameDrawingNode(Node):
    def init(self):
        super().init("drawing_A")
        self.time_needed = 0.0
        self.cmd_vel_publisherA_ = self.create_publisher(Twist , "/LetterATurtle/cmd_vel" , 10)
        global printed
        if printed :
            self.spawnturtle_request()
            printed = False
```

* Initializes the node with the name `"drawing_A"`.
* Creates a publisher for controlling the turtle's velocity (`cmd_vel`).
* Ensures the turtle spawns only once by calling `spawnturtle_request()`.

```python
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
```

Processes the result of the spawn request. If successful, calls `killturtle_request()` to kill the default turtle (`turtle1`).

```python

def callback_spawn(self, future):
    try:
        res = future.result()
        self.killturtle_request()
        self.get_logger().info("Turtle Spawned successfully !!!!!")
    except Exception as e:
        self.get_logger().error(f"Service failed: {e}")

```

* The `callback_spawn` method processes the result of the spawn request. If successful, it calls `killturtle_request()` to kill the default turtle (`turtle1`).

```python
    client = self.create_client(Kill ,"/kill")
    self.get_logger().info("Waiting for turtle to spawn ......")
    client.wait_for_service()
    request = Kill.Request()
    request.name = "turtle1"
    future1 = client.call_async(request)
    future1.add_done_callback(partial(self.call_back_kill))
```

* The `killturtle_request` method sends a request to kill the default turtle (`turtle1`).

```python
    try:
        res = future1.result()
        self.call_set_pen_service()
        self.get_logger().info("Turtle Spawned successfully !!!!!")
    except Exception as e:
        self.get_logger().error(f"Service failed: {e}")  
```

* The `call_back_kill` method is executed after killing the default turtle. It proceeds to call `call_set_pen_service()` to configure the pen color and width.

```python
def call_set_pen_service(self):
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
```

The `call_set_pen_service` method sends a request to set the pen color to red (`r=255, g=0, b=0`) and set the pen width to `7`.

```python
callback_set_pen(self, future__):
    try:
        res = future__.result()
        self.cmd_vel_publisherA_func()
    except Exception as e:
        self.get_logger().error("Service Failed : %r % (e,)")   
```

* The callback_set_pen method is executed after setting the pen. It starts drawing the letter 'A' by calling `cmd_vel_publisherA_func()`.

```python
def main(args=None):
    rclpy.init(args=args)
    node = NameDrawingNode()
    rclpy.spin(node)
    rclpy.shutdown()
```

* The main function initializes ROS 2 communication, creates the NameDrawingNode, and enters the ROS 2 event loop (rclpy.spin(node)).
* It shuts down ROS 2 once the node has finished processing.

---

## *Summary*

This code defines a ROS 2 node that interacts with the `turtlesim` simulator to draw the letter 'A'. It achieves this by spawning a turtle, controlling its movements using velocity commands, setting the pen color to red, and using a sequence of movements to draw the letter. & each other node is exactly the same but with differnet movements to change the letter drawed .
