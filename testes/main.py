import json

dados ={"nome":"caneta","preco":2.51}

with open("./dados.json","w",encoding="utf-8") as f:
    json.dump(dados,f,ensure_ascii=False,indent=2)

with open("./dados.json", encoding="utf-8") as f:
    print(json.load(f)["nome"])

print(json.dumps(dados))