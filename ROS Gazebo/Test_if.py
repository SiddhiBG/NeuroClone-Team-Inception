from  robot_control_class import RobotControl 

rc =RobotControl()

a = rc.get_laser(360)

while a>1 :
    rc.move_straight()
    a=rc.get_laser(360)
   
    print ( "Distance : %a " %a)


rc.stop_robot()
print ( " Stopped at " , a )



