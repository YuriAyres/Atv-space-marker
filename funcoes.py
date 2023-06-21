import pygame
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
    if primeiro_indice >= 950:
        a = primeiro_indice - 150
    elif primeiro_indice >852:
        a = primeiro_indice - 100
    elif primeiro_indice:
        a = primeiro_indice
    if segundo_indice:
        b = segundo_indice - 25
    
    pos2 = (a,b)
    return pos2
def medias_tuplas(dicionario,lista1,lista2):
    tuplas = list(dicionario.values())
    for i in range(len(tuplas)-1):
        tupla_atual = tuplas[i]
        proxima_tupla = tuplas[i+1]
        x_atual, y_atual = tupla_atual
        x_proximo, y_proximo = proxima_tupla
        media_x = (x_atual + x_proximo) / 2
        media_y = (y_atual + y_proximo) / 2
        soma_medias = (media_x,media_y)
        lista1.append(soma_medias)
        resultado = (max(x_atual, x_proximo) - min(x_atual, x_proximo)) + (max(y_atual, y_proximo) - min(y_atual, y_proximo))
        lista2.append(resultado)
    

