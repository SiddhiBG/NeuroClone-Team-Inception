from robot_control_class import RobotControl

rc=RobotControl(robot_name="summit")

print(rc.move_straight_time("forward",0.5,2))
print(rc.turn("counter-clockwise",0.6,3))
print(rc.move_straight_time("forward",0.5,4.15))
print(rc.turn("counter-clockwise", 0.6,3))
print(rc.move_straight_time("forward",2,1.5))



