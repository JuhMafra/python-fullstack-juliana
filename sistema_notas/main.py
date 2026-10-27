
# ============================================================
# ARQUIVO PRINCIPAL: main.py
# Sistema de Lançamento de Notas — Nível Fácil
# ============================================================
# Este arquivo orquestra o programa inteiro.
# Ele usa as funções dos módulos em /funcoes para:
#   - Ler e validar entradas do usuário
#   - Salvar e exibir notas em JSON
# ============================================================

from funcoes.validacoes import validar_turma, validar_aluno, validar_nota
from funcoes.arquivo import salvar_nota, ler_notas


def obter_turma():
    """
    Solicita ao usuário o nome da turma em loop até receber uma entrada válida.
    Se o usuário digitar "sair", retorna None para sinalizar encerramento.

    Retorno:
        str ou None
    """
    while True:
        nome_turma = input("Nome da turma: ").strip()

        if nome_turma.lower() == "sair":
            return None

        if validar_turma(nome_turma):
            return nome_turma

        print("Nome da turma inválido. Tente novamente.")


def obter_aluno():
    """
    Solicita ao usuário o nome do aluno em loop até receber uma entrada válida.
    Se o usuário digitar "sair", retorna None.

    Retorno:
        str ou None
    """
    while True:
        nome_aluno = input(
            "\nNome do aluno (ou 'sair'): "
        ).strip()

        if nome_aluno.lower() == "sair":
            return None

        if validar_aluno(nome_aluno):
            return nome_aluno

        print(
            "Nome inválido. Digite o nome e o sobrenome do aluno."
        )


def obter_nota(numero_da_nota):
    """
    Solicita uma nota ao usuário em loop até receber um valor válido.

    Parâmetros:
        numero_da_nota (int): 1, 2 ou 3 — usado na mensagem exibida ao usuário

    Retorno:
        float: a nota validada e convertida
        None: se o usuário digitar "sair"
    """
    while True:
        valor = input(
            f"Nota {numero_da_nota} (ou 'sair'): "
        ).strip()

        if valor.lower() == "sair":
            return None

        nota = validar_nota(valor)

        if nota is not None:
            return nota

        print("Nota inválida. Digite um número entre 0 e 10.")


def main():
    """
    Função principal que coordena o fluxo do programa.
    """
    print("=" * 45)
    print("  Sistema de Lançamento de Notas")
    print("  Digite 'sair' a qualquer momento para encerrar")
    print("=" * 45)

    # Obtém o nome da turma.
    turma = obter_turma()

    if turma is None:
        print("\nEncerrando o sistema. Até logo!")
        return

    # Loop para cadastrar vários alunos.
    while True:

        # Solicita o nome do aluno.
        aluno = obter_aluno()

        if aluno is None:
            break

        # Solicita as três notas.
        nota1 = obter_nota(1)

        if nota1 is None:
            break

        nota2 = obter_nota(2)

        if nota2 is None:
            break

        nota3 = obter_nota(3)

        if nota3 is None:
            break

        # Salva as notas do aluno.
        salvar_nota(turma, aluno, nota1, nota2, nota3)

        print("\nNota salva com sucesso!")

        # Exibe todos os registros da turma.
        ler_notas(turma)

    # Mensagem de encerramento.
    print("\nEncerrando o sistema. Até logo!")


# ── Ponto de entrada do programa ──────────────────────────
# Esta condicional garante que main() só é chamada quando
# este arquivo for executado diretamente (não quando importado).
if __name__ == "__main__":
    main()
