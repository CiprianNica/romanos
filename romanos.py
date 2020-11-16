simbolos ={'M':1000, 'D': 500, 'C': 100, 'L':50, 'X': 10, 'V': 5, 'I': 1}
tipo_5 = ('V', 'L', 'D')
tipo_1 = ('I', 'X', 'C', 'M')

def simbolo_a_entero(simbolo):
    if isinstance(simbolo, str) and simbolo.upper() in simbolos:
        return simbolos[simbolo.upper()]
    elif isinstance(simbolo, str):
        raise ValueError(f"simbolo {simbolo} no permitido")
    else:
        raise ValueError(f"parrametro {simbolo} debe ser un strig")

def romano_a_entero(romano):
    if not isinstance(romano, str):
        raise ValueError(f"parametro{romano} debe ser un strig")

    suma = 0
    c_repes = 0
    valor_anterior = ""


    for letra in romano:
        if letra == valor_anterior and letra in tipo_5:
            raise OverflowError(f'Demasiado simbolos tipo {letra}')
        if letra == valor_anterior:
            c_repes += 1
            if c_repes > 2:
                raise OverflowError(f'Demasiado simbolos tipo {letra}')

        suma = suma + simbolo_a_entero(letra)
        valor_anterior = letra
        
    return suma