# RT1Assignment3

## INTRODUTION
----------------------------
In this assignment we were asked to program and develop the structure of the robot on ROS enviroment in such a way that it must follow the following behaviours.
* Autonomously reach a x,y coordinate inserted by the user
* Let the user drive the robot with the keyboard.
* Let the user drive the robot assisting them to avoid collisions.

The project is to create on a simulation of a robot on ROS with Gazebo and Rviz, in order to make the robot exploring the map. These packages provides a 3D environment with a mobile robot, and a number of robot control is implemented to navigate this environment. The major packages and nodes that are showcased in this package are the MoveBase path planning package, the slam gmapping package for mapping the environment, the Xterm based command-line user interface is provided for the user to select one of the aboved mentioned actions. 

# Robot Simulation
To run the simulation, open a terminal and type:
```
$ roslaunch final_assignment simulation.launch
```
## Simulation Launch File

The above simulation.launch file holds the launch parameters of both simulation_gmapping and move_base packages and robot simulation. 

### simulation_gmapping
The simulation_gmapping package allows:
```
Add the description of the robot to the ROS parameter server
Launch the simulation in Gazebo
Launch the Rviz node, along with some additional nodes
Generate the robot in the simulation
```
### Move_base 
The move_base package allows:
```
Launch the move_base node
Set the rosparam described in the .yaml file
```
### final_assignment 
The final_assignment packages holds the overall working of each mode by making different nodes that works together to compelet the goal given by user.

#### UserInterface
```
The UserInterface node is capable of switching between the nodes by setting the ros parameter. 
Ros parameter updates the value in “active” as chosen by the user to run the specific node.
```
![UI](https://user-images.githubusercontent.com/95746070/182434366-3184f0af-5f98-45b1-a485-8b181631d904.png)


#### mode 1
```

```
![mode1](https://user-images.githubusercontent.com/95746070/182434470-4ad974b2-c458-49c6-8e85-ddec7cd86d5b.png)


#### mode 2
```

```
![mode 2](https://user-images.githubusercontent.com/95746070/182434498-12d37440-1aa2-4389-80e3-6b003da768d3.png)


#### mode 3
```

```
![mode3](https://user-images.githubusercontent.com/95746070/182434522-189a0ba4-e073-4c44-a42a-dc7e4660e0e9.png)


# RVIZ & Gazebo Environment 

![gazebo](https://user-images.githubusercontent.com/95746070/182430919-4ea5bcf9-4bd6-48c2-b341-3d63dd5d704c.png)
![rviz](https://user-images.githubusercontent.com/95746070/182430941-553625f0-ba23-4581-bd9e-5bc08d4e5763.png)


## Mode1:
In this mode Robot has to reach the goal by getting the co-ordinates. The node uses move_base node to follow the navigation to reach its goal. This mode is based on MoveBaseAction. 
Then, we have the function ActionClient(), __the function starts the communication with wait_for_server(). The action client and server communicate over a set of topics, described in the actionlib protocol. 
The main() function takes the aim of the modality. First of all it loops, then we update the variables (containing the status of the modality and the position informations) and the code understands the behavior of the robot status thanks to the action.
