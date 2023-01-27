# # EXO 3

# ## Exigences

# * Mettre en avant un principe de classe abstraite
# * Mettre en avant un principe de polymorphisme
# * Mettre en avant un principe d'héritage multiple
# * Max 3 méthodes par classe (hors getter/setter)
# * Pas d'algorithmes complexes, juste des print ;)
# * En tant que client, je veux pouvoir jouer avec trois types/dérivés de robots différents

# ### Aide

# Sortez un bon vieux crayon pour schématiser vos dépendances d'héritages



from abc import ABCMeta, abstractmethod

""" You can use classes below or create your own 👍️"""

class UnmannedVehicle(metaclass=ABCMeta):
    """ 
        An autonomous vehicle have to do his mission automatically.
        This mission can be configured by an operator.
    """
    @abstractmethod
    def start_mission(self):
        print("mission started!")

    @abstractmethod
    def stop_mission(self):
        print("mission stopped!")

    @abstractmethod
    def do_something_interesting(self):
        print("i'm doing something interesting")


class AerialVehicle(metaclass=ABCMeta):
    """ A vehicle made for ground fields."""
    @abstractmethod
    def do_something_aerial_specific(self):
        print("doing something aerial specific")

class GroundVehicle(metaclass=ABCMeta):
    """ A vehicle made for ground fields."""
    @abstractmethod
    def do_something_ground_specific(self):
        print("doing something ground specific")

class UnderseaVehicle(metaclass=ABCMeta):
    """ A vehicle made for ground fields."""
    @abstractmethod
    def do_something_undersea_specific(self):
        print("doing something undersea specific")

class UAV(UnmannedVehicle, AerialVehicle): 

    """Unmanned Aerial Vehicle"""
    def start_mission(self):
        return super().start_mission()

    def stop_mission(self):
        return super().stop_mission()

    def do_something_interesting(self):
        return super().do_something_interesting()

    def do_something_aerial_specific(self):
        return super().do_something_aerial_specific()

class UUV(UnmannedVehicle, UnderseaVehicle):
    """Unmanned Undersea Vehicle"""
    def start_mission(self):
        return super().start_mission()

    def stop_mission(self):
        return super().stop_mission()

    def do_something_interesting(self):
        return super().do_something_interesting()

    def do_something_undersea_specific(self):
        return super().do_something_undersea_specific()

class UGV(UnmannedVehicle, GroundVehicle):
    """Unmanned Ground Vehicle"""
    def start_mission(self):
        return super().start_mission()

    def stop_mission(self):
        return super().stop_mission()

    def do_something_interesting(self):
        return super().do_something_interesting()

    def do_something_ground_specific(self):
        return super().do_something_ground_specific()


#MAIN
if __name__ == '__main__':

    print("APPEL UAV \n\r")

    uav = UAV()
    uav.do_something_interesting()
    uav.do_something_aerial_specific()

    print("\n\r\n\r APPEL UGV \n\r")

    ugv = UGV()
    ugv.do_something_interesting()
    ugv.do_something_ground_specific()

    print("\n\r\n\r APPEL UUV \n\r")

    uuv = UUV()
    uuv.do_something_interesting()
    uuv.do_something_undersea_specific()

