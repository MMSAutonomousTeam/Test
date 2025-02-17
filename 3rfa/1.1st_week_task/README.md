# 🐢 ROS 2 Turtlesim Name Drawer

## 🚀 Overview

This ROS 2 project uses `turtlesim` to draw the name **"ARAFA"** using multiple turtles. Each letter is drawn by a different turtle with a unique color. The program handles spawning, killing, pen color setting, and movement of turtles to create the desired letters.

## 📌 Features

* 🐢 Spawns 5 turtles at specific positions.
* 🎨 Sets different pen colors for each turtle.
* ❌ Removes the default `turtle1` to avoid conflicts.
* ✏️ Draws the letters **A, R, A, F, A** sequentially by Using velocity commands to move turtles and draw letters.
* 🔄 Uses ROS 2 services and publishers for movement and pen control.

## 🛠 Dependencies

Make sure you have the following installed:

* **ROS 2 (Humble or newer)** 🦾
* **turtlesim** package 🐢

To install turtlesim:

```bash
sudo apt install ros-humble-turtlesim
```

## ⚙️ Installation

Clone this repository into your ROS 2 workspace then, build source it:

```bash
cd ~/ros2_ws/src
git clone <this-repo-link>
cd ~/ros2_ws
colcon build
source install/setup.bash
```

## ▶️ Running the Program

First, launch `turtlesim`:

```bash
ros2 run turtlesim turtlesim_node
```

Then, run the script to draw "ARAFA":

```bash
ros2 run turtle_package my_name
```

## 🛠️ How It Works

* 🐢 The program spawns five turtles at different positions.
* 🎨 It sets pen colors for each turtle.
* ✍️ Each turtle moves according to pre-defined paths to form letters.
* 📡 The movement is done using velocity commands (`<span>cmd_vel</span>`).
* 🤖 The script runs automatically without manual input.

## 📂 Code Structure

* 🔹 `<span><strong>spawn_turt(x, y, theta, name)</strong></span>` → Spawns a turtle at given coordinates.
* 🔹 `<span><strong>kill_turt(name)</strong></span>` → Kills an existing turtle.
* 🔹 `<span><strong>set_pen(r, g, b, name)</strong></span>` → Changes pen color for a turtle.
* 🔹 `<span><strong>move_turtle(name, x, y, theta)</strong></span>` → Moves a turtle in a specific direction.
* 🔹 `<span><strong>draw_A(name)</strong></span>`, `<span><strong>draw_R(name)</strong></span>`, `<span><strong>draw_F(name)</strong></span>` → Functions to draw letters.

## 📜 Code Explanation

### 🏗 Initialization

```python
class my_name(Node):
    def __init__(self):
        super().__init__('my_name')
```

* Creates a ROS 2 node named `my_name`.

### 🐢 Turtle Spawning & Setup

```python
self.spawn_turt(x, y, theta, turtle_name)
self.set_pen(r, g, b, turtle_name)
self.creat_pup(turtle_name)
```

* Spawns turtles at defined positions.
* Assigns each a unique pen color.
* Creates velocity publishers to control movement.

### ❌ Killing Default Turtle

```python
self.kill_turt('turtle1')
```

* Removes the default `turtle1` so it doesn’t interfere.

### ✏️ Drawing Letters

##### Each function moves the turtle to draw a specific letter(but to do that you should know the turtlesim dimensions):

This way TurtleSim field will be divided into 9 areas, as shown below:
![Alt text](https://github.com/MMSAutonomousTeam/Test/blob/0f19006d869143628a329f2b903f423b4eb489b4/3rfa/1.1st_week_task/images/1.png)

#### Example: Drawing 'A'

```python
self.move_turtle(turtle_name,  0.75 ,  4.0, 0.0) # Move diagonally up
self.move_turtle(turtle_name,  0.375, -2.0, 0.0) # Move diagonally down
self.move_turtle(turtle_name, -0.75 ,  0.0, 0.0) # Draw the crossbar
self.move_turtle(turtle_name,  0.75 ,  0.0, 0.0) # Go back
self.move_turtle(turtle_name,  0.375, -2.0, 0.0) # Move diagonally down
```

* Moves the turtle to create the strokes forming the letter 'A'.

### 🔄 Moving Turtles

```python
msg = Twist()
msg.linear.x = linearx
msg.linear.y = lineary
msg.angular.z = angular
self.pub.publish(msg)
```

* Publishes velocity commands to move the turtle.
* Uses `time.sleep(1.5)` for smoother execution.

## 📌 Output

After running the script, the turtles will draw the name **"ARAFA"** in different colors inside the `<span>turtlesim</span>` window. Each letter will be drawn by a different turtle, creating a colorful and dynamic effect.
![Alt text](https://github.com/MMSAutonomousTeam/Test/blob/0f19006d869143628a329f2b903f423b4eb489b4/3rfa/1.1st_week_task/images/2.png)

## 📚 References

* [ROS 2 Documentation]()
* [Turtlesim Tutorials]()
* [Velocity Commands in ROS 2]()

## 👨‍💻 Author

Developed by **Abdelrahman Arafa** 🚀. Contributions are welcome!


