# writing my name wit he the turtle _sym

in this document i will discus alot of ROS basics which i used while working on this project

* **introduction**
* **positioning & controling**
* **code structure and syntax for each letter**
* **error correction and optimization**
* **recap**

### introduction

in this document i will  discus the steps which followed to make this project , i hope you like it <3

### **postioning :**

first, i devided the the turtle sym window into some cells and spawned the turtles in specific positions

which which each turtle can have 2*2 cell to navigate in

```
ros2 service call /spawn turtlesim/srv/Spawn "{x: 1.5, y: 8.5, theta: 0, name: 'turtle1'}"          # turtle1  →
ros2 service call /spawn turtlesim/srv/Spawn "{x: 4.5, y: 8.5, theta: 3.14, name: 'turtle2'}"       # turtle2  ←
ros2 service call /spawn turtlesim/srv/Spawn "{x: 5.0, y: 4.5, theta: 3.14, name: 'turtle3'}"       # turtle3  ←
ros2 service call /spawn turtlesim/srv/Spawn "{x: 6.5, y: 5.5, theta: -1.57, name: 'turtle4'}"      # turtle4  ↓
ros2 service call /spawn turtlesim/srv/Spawn "{x: 9.0, y: 2.0 , theta: 3.14, name: 'turtle5'}"      # turtle5  ←
```

### **controlling :**

to make each turtle draw a letter in a 2*2 area i used some linear & rotational dynamics concepts like :

**v = dx / dt**      which used in linear motion

This is the fundamental definition of  **linear velocity** , which represents the rate of change of position (x) with respect to time (t)

---

* **v** → **Linear velocity** (m/s): The speed and direction of an object moving in a straight line.
* x → **Position** (m): The location of the object along a straight path.
* **dx**→  **Change in position** : A small movement over a tiny time interval.
* **dt** →  **Change in time** : The tiny time step during which the move

**v = rω**    in rotaional motion

This equation describes the relationship between **linear velocity** (**v**) and **angular velocity** (ω\omega**ω**) in a rotating system. It tells us how fast a point on a rotating object moves in a straight-line direction at any instant.

---

* v → **Linear velocity** (m/s): How fast a point on the rotating object moves along a straight line (tangential velocity).
* **r**→ **Radius** (m): The distance from the axis of rotation to the point in motion.
* **ω\omega** → **Angular velocity** (rad/s): The rate at which the object rotates (how fast the angle changes).

### coding structure for each syntax

#### 1- o (turtle_1):

consists of a circle of radius = 1.0 so, we nead a linear x vel and an angular z vel which at we get a radius = 1.0
these conditions will be true at **v = ω** and i assigned these values as : l**in.x = 3.0  & ang.z = 3.0**

```

self.publisher1 = self.create_publisher(Twist , "/turtle1/cmd_vel" , 10)   # created a pub for the turtle 1 
        self.timer1 = self.create_timer (1.0 , self.o_fun)                 # created a timer for the o_fun


def o_fun(self):
        snd = Twist()                                                      # making an instance of Twist to send it with the pub
        snd.linear.x = 3.0                                                 # initializing the lin.x vel 
        snd.angular.z = 3.0                                                # initializing the ang.z vel 
        self.publisher1.publish(snd)                                       # publishing the message to the topic

```

#### 2- s(turtle_2):

consists of a half circle of radius = 0.5 conter clock wise followed by a half circle of radius = 0.5 conter clock wise so, we nead a linear x vel and an angular z vel which at we get a radius = 0.5 , these conditions will be true at **v = ω** and i assigned these values as :

 l**in.x = 3.0  & ang.z = 3.0  for the 1st H.C ---** **lin.x = 3.0  & ang.z = - 3.0  for the 2nd H.C**

```
self.s = 0
self.publisher2= self.create_publisher(Twist , "/turtle2/cmd_vel" , 10)
self.su2 = self.create_subscription(Pose,"/turtle2/pose",self.s_fun,10)

def s_fun (self,pose:Pose):
        output = Twist()                               # making an instance of Twist to send it with the pub  
        if pose.y <= 6.7 :                             # a condition at which the turtle stops moving when the letter is already written
            output.linear.x = 0.0  
            output.angular.z = 0.0
            self.s += 1                          # a counter used to prevent the other conditions of the turtle from working more than once 

        elif self.s <= 0 and 6.5 < pose.y <= 7.57 :    # a condition used to prevent the turtle from contiuing moving beyond the lower H.C 
            output.linear.x = 3.0
            output.angular.z = -6.0

        elif self.s <= 0 and pose.y > 7.5  :           # a condition used to prevent the turtle from continuing moving beyond the upper H.C 
            output.linear.x = 3.0
            output.angular.z = 6.0

        self.publisher2.publish(output)
```

