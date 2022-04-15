from Module import Person, Wizard

person = Person('Batman')
wizard = Wizard(Person('Gandalf'))

def test_winner():
    expected_result = 'Batman'
    person.hit(wizard)
    wizard.hit(person)
    if(person.life_points > wizard.life_points):
        actual_result = person.name
    else:
        actual_result = wizard.name
    assert expected_result == actual_result