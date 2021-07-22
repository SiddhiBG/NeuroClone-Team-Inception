from robot_control_class import RobotControl

rc = RobotControl()
laser1 = rc.get_laser (719)
 print ( "Laser value in laser 1 :", laser1)

 laser2= rc.get_laser(360)
 print( 'Laser value in laser 2 :' ,laser2)

 laser2= rc.get_laser(360) 
 print ( ' Modified value of laser 2', laser2)
