# Candidatos a Prefeito
prefeitos = {10: {'nome': 'Pedro', 'partido': 'Partido Democrata', 'votos': 0},
             20: {'nome': 'Carlos', 'partido': 'Partido Social', 'votos': 0},
             30: {'nome': 'Cleber', 'partido': 'Partido PC do B', 'votos': 0},
             40: {'nome': 'Ana', 'partido': 'Partido PL', 'votos': 0}}

# Candidatos a Vereadores
vereadores = {10001: {'nome': 'Carla', 'partido': 'Partido Democrata', 'votos': 0},
              10002: {'nome': 'Jose', 'partido': 'Partido Democrata', 'votos': 0},
              10003: {'nome': 'Emanuel', 'partido': 'Partido Democrata', 'votos': 0},
              # Lista continua...
              10010: {'nome': 'Jailton', 'partido': 'Partido PL', 'votos': 0},
              10011: {'nome': 'Eliane', 'partido': 'Partido PL', 'votos': 0}}

# Contagem de votos em branco
votos_branco_prefeito = 0
votos_branco_vereador = 0

# Função para imprimir a "zerésima", mostrando todos os candidatos sem votos computados
def imprimir_zeresima():
    print("Zerésima: Nenhum voto computado.\n")
    for candidato in prefeitos.values():
        print(f"Prefeito {candidato['nome']} ({candidato['partido']}): {candidato['votos']} votos")
    for candidato in vereadores.values():
        print(f"Vereador {candidato['nome']} ({candidato['partido']}): {candidato['votos']} votos")
    print(f"Votos em branco para Prefeito: {votos_branco_prefeito}")
    print(f"Votos em branco para Vereador: {votos_branco_vereador}\n")

# Função principal de votação
def iniciar_votacao():
    global votos_branco_prefeito, votos_branco_vereador
    while True:
        # Votação para prefeito
        print("Vote para Prefeito (insira o número do candidato ou digite 0 para votar em branco):")
        numero = int(input())
        if numero == 0:
            votos_branco_prefeito += 1
            print("Voto em branco para prefeito confirmado.\n")
        elif numero in prefeitos:
            confirmar_voto('Prefeito', prefeitos[numero])
        else:
            print("Voto nulo para prefeito.\n")
        
        # Votação para vereador
        print("Vote para Vereador (insira o número do candidato ou digite 0 para votar em branco):")
        numero = int(input())
        if numero == 0:
            votos_branco_vereador += 1
            print("Voto em branco para vereador confirmado.\n")
        elif numero in vereadores:
            confirmar_voto('Vereador', vereadores[numero])
        else:
            print("Voto nulo para vereador.\n")
        
        # Finalizar ou continuar
        continuar = input("Finalizar a votação ou continuar? (F/C): ").lower()
        if continuar == 'f':
            totalizar_votos()
            break

# Função para confirmar e registrar o voto no sistema
def confirmar_voto(cargo, candidato):
    print(f"Você votou em {candidato['nome']} ({candidato['partido']}) para {cargo}. Confirma? (S/N)")
    confirmar = input().lower()
    if confirmar == 's':
        candidato['votos'] += 1
        print(f"Voto confirmado para {candidato['nome']}.\n")
    else:
        print("Voto não confirmado.\n")

# Função para totalizar votos e declarar vencedores
def totalizar_votos():
    print("\nTotalização dos votos:\n")
    for candidato in prefeitos.values():
        print(f"Prefeito {candidato['nome']} ({candidato['partido']}): {candidato['votos']} votos")
    for candidato in vereadores.values():
        print(f"Vereador {candidato['nome']} ({candidato['partido']}): {candidato['votos']} votos")
    
    print(f"Votos em branco para Prefeito: {votos_branco_prefeito}")
    print(f"Votos em branco para Vereador: {votos_branco_vereador}\n")
    
    # Determinar vencedor para prefeito
    vencedor_prefeito = max(prefeitos.values(), key=lambda c: c['votos'])
    empate_prefeito = [c for c in prefeitos.values() if c['votos'] == vencedor_prefeito['votos']]
    
    if len(empate_prefeito) > 1:
        print("Houve um empate para Prefeito. Um segundo turno será necessário.\n")
    else:
        print(f"O vencedor para Prefeito é {vencedor_prefeito['nome']} ({vencedor_prefeito['partido']}) com {vencedor_prefeito['votos']} votos.\n")
    
    # Determinar os três vereadores com mais votos
    vereadores_ordenados = sorted(vereadores.values(), key=lambda c: c['votos'], reverse=True)
    eleitos = [v for v in vereadores_ordenados if v['votos'] > 0][:3]  # Apenas os que receberam votos
    
    if len(eleitos) < 3:
        print("Não houve vereadores suficientes eleitos com votos válidos.")
    else:
        print("Os três vereadores mais votados são:")
        for i, vereador in enumerate(eleitos, start=1):
            print(f"{i}. {vereador['nome']} ({vereador['partido']}) com {vereador['votos']} votos")

# Menu inicial para o usuário escolher entre imprimir a zerésima ou iniciar a votação
while True:
    print("1. Imprimir Zerésima")
    print("2. Iniciar Votação")
    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        imprimir_zeresima()
    elif opcao == 2:
        iniciar_votacao()
        break
