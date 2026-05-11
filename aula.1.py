temperaturas = [
    [28, 31, 34, 33],
    [25, 27, 29, 28],
    [32, 35, 36, 34],
    [24, 26, 25, 27]]


mais_critico = 0
maior_sala = 0

for i in range(len(temperaturas)):
    sala = temperaturas[i]

    media = sum(sala) / len(sala)

    criticos = 0
    for temp in sala:
        if temp >= 33:
            criticos += 1

        if temp > mais_critico:
            mais_critico = temp
            maior_sala = i + 1

    print (f"Sala - { i + 1}")
    print (f"Média das temperaturas - {media}")
    print (f"Registros Criticos - {criticos}")
    print()

    if criticos > mais_critico:
        mais_critico = criticos
        maior_sala = i + 1

print (f"Sala com maior risco: Sala {maior_sala}")
print (f"Temperatura mais critica: {mais_critico}")