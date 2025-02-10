# ZAHABY Name Writing Using ROS 2 Turtles

## Overview

This project demonstrates how to programmatically control turtles in ROS 2's `turtlesim` simulator to write the name **"ZAHABY"** using multiple turtles. Each turtle is responsible for drawing a specific letter. The project utilizes services and publishers in ROS 2 to spawn, control, and set the appearance of turtles.

## Table of Contents

- [System Requirements](#system-requirements)
- [Installation](#installation)
- [Code Explanation](#code-explanation)
  - [Node Initialization](#node-initialization)
  - [Services and Publishers](#services-and-publishers)
  - [Functions](#functions)
- [Execution Steps](#execution-steps)
- [Output](#output)
- [References](#references)

## System Requirements

- **ROS 2 Humble** (or compatible version)
- Python 3.8+
- `turtlesim` package installed:
  ```bash
  sudo apt install ros-humble-turtlesim
  ```

## Installation

1. Clone or download the project repository.
2. Save the provided Python script as `turt_cont.py` in your ROS 2 workspace (e.g., `~/ros2_ws/src`).
3. Build the workspace:
   ```bash
   colcon build
   ```
4. Source the workspace:
   ```bash
   source install/setup.bash
   ```

## Code Explanation

### Node Initialization

The `turtle_node` class inherits from `Node` and is initialized with services and publishers for controlling turtles in `turtlesim`.

### Services and Publishers

- **Spawn Service**: Used to create new turtles at specified positions.
- **Kill Service**: Removes the default `turtle1` and other turtles as needed.
- **SetPen Service**: Configures the pen color, width, and state (on/off) for each turtle.
- **Velocity Publishers**: Send velocity commands to turtles to draw shapes.

### Functions

#### 1. **`spawn_turt`**

   Spawns a turtle at a specified position.

```python
   def spawn_turt(self, x, y, theta, name):
```

#### 2. **`kill_turt`**

   Kills an existing turtle by name.

```python
   def kill_turt(self, name):
```

#### 3. **`set_pen`**

   Configures the pen settings for a turtle.

```python
   def set_pen(self, r, g, b, width, off, name):
```

#### 4. **`move_for_duration`**

   Moves a turtle for a specific duration using linear and angular velocities.

```python
   def move_for_duration(self, publisher, msg, duration):
```

#### 5. **Drawing Functions**

- `draw_z`: Draws the letter "Z".
- `draw_a`: Draws the letter "A".
- `draw_h`: Draws the letter "H".
- `draw_b`: Draws the letter "B".
- `draw_y`: Draws the letter "Y".

#### 6. **`draw_name`**

   Calls the individual letter-drawing functions to draw "ZAHABY".

### Execution Steps

1. Initialize the ROS 2 node.
2. Remove the default turtle (`turtle1`).
3. Spawn six turtles with specific initial positions and orientations.
4. Set the pen properties for each turtle.
5. Command each turtle to draw its respective letter.
6. Combine the letters to form the name "ZAHABY".

## Execution Steps

1. Run the ROS 2 `turtlesim_node`:

   ```bash
   ros2 run turtlesim turtlesim_node
   ```
2. Execute the script:

   ```bash
   ros2 run zahaby_pkg turt_cont.py
   ```

## Output

The turtles will collectively draw the name **"ZAHABY"** in the `turtlesim` simulator.

## References

- ROS 2 Documentation: [https://docs.ros.org](https://docs.ros.org)
- `turtlesim` Package: [Turtlesim Overview](https://docs.ros.org/en/humble/Tutorials/Turtlesim.html)
