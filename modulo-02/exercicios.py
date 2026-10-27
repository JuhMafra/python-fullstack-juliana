"""
=============================================================
MÓDULO 2 – Estruturas de Controle
Curso de Capacitação Full Stack – ITEAM

Aluno(a): Juliana Mafra
Data    : 21/10
=============================================================

INSTRUÇÕES:
  1. Substitua <SEU NOME COMPLETO AQUI> e <DATA DE ENTREGA> acima.
  2. Implemente cada função no espaço indicado com # SUA SOLUÇÃO AQUI.
  3. Não apague os comentários de orientação.
  4. Execute o arquivo para testar suas soluções antes de enviar.
  5. Salve este arquivo como modulo-02/exercicios.py, na sua cópia
     do repositório do curso.

COMO EXECUTAR:
  python exercicios.py
=============================================================
"""


# ==============================================================
# EXERCÍCIO 01 – Classificador de Temperatura
# Conceitos: if / elif / else, float(), input()
# ==============================================================
def ex01_classificador_temperatura():
    """
    Lê uma temperatura em Celsius e exibe sua classificação.

    Faixas:
        < 0        → ❄️ Congelante
        0  a 14   → 🥶 Frio
        15 a 24   → 😊 Agradável
        25 a 34   → ☀️ Quente
        >= 35     → 🔥 Muito quente
    """
    temp=float(input("Digite a temperatura em Celsius:"))
    if temp < 0:
        print("❄️ Congelante")
    elif temp> 0 and temp <14:
        print("🥶 Frio")
    elif temp>14 and temp <24:
        print("😊 Agradável")
    elif temp>24 and temp<34:
        print("☀️ Quente")
    elif temp>34:
        print("🔥 Muito quente")
    else:
        print("temperatura invalida")



# ==============================================================
# EXERCÍCIO 02 – Validador de Acesso
# Conceitos: if aninhado, comparação de strings
# ==============================================================
def ex02_validador_acesso():
    """
    Solicita usuário e senha e valida o acesso.

    Credenciais corretas:
        usuário → "admin"
        senha   → "iteam2025"
    """
    user="admin"
    pwd="iteam2025"
    usuario=input("digite seu usuario:")
    senha=input("Digite a senha: ")
    if user == usuario and pwd == senha:
        print("Acesso Validado")
    else:
        print("Usuario ou senha errada")


# ==============================================================
# EXERCÍCIO 03 – Tabuada Interativa
# Conceitos: for, range(), f-string com alinhamento
# ==============================================================
def ex03_tabuada():
    """
    Solicita um número inteiro e exibe sua tabuada de 1 a 10.
    """
    numero = int(input("Digite um número inteiro: "))
    print("\n" + "=" * 30)
    print(f"       TABUADA DO {numero}")
    print("=" * 30)
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero:2} x {i:2} = {resultado:3}")
    print("=" * 30)
    


# ==============================================================
# EXERCÍCIO 04 – Contador Regressivo
# Conceitos: while, print com end=
# ==============================================================
def ex04_contador_regressivo():
    """
    Solicita um número inteiro positivo e faz a contagem
    regressiva até 0, finalizando com '🚀 Lançamento!'.
    """
    numero = int(input("Digite um número inteiro positivo: "))
    while numero <= 0:
        print("Número inválido! Digite um número positivo.")
        numero = int(input("Digite um número inteiro positivo: "))
    for i in range(numero, -1, -1):
        print(i,end="\n")
    print("🚀 Lançamento!")


# ==============================================================
# EXERCÍCIO 05 – Buscador com break
# Conceitos: for, break, enumerate()
# ==============================================================
def ex05_buscador_break():
    """
    Percorre o estoque e localiza 'Monitor', exibindo
    sua posição. Usa break ao encontrar o item.
    """
    estoque = ["Teclado", "Mouse", "Webcam", "Monitor", "Headset", "Notebook"]

    # SUA SOLUÇÃO AQUI
    for posicao, item in enumerate(estoque):
        if item == "Monitor":
            print(f"Monitor encontrado na posição {posicao}")
            break


