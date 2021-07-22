# The code given in exapmle is a simpler way to express
# This was just to experiment lists as parameters

from robot_control_class import RobotControl

rc = RobotControl()
List = [0,0,0]

def laser_list(List):
    r1 = rc.get_laser_summit(List[0])
    r2 = rc.get_laser_summit(List[1])
    r3 = rc.get_laser_summit(List[2])
    return [r1,r2,r3]


for i in range(3) :
  List[i]=int (input( "Enter integer value between 0 to 719"))
  if List[i] >719 or <0 : 
      print ( " Learn to follow instructons")
      break

print ("Laser Values corresponding to" , List , " is " , laser_list(List)  )    