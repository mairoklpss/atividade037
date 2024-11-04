#Ler um vetor com 20 idades e exibir a maior e menor.

ListIdades = []

print('digite 20 idades.')
for i in range (1, 21):
    idade = int(input(f"digite a {i}° idade: "))
    ListIdades.append(idade)

maior = max(ListIdades)
menor = min(ListIdades)

print(f"""
a lista de idade: {ListIdades}

a maior idade: {maior}
a menor idade: {menor}
""")
