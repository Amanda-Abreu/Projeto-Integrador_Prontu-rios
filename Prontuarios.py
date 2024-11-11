#Lista com nomes dos pacientes
pacientes = ["Maria da dores", "Edson santos", "Edna Silveira", "Vania cristina silva", "Beatriz da silva santos", "Amanda silva santos", "Priscila pereira", "Felipe macedo santos", "Marcia oliveira"]

#Armazenar os prontuários dos pacientes
prontuarios = {
    "Maria das dores".lower(): {
        "Numero_prontuario": 103,
        "Sala": "2A",
        "Responsavel":"João Macedo",
        "Data": "2024-10-23"
    },
    "Edson santos".lower(): {
        "Numero_prontuario": 102,
        "Sala": "2A",
        "Responsavel":"Mariana Silva",
        "Data": "2024-10-20"
    },
    "Edna silveira".lower(): {
        "Numero_prontuario": 101,
        "Sala": "3C",
        "Responsavel":"Mariana Silva",
        "Data": "2024-10-19"
    },
    "Vania cristina silva".lower(): {
        "Numero_prontuario": 104,
        "Sala": "3C",
        "Responsavel":"Viviane Nogueira",
        "Data": "2024-10-23"
    },
    "Beatriz da silva santos".lower(): {
        "Numero_prontuario": 105,
        "Sala": "2A",
        "Responsavel":"João Macedo",
        "Data": "2024-10-23"
    },
    "Amanda silva santos".lower(): {
        "Numero_prontuario": 106,
        "Sala": "2B",
        "Responsavel":"Viviane Nogueira",
        "Data": "2024-10-23"
    },
    "Priscila pereira".lower(): {
        "Numero_prontuario": 107,
        "Sala": "2B",
        "Responsavel":"Viviane Nogueira",
        "Data": "2024-10-23"
    },
    "Felipe macedo santos".lower(): {
        "Numero_prontuario": 108,
        "Sala": "3C",
        "Responsavel":"João Macedo",
        "Data": "2024-10-23"
    },
    "Marcia oliveira".lower(): {
        "Numero_prontuario": 109,
        "Sala": "2B",
        "Responsavel":"Marina Nogueira",
        "Data": "2024-10-23"
    }

}

# Função para exibir prontuário
def exibir_prontuario():
    nome_paciente = input("Digite o nome do paciente: ").lower()
    if nome_paciente in prontuarios:
        prontuario = prontuarios[nome_paciente]
        print(f"\nProntuário de {nome_paciente.title()}:")
        print("Número do Prontuário:", prontuario["Numero_prontuario"])
        print("Sala:", prontuario["Sala"])
        print("Responsável:", prontuario["Responsavel"])
        print("Data:", prontuario["Data"])
    else:
        print("Paciente não encontrado.\n")

# Função para adicionar novo paciente
def adicionar_paciente():
    nome_paciente = input("Digite o nome do novo paciente: ").lower()
    if nome_paciente in prontuarios:
        print("Este paciente já existe no sistema.\n")
    else:
        numero_prontuario = int(input("Digite o número do prontuário: "))
        sala = input("Digite a sala: ")
        responsavel = input("Digite o nome do responsável: ")
        data = input("Digite a data (YYYY-MM-DD): ")
        
        prontuarios[nome_paciente] = {
            "Numero_prontuario": numero_prontuario,
            "Sala": sala,
            "Responsavel": responsavel,
            "Data": data
        }
        pacientes.append(nome_paciente.title())
        print(f"Paciente {nome_paciente.title()} adicionado com sucesso.\n")

# Menu principal
while True:
    print("Escolha uma opção:")
    print("1. Exibir prontuário de um paciente")
    print("2. Adicionar novo paciente")
    print("3. Sair")
    
    opcao = input("Digite o número da opção desejada: ")
    
    if opcao == "1":
        exibir_prontuario()
    elif opcao == "2":
        adicionar_paciente()
    elif opcao == "3":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida! Tente novamente.\n")
