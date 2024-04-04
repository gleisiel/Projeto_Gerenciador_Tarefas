
tarefas = []
def add_tarefa(tarefa):
    tarefas.append({"tarefa": tarefa, "concluida": false})
    print("Tarefa adicionada: ", tarefa)

def remove_tarefa(tarefa):
    for t in tarefa:
        if t["tarefa"] == tarefa:
            tarefas.remove(t)
            print("Tarefa removida: ", tarefa)
            return
        print ("Tarefa nao encontrada.")

def concluir_tarefa(tarefa):
    for t in tarefas:
        if t["tarefa"] == tarefa:
            t["concluida"]= True
            print("\n-->Tarefa concluida: ", tarefa)
            return
    print("Tarefa nao encontrada")

def list_tarefas():
    if tarefas:
        print("\n--> Lista de tarefas <--")
        for t in tarefas:
            status = "Concluida" if t["concluida"] else "Pendente"
            print(f"{t['tarefa']} - ({status})")
    else:
        print("\nSem tarefas no momento.")

def clear_list ():
    tarefas.clear()
    print("Todas as tarefas foram removidas.")

while True:
    print("\n--> Gerenciador de tarefas <--")
    print("1-Adicionar Tarefa")
    print("2-Concluir Tarefa")
    print("3-Remover Tarefa")
    print("4-Exibir Tarefa")
    print("5-Limpar lista de Tarefa")
    print("0-Sair")

    opcao= input("\nDigite a opcao desejada-->")
    if opcao == "0":
        print("\n... Encerrando o gerenciador de tarefas")
        break

    elif opcao == "1":
        tarefa_name = input("Digite o nome da tarefa ==> ")
        add_tarefa(tarefa_name)

    elif opcao == "2":
        tarefa_name = input("Digite o nome da tarefa  que deseja concluir ==> ")
        concluir_tarefa(tarefa_name)


    elif opcao == "3":
        tarefa_name = input("Digite o nome da tarefa que gostaria de remover ==> ")
        remove_tarefa(tarefa_name)

    elif opcao == "4":
        tarefa_name = input("Exiba a lista ==> ")
        list_tarefas(tarefa_name)

    elif opcao == "5":
        tarefa_name = input("Limpar lista de tarefa==> ")
        clear_list(tarefa_name)

    

#https://youtu.be/63xCY_BIOA8?si=GJkuLjdbnR3PE_rc
