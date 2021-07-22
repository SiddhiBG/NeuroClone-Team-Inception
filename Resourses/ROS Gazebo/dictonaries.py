from robot_control_class import RobotControl

rc = RobotControl  ()
a = rc.get_laser_full()
b = 10
dicto = {" Position 0 :" : a[0] , "Position 100 :" : a[100]  , "Position 200 : " : a[200] , 'Position 300 : ' : a[300] , 'Positon 400 : ' : a[400]  }

#print ( " Hi this is the terminal "  b )
name = input ( " Whats your name ?")

#print ( "Nice to meet you, " + str(name) )

age = input( 'Whats your age ?')
print ( ' Next year you will be %d years old ' %(age+1))
