import random

def crear_juego():
    """Genera un nuevo juego y devuelve el estado inicial."""
    
    return {
        'numero_secreto' : random.randint(1, 100),
        'intentos' : 0,
        'max_intentos' : 12,
        'terminado' : False
    }
    

def adivinar(numero, estado):
    """

    Recibe el número del usuario y el estado actual.

    Devuelve (resultado_dict, estado_actualizado).

    """
    
    resultado = {
        'pista' : '',
        'mensaje' : '',
        'terminado' : False,
        'gano' : False
    }
    
    if numero < 1 or numero > 100:
        
        resultado['pista'] = 'invalido'
        
        resultado['mensaje'] = 'El numero debe estar entre 1 y 100'
        
        return resultado, estado
        
    estado['intentos'] += 1
    if numero < estado['numero_secreto']:
        resultado['pista'] = 'bajo'
        
        resultado['mensaje'] = '🔺 El número es mayor'
                    
    elif numero > estado['numero_secreto']:
        
        resultado['pista'] = 'alto'
        
        resultado['mensaje'] = '🔻 El número es menor'
            
    elif numero == estado['numero_secreto']:
        
        resultado['pista'] = 'correcto'
        
        resultado['mensaje'] = f'🎉 ¡Correcto! Lo adivinaste en {estado["intentos"]} intentos'
        
        resultado['gano'] = True
        
        resultado['terminado'] = True
        
        estado['terminado'] = True
        
    if estado['intentos'] >= estado['max_intentos'] and not resultado['gano']:
        
        resultado['pista'] = 'perdiste'
        
        resultado['mensaje'] = f'💀 Sin intentos. El número era {estado["numero_secreto"]}'
        
        resultado['terminado'] = True
        
        estado['terminado'] = True
        
    return resultado, estado
