full_dot = '●'
empty_dot = '○'

def create_character(name , strength , intelligence , charisma):
    if not isinstance(name , str):
        return print("The character name should be a string")
    elif len(name) == 0:
        return print('The character should have a name')
    elif len(name) > 10 :
        return print('The character name is too long')
    elif " " in name :
        return print('The character name should not contain spaces')


    if not isinstance(strength , int) or not isinstance(intelligence , int) or not isinstance(charisma , int):
        return "All stats should be integers"
    elif strength < 1 or intelligence < 1 or charisma < 1 :
        return "All stats should be no less than 1"
    elif strength > 4 or intelligence > 4 or charisma > 4 :
        return "All stats should be no more than 4"
    elif charisma + intelligence + strength != 7 :
        return 'The character should start with 7 points'


    four_line_str = f"{name}\nSTR {full_dot*strength}{empty_dot*(10 - strength)}\nINT {full_dot*intelligence}{empty_dot*(10 - intelligence)}\nCHA {full_dot*charisma}{empty_dot*(10 - charisma)}"
    return print(four_line_str) #it prints the output to terminal and returns None.

create_character('' , 3 , 3 , 5)
create_character('ahmed', 4, 2, 1)
create_character(6.34 , 2 , 5 , 6)
