eventos = {}

opcao = ""
#Inicio do nosso CRUD
while opcao != "S":
    print("_-_-"*30)
    print("[C] CRIAR EVENTO")
    print("[E] EXCLUIR EVENTO")
    print("[V] VERIFICAR OS EVENTOS")
    print("[S] SAIR DO EDITOR")
    print("[R] EDITAR EVENTOS")
    print("_-_-"*30)

    opcao = input("Escolha uma opção: ").upper()

    if opcao == "C": #>C<RUD

        nome = (input("Nome do evento: ")).lower()
        eventos[nome] = {
        "tipo": input("Tipo do evento: "),
        "Data": input("Data do evento(xx/yy/zz)"),
        "Hora": input("Hora do evento(xx:yy): " ),
        "local": input("Local do evento: "),
        "orcamento": float(input("Orçamento do evento: "))}




    elif opcao == "E" : #CRU>D<
     nome= input("Qual evento desaja excluir? ").lower()#padronizar

     if nome in eventos:
         del eventos[nome]
         print("deletado com sucesso!")
     else:
         print("**ERRO** Evento não encontrado! ")

    elif opcao == "V": #C>R<UD
        if len(eventos) == 0:
            print("Sinto muito! Nenhum evento encontrado")

        else:

            for nome in eventos: #contador
                print("Eventos:", [nome])
                print("--"*10)
                print("Data")
                print(eventos[nome]["Data"])
                print("--" * 10)
                print("hora")
                print(eventos[nome]["Hora"])
                print("--" * 10)
                print("orçamento")
                print(eventos[nome]["orcamento"])
                print("--" * 10)
                print("Local")
                print(eventos[nome]["local"])
                print("--" * 10)

    elif opcao == "R":
        nome = input("Qual evento deseja editar? ")
        if nome in eventos:
            editar = input("Digite oque deseja aditar: ")
            if editar in eventos[nome]:
                eventos[nome][editar] = input("Novo valor: ")


    elif opcao == "S":
        print("Até mais!")

    else:
        print("Opção inválida, tente novamente")