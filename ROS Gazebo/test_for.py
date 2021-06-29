from robot_control_class import RobotControl

rc = RobotControl()

a = rc.get_laser_full()
counter=0
for x in a : 
   x=min(x,a[counter])
   counter += 1

print(x)