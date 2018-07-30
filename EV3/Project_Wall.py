from ev3dev.ev3 import *
from time import sleep


motor1 = LargeMotor('outA')
motor2 = LargeMotor('outB')
motor3 = MediumMotor('outD')
ir = InfraredSensor()
ir.mode = 'IR-PROX'
tc = TouchSensor()
tc.mode = 'TOUCH'

while True:
    print("Inside While")
    proximity = ir.value()
    #print("Proximity: %s" % proximity)
    if proximity <= 16:
        #Sound.speak('Proximity is less than 16')
        motor1.run_to_rel_pos(position_sp=360, speed_sp=400, stop_action='brake')
        motor2.run_to_rel_pos(position_sp=360, speed_sp=400, stop_action='brake')
        motor3.run_to_rel_pos(position_sp=50, speed_sp=400, stop_action='brake')
        motor1.run_to_rel_pos(position_sp=2200, speed_sp=300, stop_action='brake')
        motor2.run_to_rel_pos(position_sp=2200, speed_sp=300, stop_action='brake')
        motor3.run_to_rel_pos(position_sp=-80, speed_sp=400, stop_action='brake')
    elif tc.value() == 1:
        #Sound.speak('Touch Sensor activated')
        motor1.stop()
        motor2.stop()
        motor3.stop()
        motor1.run_to_rel_pos(position_sp=-360, speed_sp=400, stop_action='brake')
        motor2.run_to_rel_pos(position_sp=-360, speed_sp=400, stop_action='brake')

    elif tc.value() == 1 and proximity <= 16:
        #Sound.speak("Unable to move")
        break
    
    elif proximity > 16:
        #Sound.speak('Proximity is greater than 16')
        motor1.run_to_rel_pos(position_sp=-360, speed_sp=400, stop_action='brake')
        motor2.run_to_rel_pos(position_sp=-360, speed_sp=400, stop_action='brake')
        
        
