# Conditions within functions
# Calling the function with parameters and returning the values
def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'


print(greet('en'), 'Sally!')
print(greet('es'), 'Maria!')
print(greet('hr'), 'Zlatan!')
print(greet('fr'), 'Susanna!')

