# RT1Assignment3

## INTRODUTION

Research Track 1 Assignment 3
In this assignment we asked to program and develop the structure of the robot on ROS enviroment in such a way that it must follow the following behaviours.
* Autonomously reach a x,y coordinate inserted by the user
* Let the user drive the robot with the keyboard.
* Let the user drive the robot assisting them to avoid collisions.


project is to created on a simulation of a robot on ROS with Gazebo and Rviz, in order to make the robot exploring the map. The simulation is like this,
This package provides a 3D environment with a mobile robot, and a number of robot control is implemented to navigate this environment. The major packages and nodes that are showcased in this package are the MoveBase path planning package, the slam gmapping package for mapping the environment, A command-line user interface is provided for the user to select one of the aboved mentioned actions. 

# picture 

## Nodes 

Different nodes are created in this package that works together to compelet the goal given by user.

## UI Node:

UI node is capable of switching between the nodes by setting the ros parameter. Ros parameter updates the value in “active” as chosen by the user to run the specific node.

## PICTURE


## Mode1:
In this mode Robot has to reach the goal by getting the co-ordinates. The node uses move_base node to follow the navigation to reach its goal. This mode is based on MoveBaseAction. 
Then, we have the function ActionClient(), __the function starts the communication with wait_for_server(). The action client and server communicate over a set of topics, described in the actionlib protocol. 
The main() function takes the aim of the modality. First of all it loops, then we update the variables (containing the status of the modality and the position informations) and the code understands the behavior of the robot status thanks to the action.
