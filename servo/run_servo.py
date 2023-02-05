#!/usr/bin/env python
from servo_controller import ServoController
from scservo_sdk import SCS_TOHOST

SCS_MINIMUM_POSITION_VALUE = 300 
SCS_MAXIMUM_POSITION_VALUE = 800 # (note that the SCServo would not move when the position value is out of movable range. Check e-manual about the range of the SCServo you use.)
scs_goal_position = [SCS_MINIMUM_POSITION_VALUE, SCS_MAXIMUM_POSITION_VALUE]
scs_goal_position_index = 0

servo = ServoController(0, "/dev/ttyUSB0")
servo.set_acc()
servo.set_speed()

while 1:
    servo.set_goal_position(scs_goal_position[scs_goal_position_index])

    # loop while servo gets to the goal position
    while 1:
        (scs_present_position, scs_present_speed) = servo.get_current_position_and_speed()

        print("[ID:%03d] GoalPos:%03d PresentPos:%03d PresentSpeed:%03d" 
              % (servo.get_id(), scs_goal_position[scs_goal_position_index], scs_present_position, SCS_TOHOST(scs_present_speed, 15)))

        SCS_MOVING_STATUS_THRESHOLD = 20

        if not abs(scs_goal_position[scs_goal_position_index] - scs_present_position) > SCS_MOVING_STATUS_THRESHOLD:
            break

    # Change goal position
    scs_goal_position_index = scs_goal_position_index ^ 1

