# * Réutiliser la class Robot faite dans l'exo 1. *Sans copier/coller dans le fichier ;)*
# * Un humain doit posséder un sexe attribuable à sa création
# * Un humain doit pouvoir manger un ou plusieurs aliments
# * Un humain doit pouvoir digérer ce qu'il a mangé *pas très important, faire en dernier si vous avez le temps*
# * Un Cyborg doit être une combinaison d'un humain et d'un robot
# * Bonus : ajouter une méthode fun au Cyborg


from exo1 import Robot


# class Robot():
#     # Robot class content here
    
#     pass

class Human():   
    # Human class content here
    __sexe_possibility = ['homme', 'femme', 'autre']
    __sexe ='femme'
    __food = []

    def __init__(self, sexe=None):
        if sexe in self.__sexe_possibility:
            self.__sexe=sexe

    def eat(self, foodasse):
        if type(foodasse)==str:
            self.__food.append(foodasse)
        elif type(foodasse)==list:
            self.__food.extend(foodasse)
        else:
            print("je mange pas c'est dégeulasse")

    def digest(self):
        self.__food.clear()

    @property
    def show_sexe(self):
    #   print("Robot sexe :", self.__sexe)
        return self.__sexe
    
    @property
    def show_food(self):
        return self.__food

class Cyborg(Robot, Human):   

    def __init__(self, name, sexe):   
        Robot.__init__(self, name)
        Human.__init__(self, sexe)

    def FunMethod(self,arg):

        pass

#MAIN
if __name__ == '__main__':


    # r = Robot('robot le robot super robotiquement robotique')
    # r.Status()


    # h = Human('homme')
    # print("sexe de l'humain:", h.show_sexe)
    # h.eat('truc a manger trop bon')
    # print("food eaten by human:", h.show_food)

    # print("---------------")
    # h.eat('truc 2')
    # print("food eaten by human:", h.show_food)

    # cyborg = Cyborg('michel', 'homme')
    # print("sexe du Cyborg:",cyborg.show_sexe)

    # cyborg.eat(4)

    # cyborg.eat('mmmmh du manger trop bon')
    # print("food eaten by Cyborg:", h.show_food)

    # cyborg.digest()

    # print("food after digest:", h.show_food)


    cyborg = Cyborg('Deux Ex Machina', 'M')

    print(cyborg.show_name, 'sexe', cyborg.show_sexe)
    print('Charging battery...')
    cyborg.charge()
    cyborg.status()
    cyborg.eat('banana')
    cyborg.eat(['coca', 'chips'])
    print("food eaten :", cyborg.show_food)
    cyborg.digest()
    print("food eaten after digest:", cyborg.show_food)