#!/usr/bin/env python3

import rospy
import os
import signal

msg = """ 

    Press key 1 for autonomous drive of the robot
    Press key 2 for manual driving of the robot
    Press key 3 for manual driving of the robot with collision avoidance
    Press key 4 for quitting the system
    """

# mode_switch()function will start the different
# modes depending on what the user decides to choose. 

boolprint = False
def mode_switch():
	
	global boolprint 
	print(msg)

	if boolprint == True:
		print("Press [0] for canceling the target.")
		boolprint = False
	command = input('Insert a command \n')
	
	# Setting all the modes idle.
	
	if command == "0":
		rospy.set_param('active', 0)
		print("All modes on IDLE")
		active_=rospy.get_param("/active")
		print(active_)

	# Starting the first mode, then asking the user which position he wants to reach.
	# Once the position is written we set the position on the parameters, these will be
	# read by the first mode.

	elif command == "1":

		rospy.set_param('active', 0)
		print("Autonomous driving mode active!")
		active_=rospy.get_param("/active")
		print("Where do you want the robot to go?")
		des_x_input = float(input("Insert the desired x position: "))
		des_y_input = float(input("Insert the desired y position: "))
		print("Heading Towards the position x = " + str(des_x_input) + " , y = " + str(des_y_input))
		print("The robot is moving towards your desired target!")		
		rospy.set_param('des_pos_x', des_x_input)
		rospy.set_param('des_pos_y', des_y_input)
		rospy.set_param('active', 1)
		boolprint=True

	# Starting the second mode.

	elif command == "2":
		rospy.set_param('active', 2)
		print("manual driving mode is active.")
		active_ = rospy.get_param("/active")
	
	# Starting the third mode.

	elif command == "3":
		rospy.set_param('active', 3)
		print("assistive driving mode 3 is active.")
		active_=rospy.get_param("/active")

	# If we want to quit the program, we press 4.

	elif command == "4":
		print("Exiting...")
		os.kill(os.getpid(), signal.SIGKILL)
	
	# If the user presses anything else, we want to quit the program.

	else:
		print("Wrong key!")

# What we want now, is to call the functions created and printing the starting message.


def main():
	print("USER INTERFACE NODE!")
	while not rospy.is_shutdown():
		mode_switch()

if __name__ == '__main__':
    main()
