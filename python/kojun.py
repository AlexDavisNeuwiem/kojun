def imprimir_matriz(matriz, tamanho):
    for i in range(tamanho):
        for j in range(tamanho):
            print(matriz[i][j],end = " ")
        print()
        
def definir_regioes(regioes_matriz, quantidade_regioes, tamanho_matriz):
    regioes = [[] for i in range(quantidade_regioes)]
    
    for i in range(tamanho_matriz):
        for j in range(tamanho_matriz):
            id_regiao = regioes_matriz[i][j]
            regioes[id_regiao].append((i, j))
            
    return regioes
        
def numero_eh_possivel(i, j, num, numeros_matriz, regioes_matriz, regioes, tamanho_matriz):
    id_regiao = regioes_matriz[i][j]
    regiao = regioes[id_regiao]
    
    for (im, jm) in regiao:
        if numeros_matriz[im][jm] == num:
            return False
    
    if (i-1 >= 0) and (numeros_matriz[i-1][j] == num):
        return False
    if (i+1 < tamanho_matriz) and (numeros_matriz[i+1][j] == num):
        return False
    if (j-1 >= 0) and (numeros_matriz[i][j-1] == num):
        return False
    if (j+1 < tamanho_matriz) and (numeros_matriz[i][j+1] == num):
        return False
    
    for it in range(i - 1, -1, -1):
        if regioes_matriz[it][j] != regioes_matriz[i][j]:
            break
        if numeros_matriz[it][j] < num:
            return False
    
    for it in range(i + 1, tamanho_matriz):
        if regioes_matriz[it][j] != regioes_matriz[i][j]:
            break
        if numeros_matriz[it][j] > num:
            return False
    
    return True
 
def Kojun(i, j, numeros_matriz, regioes_matriz, regioes, tamanho_matriz):
 
    if (i == tamanho_matriz - 1 and j == tamanho_matriz):
        return True
    if j == tamanho_matriz:
        return Kojun(i+1, 0, numeros_matriz, regioes_matriz, regioes, tamanho_matriz)
    if numeros_matriz[i][j] > 0:
        return Kojun(i, j + 1, numeros_matriz, regioes_matriz, regioes, tamanho_matriz)
    
    id_regiao = regioes_matriz[i][j]
    regiao = regioes[id_regiao]
    for num in range(1, len(regiao)+1):
     
        if numero_eh_possivel(i, j, num, numeros_matriz, regioes_matriz, regioes, tamanho_matriz):
         
            numeros_matriz[i][j] = num
            if Kojun(i, j + 1, numeros_matriz, regioes_matriz, regioes, tamanho_matriz):
                return True
        numeros_matriz[i][j] = 0
    return False

numeros_matriz = [[2,0,0,0,1,0],
        [0,0,0,3,0,0],
        [0,3,0,0,5,3],
        [0,0,0,0,0,0],
        [0,0,3,0,4,2],
        [0,0,0,0,0,0]]
tamanho_matriz = len(numeros_matriz)

regioes_matriz = [[0 ,0 ,1 ,1 ,1 ,2],
                   [3 ,3 ,3 ,3 ,3 ,2],
                   [4 ,5 ,5 ,5 ,3 ,6],
                   [4 ,4 ,4 ,5 ,6 ,6],
                   [7 ,7 ,8 ,9 ,9 ,9],
                   [10,10,8 ,8 ,9 ,9]]
quantidade_regioes = max(max(row) for row in regioes_matriz) + 1

regioes = definir_regioes(regioes_matriz, quantidade_regioes, tamanho_matriz)
 
if (Kojun(0, 0, numeros_matriz, regioes_matriz, regioes, tamanho_matriz)):
    imprimir_matriz(numeros_matriz, tamanho_matriz)
else:
    print("Sem solução")
