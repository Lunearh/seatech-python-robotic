# EXO 1

## Exigences

# Lorsque je crée mon robot, je veux pouvoir lui attribuer un nom
# Mon robot doit pouvoir s'allumer
# Mon robot doit pouvoir s'éteindre
# Mon robot doit pouvoir charger sa batterie à 100%, allumé ou non
# Le temps de charge ne peut pas être immédiat (10s max)
# Mon robot doit afficher son % de batterie durant sa charge
# Mon robot doit pouvoir enregistrer une vitesse de déplacement
# Mon robot doit pouvoir me donner sa vitesse de déplacement
# Mon robot doit pouvoir arrêter son déplacement sur commande
# Mon robot doit pouvoir me fournir un résumé de son état global

import time



class Robot():
    __name = "<unnamed>"
    __power = False
    __current_speed = 0
    __battery_level = 0
    __states = ['shutown', 'running']
    __current_state = 'shutdown'
    
        
    """
      Give your best code here ( •̀ ω •́ )✧
    """

    # __slots__ = ('name' , 'power', 'speed', 'battery_level', 'current_state')
	
    ROBOT_COUNT = 0
	
    # def __init__(self, name=None):
    #   if name:
    #     self.__name = name
    #   self.__current_state = self.__states[0]
    #   self.__power = False

    def __init__(self, name):
      if(name):
        self.__name= name
      self.__power = True

	
    def allumer(self):
      if(self.__power==False):
        self.__power = True
        print("Robot allumé")
      else:
        print("Robot déjà allumé")


    def eteindre(self):
      if(self.__power==True):
        self.__power = False
        print("Robot éteint")
      else:
        print("Robot déjà éteint")

    def charge(self, level=None):
      if not level:
        level = 100

      bat=self.__battery_level
      for i in range(10):
        if(bat<level):
          bat=bat+10
          time.sleep(1)
          print("Robot chargé à",bat,"%")
      self.__battery_level=bat

    def stop_movement(self):
      self.Speed(0)

    @property
    def show_speed(self):
      return self.__current_speed

    @property
    def show_battery_level(self):
      return self.__battery_level

    @property
    def show_name(self):
      return self.__name

    @property
    def show_state(self):
      return self.__current_state

    def Speed(self, s):
      self.__current_speed = s

    def State(self, sta):
      self.__current_state = sta

    def name(self, n):
      self.__name = n

    

    def status(self):
      print("--------- STATUS -------")
      print("name : ",self.show_name)
      print("state :", self.show_state)
      print("speed :", self.show_speed)
      print("battery level :", self.show_battery_level)
      print("-------------------------")

    
	
    # def __del__(self):
    #   print("%s Auto destruction NOW"%(self.__name))
    #   global ROBOT_COUNT
    #   ROBOT_COUNT -= 1


     	
#MAIN
if __name__ == '__main__':

  # r = Robot(name='Terminator')

  r = Robot('Robert le Robot Robotisé de manière robotique')
  #print("Robot power is %s"%(r.power))
    
  r.allumer()
  r.allumer()
  r.eteindre()
  r.eteindre()


  r.allumer()

  r.charge(30)

  r.Speed(100000000)

  r.status()

  r.stop_movement()

  r.status()