dici = {}

print("=========== CADASTRO DE ALUNOS ===========")

print("Quantos alunos deseja cadastrar? ")
quantidade = int(input("Quantos alunos deseja cadastrar? "))

for i in range(quantidade):
    print(f"Cadastro do {i+1}º aluno: ")

    nome = input("Digite o nome do aluno: ").capitalize()

    hobby = input("Digite o hobby do aluno: ")
    
    dici[nome] =  hobby

for chave,valor in dici.items():
    print(f"Nome: {chave}\nHobby: {valor}\n")