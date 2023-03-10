"""my_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, Motor, DistanceSensor, GPS
import random

class SmashBotMotor(Motor):

    def __init__(self, name=None):
        super().__init__(name)
        self.setPosition(float('inf'))
        self.setVelocity(0)
        

class SmashBotMotors():
    def __init__(self, speed=None):
        self.__front_right_wheel_m = SmashBotMotor("front right wheel motor")
        self.__front_left_wheel_m = SmashBotMotor("front left wheel motor")
        self.__rear_right_wheel_m = SmashBotMotor("rear right wheel motor")
        self.__rear_left_wheel_m = SmashBotMotor("rear left wheel motor")
    
    def go_forward(self, speed=20):
        self.__front_right_wheel_m.setVelocity(speed)
        self.__front_left_wheel_m.setVelocity(speed)
        self.__rear_left_wheel_m.setVelocity(speed)
        self.__rear_right_wheel_m.setVelocity(speed)

    def go_backwards(self, speed=20):

        self.__front_right_wheel_m.setVelocity(-1*speed)
        self.__front_left_wheel_m.setVelocity(-1*speed)
        self.__rear_left_wheel_m.setVelocity(-1*speed)
        self.__rear_right_wheel_m.setVelocity(-1*speed)
        print("Go Back method")

    def go_left(self, speed=20):
        self.__front_right_wheel_m.setVelocity(speed)
        self.__front_left_wheel_m.setVelocity(0)
        self.__rear_left_wheel_m.setVelocity(0)
        self.__rear_right_wheel_m.setVelocity(speed)
        print("Go Left method")

    def go_right(self, speed=20):
            self.__front_right_wheel_m.setVelocity(0)
            self.__front_left_wheel_m.setVelocity(speed)
            self.__rear_left_wheel_m.setVelocity(speed)
            self.__rear_right_wheel_m.setVelocity(0)

class SmashBot(Robot):

    def __init__(self, speed=None):
        super().__init__()
        self.__motors = SmashBotMotors()
        self.__sensors = SmashBotSensors()
        self.gps = SmashBotGPS()

    def run(self, dir='forward', speed=20):
        if dir=='forward':
            self.__motors.go_forward()
        elif dir=='backwards':
            self.__motors.go_backwards()
        elif dir=='left':
            self.__motors.go_left()
        elif dir=='right':
            self.__motors.go_right()

        self.__sensors.get_sensor()
        self.__sensors.print_sensor_value()
                


class SmashBotSensor(DistanceSensor):
    def __init__(self):
        super().__init__()
        self.enable()
        #self.getValue()

class SmashBotSensors(SmashBotSensor):
    
    def __init__(self):
        self.__front_right_sensor = DistanceSensor("front right distance sensor")
        self.__front_left_sensor = DistanceSensor("front left distance sensor")
        self.__rear_right_sensor = DistanceSensor("rear right distance sensor")
        self.__rear_left_sensor = DistanceSensor("rear left distance sensor")

    def get_sensor(self):
        return [self.__front_right_sensor.getValue(),
        self.__front_left_sensor.getValue(),
        self.__rear_right_sensor.getValue(),
        self.__rear_left_sensor.getValue()]

    def print_sensor_value(self):
        print("sensor value :")
        print(self.__front_left_sensor.getValue())
    
class SmashBotGPS(GPS):
    def __init__(self):
        super().__init__('gps')


    def getGPS(self):
        return self.getValues()

    def checkGPS(self):
        borders={
            "right":2.5,
            "left":-2.5,
            "front":2.5,
            "back":-2.5
        }

        limit=0.3

        coord=self.getValues()
        long=[]

        for key,value in borders.items():
            long.append(abs(coord[0]-borders[key]))
            long.append(abs(coord[1]-borders[key]))

        long = min(long)

        if(long<limit):
            print(True)
            return True
        else:
            print(False)
            return False


# create the Robot instance.
robot = SmashBot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getDevice('motorname')
#  ds = robot.getDevice('dsname')
#  ds.enable(timestep)

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()
    gpsVal = robot.gps.getGPS()


    robot.run("forwward")

    if(robot.gps.checkGPS()==True):
        if(turn==1):
            robot.run("right")
        else:
            robot.run("left")
    else:
        robot.run("forward")
        if(random.randint(0,1)==1):
            turn=1
        else:
            turn=0

    # Process sensor data here.

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)

# Enter here exit cleanup code.
