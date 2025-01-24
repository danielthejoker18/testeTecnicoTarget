#questao 1
INDICE = 13
SOMA = 0
K = 0

while K < INDICE:
    K = K + 1
    SOMA = SOMA + K

print(SOMA)

#questao 2
def is_fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n

numero = int(input("Digite um número: "))
if is_fibonacci(numero):
    print(f"{numero} pertence à sequência de Fibonacci.")
else:
    print(f"{numero} não pertence à sequência de Fibonacci.")

#questao 3
faturamento_diario = [1000, 1500, 2000, 0, 3000, 0, 4000, 5000, 6000, 0, 7000, 8000, 9000, 10000, 11000, 12000, 0, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000, 24000, 25000]
faturamento_diario_filtrado = [valor for valor in faturamento_diario if valor > 0]

media_mensal = sum(faturamento_diario_filtrado) / len(faturamento_diario_filtrado)

menor_valor = min(faturamento_diario_filtrado)
maior_valor = max(faturamento_diario_filtrado)

dias_acima_media = sum(1 for valor in faturamento_diario_filtrado if valor > media_mensal)

print(f"Menor valor de faturamento diário: R${menor_valor:.2f}")
print(f"Maior valor de faturamento diário: R${maior_valor:.2f}")
print(f"Número de dias no mês com faturamento acima da média: {dias_acima_media}")

#questao 5
faturamento_estados = {
    'SP': 67836.43,
    'RJ': 36878.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

total_faturamento = sum(faturamento_estados.values())

for estado, valor in faturamento_estados.items():
    percentual = (valor / total_faturamento) * 100
    print(f"Percentual de representação de {estado}: {percentual:.2f}%")

#questao 5
def inverter_string(string):
    string_invertida = ""

    for i in range(len(string) - 1, -1, -1):
        string_invertida += string[i]
    
    return string_invertida

string_original = "Hello, World!"
string_invertida = inverter_string(string_original)
print(f"String original: {string_original}")
print(f"String invertida: {string_invertida}")