# ==============================================================
# EXERCÍCIO 06 – Filtro de Dados com continue
# Conceitos: for, continue, None, acumuladores
# ==============================================================
def ex06_filtro_continue():
    """
    Percorre a lista de leituras, ignora os valores None
    com continue e calcula soma, média e total ignorado.
    """
    leituras = [12.5, None, 8.3, None, 15.0, 9.7, None, 11.2, 6.8, None]

    # SUA SOLUÇÃO AQUI
    soma = 0
    total = 0
    ignorados = 0

    for leitura in leituras:
        if leitura is None:
            ignorados += 1
            continue
        soma += leitura
        total += 1

    media = soma / total

    print(f"Soma: {soma}")
    print(f"Média: {media:.2f}")
    print(f"Total ignorado: {ignorados}")

# ==============================================================
# EXERCÍCIO 07 – Validação de Entrada com while
# Conceitos: while True, break, if/elif/else, float()
# ==============================================================
def ex07_validacao_nota():
    """
    Solicita a nota do aluno repetidamente até receber
    um valor válido (0.0 a 10.0), então exibe o conceito.

    Conceitos:
        9.0 a 10.0 → A – Excelente
        7.0 a 8.9  → B – Bom
        5.0 a 6.9  → C – Regular
        < 5.0      → D – Insuficiente
    """
    # SUA SOLUÇÃO AQUI
    while True:
        nota = float(input("Digite a nota do aluno (0 a 10): "))

        if nota < 0 or nota > 10:
            print("Nota inválida! Digite uma nota entre 0 e 10.")
        else:
            break

    if nota >= 9:
        print("A – Excelente")
    elif nota >= 7:
        print("B – Bom")
    elif nota >= 5:
        print("C – Regular")
    else:
        print("D – Insuficiente")

# ==============================================================
# EXERCÍCIO 08 – Calculadora com try/except
# Conceitos: try/except/else/finally, ValueError, ZeroDivisionError
# ==============================================================
def ex08_calculadora_segura():
    """
    Solicita dois números e uma operação (+, -, *, /).
    Trata: ValueError, ZeroDivisionError, operação inválida.
    Usa else para exibir o resultado e finally para encerrar.
    """
    # SUA SOLUÇÃO AQUI
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operacao = input("Digite a operação (+, -, *, /): ")

        if operacao == "+":
            resultado = num1 + num2
        elif operacao == "-":
            resultado = num1 - num2
        elif operacao == "*":
            resultado = num1 * num2
        elif operacao == "/":
            resultado = num1 / num2
        else:
            print("Operação inválida!")
            return

    except ValueError:
        print("Erro: digite números válidos!")
    except ZeroDivisionError:
        print("Erro: não é possível dividir por zero!")
    else:
        print(f"Resultado: {resultado}")
    finally:
        print("Calculadora encerrada.")


