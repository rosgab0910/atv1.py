N = int(input("Digite um número inteiro: "))
fatorial = 1
for i in range(1, N + 1):
    fatorial *= i
print(f"O fatorial de {N} é {fatorial}.")