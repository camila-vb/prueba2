"""este programa es para determinar si una palabra es palidroma"""
def esPal(x):
    """Funcion que x es lista y devuelve valor boobleano si los elementos
de la lista son iguales al invertir la palabra  """
    assert type(x) == list
    temp = x[:] #crea una copia de x 
    temp.reverse() #se añadio los parentesis para ejecutar la funcion
    print(temp , x)
    if temp == x:
        return True
    else:
        return False

def palabra(n):
    """asume que n es palabra  y devuelve si es True o False"""
    result = []
    for i in range(n):
        elem = input('Entrar letra: ')
        result.append(elem)
    print(result)
    if esPal(result):
        print('Si es palindromo ')
    else:
        print('No es palindromo ')


## Testing para validar :
## abcd     n = 4
## ana      n = 3
## hola     n = 4
## abccba   n = 6
## abba     n = 4
