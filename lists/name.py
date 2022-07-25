first_name = 'joao'
middle_name = 'lobo'
family_name = 'guerra'
last_name = 'neto'
genre = 'feminino'
full_name = first_name + " " + middle_name + " " + family_name + " " + last_name
short_name = first_name + " " + middle_name[0:1] + ". " + family_name[0:1] + ". " + last_name
if len(full_name) < 25 or len(family_name) < 10:  
    print('\nWelcome ' + full_name.title())
else:
    print('\nWelcome ' + short_name.title())