# ==============================================================
# EXERCÍCIO 09 – Padrão Numérico com for aninhado
# Conceitos: for aninhado, range(), print com end=
# ==============================================================
def ex09_padrao_numerico():
    """
    Gera o triângulo crescente:
        1
        1 2
        1 2 3
        ...
        1 2 3 4 5

    Desafio extra: gera também o triângulo decrescente logo abaixo.
    """
    # SUA SOLUÇÃO AQUI
    for i in range(1, 6):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

    for i in range(4, 0, -1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


# ==============================================================
# EXERCÍCIO 10 – Jogo de Adivinhação
# Conceitos: while, contador, random, if/elif/else
# ==============================================================
def ex10_jogo_adivinhacao():
    """
    O computador sorteia um número entre 1 e 100.
    O usuário tem 7 tentativas para adivinhar.
    A cada erro, indica se o número é maior ou menor.
    """
    import random
    numero_secreto = random.randint(1, 100)

    # SUA SOLUÇÃO AQUI
    tentativas = 0

    while tentativas < 7:
        palpite = int(input("Digite um número entre 1 e 100: "))
        tentativas += 1

        if palpite == numero_secreto:
            print("Parabéns! Você acertou!")
            break
        elif palpite < numero_secreto:
            print("O número secreto é maior!")
        else:
            print("O número secreto é menor!")

    else:
        print(f"Você perdeu! O número era {numero_secreto}.")


# ==============================================================
# EXERCÍCIO 11 – Verificador de Número Primo
# Conceitos: for, break, try/except, otimização com √n
# ==============================================================
def ex11_numero_primo():
    """
    Solicita um número inteiro positivo e verifica se é primo.
    Usa break ao encontrar o primeiro divisor.
    Trata ValueError e números negativos/zero.
    Otimização: verifica divisores somente até √n.
    """
    # SUA SOLUÇÃO AQUI
    try:
        numero = int(input("Digite um número inteiro positivo: "))

        if numero <= 0:
            print("Digite um número maior que zero.")
            return

        if numero == 1:
            print("Não é primo.")
            return

        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                print("Não é primo.")
                break
        else:
            print("É primo!")

    except ValueError:
        print("Erro: digite um número inteiro válido.")


# ==============================================================
# EXERCÍCIO 12 – Analisador de Senha Forte
# Conceitos: for, if, booleanos, métodos de string
# ==============================================================
def ex12_analisador_senha():
    """
    Analisa se uma senha atende aos critérios de segurança:
        - Mínimo 8 caracteres
        - Pelo menos 1 maiúscula
        - Pelo menos 1 minúscula
        - Pelo menos 1 dígito
        - Pelo menos 1 caractere especial: !@#$%^&*

    Exibe relatório com ✅ ou ❌ para cada critério.
    """
    # SUA SOLUÇÃO AQUI
    senha = input("Digite uma senha: ")

    maiuscula = False
    minuscula = False
    digito = False
    especial = False

    for caractere in senha:
        if caractere.isupper():
            maiuscula = True
        if caractere.islower():
            minuscula = True
        if caractere.isdigit():
            digito = True
        if caractere in "!@#$%^&*":
            especial = True

    print(f"{'✅' if len(senha) >= 8 else '❌'} Mínimo de 8 caracteres")
    print(f"{'✅' if maiuscula else '❌'} Pelo menos 1 maiúscula")
    print(f"{'✅' if minuscula else '❌'} Pelo menos 1 minúscula")
    print(f"{'✅' if digito else '❌'} Pelo menos 1 dígito")
    print(f"{'✅' if especial else '❌'} Pelo menos 1 caractere especial")


# ==============================================================
# EXERCÍCIO 13 – Simulador de Caixa Eletrônico
# Conceitos: while, //, if/else, try/except
# ==============================================================
def ex13_caixa_eletronico():
    """
    Solicita um valor de saque (múltiplo de R$10, máx R$3.000).
    Calcula o menor número de cédulas: R$200, R$100, R$50, R$20, R$10.
    Trata entradas inválidas.
    """
    cedulas = [200, 100, 50, 20, 10]

    # SUA SOLUÇÃO AQUI
    try:
        valor = int(input("Digite o valor do saque (máximo R$ 3.000): "))

        if valor <= 0 or valor > 3000 or valor % 10 != 0:
            print("Valor inválido! Digite um valor múltiplo de R$ 10, entre R$ 10 e R$ 3.000.")
        else:
            for cedula in cedulas:
                quantidade = valor // cedula
                if quantidade > 0:
                    print(f"{quantidade} cédula(s) de R$ {cedula}")
                    valor %= cedula

    except ValueError:
        print("Erro: digite um valor inteiro válido.")

# ==============================================================
# EXERCÍCIO 14 – Leitura de Múltiplos Dados com Tratamento
# Conceitos: while, break, continue, try/except, pass
# ==============================================================
def ex14_leitura_notas_turma():
    """
    Lê notas de uma turma até o usuário digitar 'fim'.
    Ignora notas inválidas com continue + mensagem de aviso.
    Ao encerrar, exibe: total, média, maior e menor nota.
    """
    notas = []

    # SUA SOLUÇÃO AQUI
    while True:
        entrada = input("Digite uma nota ou 'fim' para encerrar: ")

        if entrada.lower() == "fim":
            break

        try:
            nota = float(entrada)
        except ValueError:
            print("Nota inválida! Tente novamente.")
            continue

        notas.append(nota)

    if len(notas) > 0:
        print(f"Total de notas: {len(notas)}")
        print(f"Média: {sum(notas) / len(notas):.2f}")
        print(f"Maior nota: {max(notas)}")
        print(f"Menor nota: {min(notas)}")
    else:
        print("Nenhuma nota foi informada.")


# ==============================================================
# EXERCÍCIO 15 – Desafio Final: Menu de Sistema
# Conceitos: while True, if/elif/else, break, continue, try/except
# ==============================================================

def menu():
    while True:
        print("\n" + "=" * 50)
        print("MÓDULO 2 – Estruturas de Controle")
        print("Aluno(a): Juliana Mafra")
        print("=" * 50)

        print("01 - Classificador de temperatura")
        print("02 - Validador de acesso")
        print("03 - Tabuada")
        print("04 - Contador regressivo")
        print("05 - Buscador com break")
        print("06 - Filtro com continue")
        print("07 - Validação de nota")
        print("08 - Calculadora segura")
        print("09 - Padrão numérico")
        print("10 - Jogo de adivinhação")
        print("11 - Número primo")
        print("12 - Analisador de senha")
        print("13 - Caixa eletrônico")
        print("14 - Leitura de notas da turma")
        print("0  - Sair")
        print("=" * 50)

        opcao = input("Qual exercício deseja executar? ").strip()

        if opcao == "1" or opcao == "01":
            ex01_classificador_temperatura()

        elif opcao == "2" or opcao == "02":
            ex02_validador_acesso()

        elif opcao == "3" or opcao == "03":
            ex03_tabuada()

        elif opcao == "4" or opcao == "04":
            ex04_contador_regressivo()

        elif opcao == "5" or opcao == "05":
            ex05_buscador_break()

        elif opcao == "6" or opcao == "06":
            ex06_filtro_continue()

        elif opcao == "7" or opcao == "07":
            ex07_validacao_nota()

        elif opcao == "8" or opcao == "08":
            ex08_calculadora_segura()

        elif opcao == "9" or opcao == "09":
            ex09_padrao_numerico()

        elif opcao == "10":
            ex10_jogo_adivinhacao()

        elif opcao == "11":
            ex11_numero_primo()

        elif opcao == "12":
            ex12_analisador_senha()

        elif opcao == "13":
            ex13_caixa_eletronico()

        elif opcao == "14":
            ex14_leitura_notas_turma()

        elif opcao == "0":
            print("Encerrando o programa. Até mais!")
            break

        else:
            print("Opção inválida! Escolha um exercício de 1 a 15 ou 0 para sair.")
            continue

        input("\nPressione ENTER para voltar ao menu...")


# Executa o menu principal
menu()

# ==============================================================
# EXECUÇÃO PRINCIPAL
# Descomente as chamadas dos exercícios que você já resolveu.
# ==============================================================
if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("MÓDULO 2 – Estruturas de Controle")
    print(f"Aluno(a): Juliana Mafra")
    print("=" * 50)
    menu()
    # Descomente linha por linha conforme for resolvendo:
    #ex01_classificador_temperatura()
    # ex02_validador_acesso()
    # ex03_tabuada()
    # ex04_contador_regressivo()
    # ex05_buscador_break()
    # ex06_filtro_continue()
    # ex07_validacao_nota()
    # ex08_calculadora_segura()
    # ex09_padrao_numerico()
    # ex10_jogo_adivinhacao()
    # ex11_numero_primo()
    # ex12_analisador_senha()
    # ex13_caixa_eletronico()
    # ex14_leitura_notas_turma()
    # ex15_menu_sistema()
