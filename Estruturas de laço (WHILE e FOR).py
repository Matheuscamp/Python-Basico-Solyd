qtd_Pessoas = int(input("Digite a quantidade de convidados: "))
lista_Convidados = []

for i in range(qtd_Pessoas):
    convidado = input(f"Digite o nome do {i + 1} convidado: ")
    lista_Convidados.append(convidado)

print("\nLista de Convidados:")
for convidado in lista_Convidados:
    print(convidado)
