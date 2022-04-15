from Module import Person, Wizard, HealthPotion
from main import Duel

# potion
def test_potion_person():
    person = Person('Batman')
    expected_result = True
    hp_before_potion = person.get_life_points()
    HealthPotion.was_used_by(person)
    hp_after_potion = person.get_life_points()
    if hp_before_potion < hp_after_potion:
        actual_result = True
    else:
        actual_result = False
    assert expected_result == actual_result
    
def test_potion_wizard():
    wizard = Wizard('Gandalf')
    expected_result = True
    hp_before_potion = wizard.get_life_points()
    HealthPotion.was_used_by(wizard)
    hp_after_potion = wizard.get_life_points()
    if hp_before_potion < hp_after_potion:
        actual_result = True
    else:
        actual_result = False
    assert expected_result == actual_result    

# suicide
def test_suicide_person():
    person = Person('Batman')
    expected_result = True
    while person.life_points > 0:
        person.hit(person)
    actual_result = person.is_dead()
    assert expected_result == actual_result
    
def test_suicide_wizard():
    wizard = Wizard('Gandalf')
    expected_result = True
    while wizard.life_points > 0:
        wizard.hit(wizard)
    actual_result = wizard.is_dead()
    assert expected_result == actual_result

# duel no heal
def test_death_duel_no_heal_person():
    person = Person('Batman')
    wizard = Wizard('Gandalf')
    expected_result = 'Gandalf' 
    while person.life_points > 0 and wizard.life_points > 0: 
        person.hit(wizard)
        wizard.hit(person)        
    if(person.life_points > wizard.life_points):
        actual_result = person.name
    else:
        actual_result = wizard.name
    assert expected_result == actual_result
    
def test_death_duel_no_heal_wizard():    
    person = Person('Batman')
    wizard = Wizard('Gandalf')
    expected_result = 'Gandalf'
    while person.get_life_points() > 0 and wizard.get_life_points() > 0:
        wizard.hit(person)
        person.hit(wizard)    
    if(person.get_life_points() > wizard.get_life_points()):
        actual_result = person.name
    else:
        actual_result = wizard.name
    assert expected_result == actual_result
 
# duel - heal   
def test_death_duel_heal_person():
    person = Person('Batman')
    wizard = Wizard('Gandalf')
    expected_result = 'Batman'
    while person.get_life_points() > 0 and wizard.get_life_points() > 0:
        person.hit(wizard)
        wizard.hit(person)
        HealthPotion.was_used_by(person)
        # print("person HP: ", person.get_life_points())
        # print("wizard HP: ", wizard.get_life_points())
    if(person.get_life_points() > wizard.get_life_points()):
        actual_result = person.name
    else:
        actual_result = wizard.name
    assert expected_result == actual_result
 
def test_death_duel_heal_wizard():
    person = Person('Batman')
    wizard = Wizard('Gandalf')
    expected_result = 'Gandalf'
    while person.get_life_points() > 0 and wizard.get_life_points() > 0:
        person.hit(wizard)
        wizard.hit(person)
        HealthPotion.was_used_by(wizard)
        # print("person HP: ", person.get_life_points())
        # print("wizard HP: ", wizard.get_life_points())
    if(person.get_life_points() > wizard.get_life_points()):
        actual_result = person.name
    else:
        actual_result = wizard.name
    assert expected_result == actual_result
    
def test_death_duel_heal():
    person = Person('Batman')
    wizard = Wizard('Gandalf')
    expected_result = 'Gandalf'
    while person.get_life_points() > 0 and wizard.get_life_points() > 0:
        person.hit(wizard)
        wizard.hit(person)
        # HealthPotion.was_used_by(wizard)
        # HealthPotion.was_used_by(person)
    if(person.get_life_points() > wizard.get_life_points()):
        actual_result = person.name
    else:
        actual_result = wizard.name
    assert expected_result == actual_result
  
# negative life gain  
def test_death_person():    
    person = Person('Batman')
    expected_result = True
    person.gained_life_points(-person.get_life_points())
    if(person.is_dead):
        actual_result = True
    else:
        actual_result = False
    assert actual_result == expected_result
    
def test_death_wizard():    
    wizard = Wizard('Gandalf')
    expected_result = True
    wizard.gained_life_points(-wizard.get_life_points())
    if(wizard.is_dead):
        actual_result = True
    else:
        actual_result = False
    assert actual_result == expected_result
  
# life gain  
def test_life_gain_person():
    person = Person('Batman')
    expected_result = True
    hp_before_potion = person.get_life_points()
    person.gained_life_points(1)
    hp_after_potion = person.get_life_points()
    if hp_before_potion < hp_after_potion:
        actual_result = True
    else:
        actual_result = False
    assert expected_result == actual_result
    
def test_life_gain_wizard():
    wizard = Wizard('Gandalf')
    expected_result = True
    hp_before_potion = wizard.get_life_points()
    wizard.gained_life_points(1)
    hp_after_potion = wizard.get_life_points()
    if hp_before_potion < hp_after_potion:
        actual_result = True
    else:
        actual_result = False
    assert expected_result == actual_result 
    
# potion + life gain
def test_potion_plus_life_gain_person():
    person = Person('Batman')
    expected_result = 11
    hp_before_potion_and_life_gain = person.get_life_points()
    HealthPotion.was_used_by(person)
    person.gained_life_points(1)
    hp_after_potion_and_life_gain = person.get_life_points()
    actual_result = hp_after_potion_and_life_gain - hp_before_potion_and_life_gain
    assert expected_result == actual_result
    
def test_potion_plus_life_gain_wizard():
    wizard = Wizard('Gandalf')
    expected_result = 11
    hp_before_potion_and_life_gain = wizard.get_life_points()
    HealthPotion.was_used_by(wizard)
    wizard.gained_life_points(1)
    hp_after_potion_and_life_gain = wizard.get_life_points()
    actual_result = hp_after_potion_and_life_gain - hp_before_potion_and_life_gain
    assert expected_result == actual_result