nome = "Mariana Souza"
cargo = "Analista de Dados"
salario = 7850.50
anos = 3

print("=============================")
print("     FICHA DO FUNCIONÁRIO")
print("=============================")
print(f"Nome   : {nome}")
print(f"Cargo  : {cargo}")
print(f"Salário: R$ {salario:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
print(f"Tempo  : {anos} ano(s) de empresa")
print("=============================")