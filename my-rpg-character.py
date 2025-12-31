full_dot = 'o'
empty_dot = '-'
def create_character(name, constitution, strength, intelligence, dexterity):
    if not isinstance(name, str):
        return 'The character name should be a string'
    if not name:
        return 'The character should have a name'
    if len(name) > 10:
        return 'The character name is too long'
    if ' ' in name:
        return 'The character name should not contain spaces'
    
    stats = {'CON':constitution, 'STR':strength, 'INT':intelligence, 'DEX':dexterity} 
    for stat in stats.values():
        if not isinstance(stat, int):
            return 'All stats should be integers'
        if stat < 1:
            return 'All stats should be no less than 1'
        if stat > 4:
            return 'All stats should be no more than 4'
    if stats['CON'] + stats['STR'] + stats['INT'] + stats['DEX'] != 10:
        return 'The character should start with 10 points'
    # Se retorna la llave y el valor (items) de cada dato dentro del diccionario
    for key, stat in stats.items():
        name += f'\n{key} {full_dot*stat}{empty_dot*(10-stat)}'
    return name

print(create_character('Josh',4,4,1,1))