#### 3- a(turtle 3,5):

consists of a qurter circle of radius = 0.5 clock wise followed by a circle of radius = 1.0 conter clock wise so, we nead a linear x vel and an angular z vel which at we get a radius = 0.5 , these conditions will be true at **2*v = ω** , v = ω  relatively and i assigned these values as :

l**in.x = 3.0  & ang.z = - 6.0  for the 1st Q.C ---** **lin.x = 6.0  & ang.z = 6.0  for the 2nd cir**

```
self.a = False
        self.publisher3= self.create_publisher(Twist , "/turtle3/cmd_vel" , 10)
        self.publisher5= self.create_publisher(Twist , "/turtle5/cmd_vel" , 10)      # making 2 pubs for every turtle which draws letter a 
        self.pub35 = self.create_subscription(Pose,"/turtle3/pose",self.a_fun,10)    # making 1 sub for one of the turtles to subscride for

def a_fun(self,pose:Pose) :
        output2 = Twist()
        if pose.theta <= 1.57 :                          # a condition to prevent the turtle from continuing drawnig the q.c   
            self.a = True                                # a boolean whoch used for preventing

        if self.a == False :                             # a condtion to draw a q.c 
            output2.linear.x = 3.0
            output2.angular.z = -6.0
  
        else :                                           # a condition to draw a circle
            output2.linear.x = 6.0
            output2.angular.z = 6.0

        self.publisher3.publish(output2)                 # publishing the same output to both turtles at the same time
        self.publisher5.publish(output2)
  
```

#### 4- m(turtle 4):

consists of an vertical line followed by 2 half circles of radius = 0.5 clock wise so, we nead a linear x vel for the line , linear x vel and an angular z vel for the 2 circles which at we get a radius = 0.5 , these conditions will be true at **ω = 0** , **2*v = ω**  relatively and i assigned these values as :

l**in.x = 3.0  & ang.z = 0.0  for the line ---** **lin.x = 3.0  & ang.z = - 6.0  for the 2 circles**

```
self.m = True
self.publisher4= self.create_publisher(Twist , "/turtle4/cmd_vel" , 10)
self.su4 = self.create_subscription(Pose,"/turtle4/pose",self.m_fun,10)

def m_fun(self,pose:Pose):
        output3 = Twist()
        if pose.x >= 8.49 :                                            # a condition to prevent the turtle from drawing more than 2 circles
                self.m = False
        if pose.y > 4.5 and -1.58 <= pose.theta <= -1.56 :             # a condition to draw the vertical line
            output3.linear.x = 3.0
            output3.angular.z = 0.0
  
        elif pose.y <= 4.5 and pose.theta <= 1.57:       # a condition to make the turtle change it's direction to start drawing any circle
            output3.linear.x = 0.0
            output3.angular.z = 1.0

        elif self.m == True :                            # a condition to make the turtle draw a a half circle
            output3.linear.x = 3.0
            output3.angular.z = -6.0
  
        self.publisher4.publish(output3)
```

### error correction and optimization

i used some tricks to optimize the errors which i found  like

**- reversing the sequence of the conditions of any letter to handle the change between moves easily without infinity loops**

**-** **and increasing the values of the y pos in the initial condition of a move than the final condition of the previous move like :**

```
 	if pose.y <= 6.7 :                                    #last cond     # y <= 6.7 not 6.5 to avoid the inaccuracy of the position
   
   
        elif self.s <= 0 and 6.5 < pose.y <= 7.57 :           # mid cond     # y<= 7.57 not 7.5 to avoid the inaccuracy of the position
  

        elif self.s <= 0 and pose.y > 7.5  :                 # first cond
   

```

**- putting the conditions of any move of a suitable parameters which has less errors like :**

in the m_fun at the beginning i put the condition to stop the turtle when a counter increases two times and a put the increment line when the turtle is at y <= 4.5

put due to the frequent call backing of the m_fun it increased fastly and the turtle draws more than 2 circles or doesnt draw any circle , so i used the conition that x shouldn't exceed 8.5 which isn't effected by the call back rate

```
if pose.x >= 8.49 :         # can't be effected with the frequent call backing
```

### recap

to make this project i used a sequence of steps like

**positioning & controling :** *i located every turtle in a specific position which is useful for organizing the letters*

**code structure and syntax for each letter :** *i devided every letter to a number of turtle moves each move have a condition should be true*

**error correction and optimization :** *i organized the conditions of the moves in a specific sequence and made the values have tolerances to avoid infinty loops*
