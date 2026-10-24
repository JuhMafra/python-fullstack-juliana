print("hello world!!!")
print("Juliana Mafra")
print("Python: simples, poderoso e elegante.\n\n")

COMANDOS={}
def comando(nome):
    def registrar(funcao):
        COMANDOS[nome] = funcao
        return funcao
    return registrar

@comando("oi")
def saudar():
    return "olá"

@comando("tchau")
def despedir():
    return "adeus"

print(COMANDOS["oi"](),"\n",COMANDOS["tchau"]())