#nome = input("Digite seu nome: ")
#idade = int(input("Digite sua idade: "))
#ano_nascimento = 2026 - idade
#print(f"Olá, {nome}! Você tem {idade} anos e nasceu por volta de {ano_nascimento}.")
###########
idade = int(input("Idade: "))
est= input("estudante? (S/n)") == "s"
if idade <12 or idade >=60:
    preco=10
elif est:
    preco=15
else:
    preco = 30
print(f"Ingresso: R$ {preco:.2f}")