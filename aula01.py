#Importando as libs para rodar o projeto
import numpy as np
import random as rnd


#Criando a funcao znorm que recebe um parametro X e tem um retorno de um calculo
def znorm(x):
    function = ((x - min(x)) / (max(x) - min(x))) 
    return function 

#Criando uma lista de 20 numeros padronizados, ou seja, em ordem
listaA = list(range(1, 21))

#Criando uma lista de 20 numeros aleatorios com a lib RANDOM e usando o metodo sample para gerar numeros aleatorios 
listaB = rnd.sample(range(1, 21), 20)

#Criando uma nova variavel para criarmos uma MATRIZ 
listaA_np = np.array(listaA)
listaB_np = np.array(listaB)


print(f'''
A matriz nao formatada A recebe = {listaA_np}
A matriz nao formatada B recebe = {listaB_np}
Ambos tem {len(listaA_np)} itens
''')

#Aplicando a funcao para cada uma das listas
listaA_norm = znorm(listaA_np)
listaB_norm = znorm(listaB_np)

print(f'''
      O resultado da aplicacao da nossa funcao na matriz A = \n{listaA_norm}
      O resultado da aplicacao da nossa funcao na matriz B = \n{listaB_norm}
      ''')


#Agora vamos criar a MATRIZ com o metodo transpose para a lista SEM FUNCAO
listaAB = np.transpose([listaA, listaB])

print(f'''
      O resultado da matriz que criamos: \n{listaAB}\n
      ''')

#Agora vamos criar a MATRIZ com o metodo transpose para a lista COM FUNCAO
listaAB_norm = np.transpose([listaA_norm, listaB_norm])
print(f'''
      O resultado da matriz aplicada com a funcao ZNORM que criamos: \n{listaAB_norm}\n
      ''')

#Criando a operacao .dot com normais e com funcao
produtoEntreMatrizes = listaAB.dot(np.transpose(listaAB_norm))


#Criando um looping para mostrar qual lista de estamos percorrendo
i =  0
while i < (len(produtoEntreMatrizes)):
    print(f'Essa e a lista: {i+1} e recebe = \n{produtoEntreMatrizes[i]} \n')
    i+=1
    
