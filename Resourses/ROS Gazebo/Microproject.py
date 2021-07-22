from robot_control_class  import RobotControl 

rc = RobotControl(robot_name= " Turtlebot")

a= rc.get_laser(360) 
b= rc.get_laser(0)
c=rc.get_laser(719)

for i in range(3) :
 while a > 5 : 
    rc.move_straight()
    a= rc.get_laser(360)

 rc.stop_robot()
 b= rc.get_laser(0)
 c= rc.get_laser(719)

 if b > c : 
    rc.rotate(90)
 else : 
    rc.rotate(270) 


while a > 5 : 
    rc.move_straight()
    a= rc.get_laser(360)

b= rc.get_laser(0)
c= rc.get_laser(719)

if b < 10 or c<10 :
  rc.stop_robot()

print ("Thanks for helping me out!")

 


