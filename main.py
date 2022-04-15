from Module import Person, Wizard, HealthPotion
import numpy as np

user_1 = Person("Hero")
user_2 = Wizard("Wizard")

def Duel():
    
    hits = []
    potions = []
    turn = 1
    
    print("The duel begins")
    
    print("Hero's HP : " + str(user_1.get_life_points()))
    print("Wizard's HP : " + str(user_2.get_life_points()))
    
    print("-----------------------")
    
    while user_1.is_dead() == False and user_2.is_dead() == False:
        
        print("* Round " + str(turn) + " *")
        
        random = np.random.randint(2)        
        
        if random == 1:
            user_1.hit(user_2)
            hits.append(user_1.name)
            print("> Hero hits Wizard")
            print("Wizard's HP after the hit : " + str(user_2.get_life_points()))
        else:
            user_2.hit(user_1)
            hits.append(user_2.name)
            print("> Wizard hits Hero")
            print("Hero's HP after the hit : " + str(user_1.get_life_points()))

        random_health_potion_use = np.random.randint(3)
        
        if random_health_potion_use == 0:
            HealthPotion.was_used_by(user_1)
            potions.append(user_1.name)
            print("> Hero uses a potion")
            print("Hero's HP after the potion : " + str(user_1.get_life_points()))
        elif random_health_potion_use == 1: # heal wizard
            HealthPotion.was_used_by(user_2)
            potions.append(user_2.name)
            print("> Wizard uses a potion")
            print("Wizard's HP after the potion : " + str(user_2.get_life_points()))
        else:
            print("> No potion used")
            potions.append("no pot")
            pass
        turn += 1
        
        print("Hero's HP at the of turn " + str(turn) + " : " + str(user_1.get_life_points()))
        print("Wizard's HP at the end of turn " + str(turn) + " : " + str(user_2.get_life_points()))
        
        print("-----------------------")
        
    if(user_1.get_life_points() > user_2.get_life_points()):
        print(user_1.name + " wins")
    elif(user_1.get_life_points() < user_2.get_life_points()):
        print(user_2.name + " wins")
    else:
        print("draw")
        
    print("Total hits Hero : " + str(hits.count("Hero")))
    print("Total hits Wizard : " + str(hits.count("Wizard")))
    print("Total potions Hero : " + str(potions.count("Hero")))
    print("Total potions Wizard : " + str(potions.count("Wizard")))
    # print("potions : " + str(potions))
    # print("nb of turns : " + str(turn))
    
            
Duel()