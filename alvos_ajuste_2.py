
# Essa seria uma boa forma de usar o continue
# Se esse alvo não estiver ativo, "continue" para o próximo, ignorando o código de ataque depois dele

portas = (8080, 443, 21, 22)

alvos = [
    {'ip': '10.10.0.1', 'ativo': True, 'SO': 'Linux', 'portas': portas},
    {'ip': '10.10.0.2', 'ativo': False, 'SO': 'Linux', 'portas': portas},
    {'ip': '10.10.0.3', 'ativo': True, 'SO': 'Windows', 'portas': portas},
    {'ip': '10.10.0.4', 'ativo': False, 'SO': 'Windows', 'portas': portas},
    {'ip': '10.10.0.5', 'ativo': True, 'SO': 'MacOS', 'portas': portas},
    {'ip': '10.10.0.6', 'ativo': False, 'SO': 'MacOS', 'portas': portas}
]

for alvo in alvos:
    if not alvo["ativo"]:
        continue    # Um bom "continue" aqui

    if alvo["SO"] == "Linux":
        print("atacando o sistema Linux com o IP --> " + alvo["ip"])
        print("___####______####____")
        for porta in alvo["portas"]:
            print("atacando a porta: " + str(porta))
    elif alvo["SO"] == "Windows":
        print("atacando o sistema Windows com o IP --> " + alvo["ip"])
        print("___####______####____")
        for porta in alvo["portas"]:
            print("atacando a porta: " + str(porta))
    elif alvo["SO"] == "MacOS":
        print("atacando o sistema MacOS (Apple) com o IP --> " + alvo["ip"])
        print("___####______####____")
        for porta in alvo["portas"]:
            print("atacando a porta: " + str(porta))
