def analisar_tupla(tupla,valorx,valory):
    primeiro_indice = tupla[0]
    segundo_indice = tupla[1]
    if primeiro_indice > valorx:
        return True
       
    elif segundo_indice > valory:
        return True
    
    else:
        return False
    
def sutrair_tupla(tupla):
    primeiro_indice = tupla[0]
    segundo_indice = tupla[1]
    if primeiro_indice > 950:
        a = primeiro_indice - 150
    elif primeiro_indice >852:
        a = primeiro_indice - 70
    elif primeiro_indice:
        a = primeiro_indice
    if segundo_indice:
        b = segundo_indice - 25
    
    pos2 = (a,b)
    return pos2