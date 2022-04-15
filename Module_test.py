from Module import Person, Wizard, HealthPotion

person = Person('Batman')
wizard = Wizard(Person('Gandalf'), 'Gandalf')

def test_potion_person():
    expected_result = True
    hp_before_potion = person.get_life_points  
    HealthPotion.was_used_by(person)
    hp_after_potion = person.get_life_points
    if hp_before_potion < hp_after_potion:
        actual_result = True
    else:
        actual_result = False
    assert expected_result == actual_result
    
def test_potion_wizard():
    expected_result = True
    hp_before_potion = wizard.get_life_points  
    HealthPotion.was_used_by(wizard)
    hp_after_potion = wizard.get_life_points
    if int(hp_before_potion) < int(hp_after_potion):
        actual_result = True
    else:
        actual_result = False
    assert expected_result == actual_result    

def test_person_suicide():
    expected_result = True
    while person.life_points > 0:
        person.hit(person)
    actual_result = person.is_dead()
    assert expected_result == actual_result
    
def test_wizard_suicide():
    expected_result = True
    while wizard.life_points > 0:
        wizard.hit(wizard)
    actual_result = wizard.is_dead()
    assert expected_result == actual_result

def test_death_duel_person_first_no_heal():
    expected_result = 'Gandalf' 
    while person.life_points > 0 & wizard.life_points > 0: 
        person.hit(wizard)
        wizard.hit(person)        
    if(person.life_points > wizard.life_points):
        actual_result = person.name
    else:
        actual_result = wizard.name
    assert expected_result == actual_result
    
def test_death_duel_wizard_first_no_heal():
    expected_result = 'Gandalf'
    while person.life_points > 0 & wizard.life_points > 0:
        wizard.hit(person)
        person.hit(wizard)    
    if(person.life_points > wizard.life_points):
        actual_result = person.name
    else:
        actual_result = wizard.name
    assert expected_result == actual_result