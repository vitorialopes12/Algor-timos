#Vitoria Bezerra Lopes
#Receba 100 números inteiros reais. Verifique e mostre o maior e o menor valor. Obs.: somente valores positivos.

def ler_numeros_positivos(qtd):
    numeros = []
    while len(numeros) < qtd:
        try:
            num = float(input(f"Digite o {len(numeros)+1}º número (positivo): "))
            if num > 0:
                numeros.append(num)
            else:
                print("Apenas números positivos são permitidos.")
    return numeros

def encontrar_maior_menor(numeros):
    maior = max(numeros)
    menor = min(numeros)
    return maior, menor
numeros = ler_numeros_positivos(100)
maior, menor = encontrar_maior_menor(numeros)

print(f"\nMaior valor: {maior}")
print(f"Menor valor: {menor}")
