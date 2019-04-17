Adjective = input('Provide an adjective:')
Name = input('Provide a name:')
Dance = input('Provide a type of dance:')

def capitalize(Name):
    fixed_name = Name.capitalize()
    return fixed_name

def madlibs(Adjective, Name, Dance):
    fixed_name = capitalize(Name)
    return print ('The %s %s likes to %s' % (Adjective, fixed_name, Dance))
    
madlibs(Adjective, Name, Dance)