import requests
from tabulate import tabulate
url_usuarios = "http://localhost:3000/usuarios"
url_contratacoes = "http://localhost:3000/contratacoes"
url_empresas = "http://localhost:3000/empresas"


def incluir_usuario():
    nome = input("Nome: ")
    if not nome:
        print("O campo 'Nome' não pode ficar vazio.")
        return

    nivel = input("Escolha o Nível (junior, pleno, senior): ")
    if nivel not in ['junior', 'pleno', 'senior']:
        print("Nível inválido. Use 'junior', 'pleno' ou 'senior'.")
        return

    anos_experiencia = input("Anos de Experiência: ")
    if not anos_experiencia.isdigit():
        print("O campo 'Anos de Experiência' deve ser um número inteiro.")
        return

    salario = input("Salário: ")
    if not salario.replace('.', '', 1).isdigit():
        print("O campo 'Salário' deve ser um número.")
        return

    area = input("Área de Atuação: ")
    if not area:
        print("O campo 'Área de Atuação' não pode ficar vazio.")
        return

    linguagem = input("Linguagem de Programação: ")
    if not linguagem:
        print("O campo 'Linguagem de Programação' não pode ficar vazio.")
        return

    cargo_pretendido = input("Cargo Pretendido: ")
    if not cargo_pretendido:
        print("O campo 'Cargo Pretendido' não pode ficar vazio.")
        return

    payload = {
        "nome": nome,
        "nivel": nivel,
        "anos_experiencia": int(anos_experiencia),
        "salario": float(salario),
        "area": area,
        "linguagem": linguagem,
        "cargo_pretendido": cargo_pretendido
    }

    response = requests.post(url_usuarios, json=payload)

    if response.status_code == 201:
        usuario_cadastrado = response.json()
        codigo = usuario_cadastrado["id"]
        print(f"Usuário cadastrado com o código: {codigo}")
    else:
        print("Erro ao cadastrar usuário")


def listar_usuarios():
    response = requests.get(url_usuarios)

    if response.status_code == 200:
        usuarios = response.json()
        dados_tabela = [[usuario['id'], usuario['nome'], usuario['nivel'], usuario['anos_experiencia'], usuario['salario'],
                         usuario['area'], usuario['linguagem'], usuario['cargo_pretendido']] for usuario in usuarios]
        print(tabulate(dados_tabela, headers=['ID', 'Nome', 'Nível', 'Anos de Exp.', 'Salário', 'Área',
                                              'Linguagem', 'Cargo Pretendido'], tablefmt='pretty'))
    else:
        print("Erro ao listar usuários")


def atualizar_usuario():
    id_usuario = input("ID do Usuário:")
    nome = input("Nome:")
    nivel = input("Nível (junior, pleno, senior):")
    anos_experiencia = input("Anos de Experiência:")
    salario = input("Salário:")
    area = input("Área de Atuação:")
    linguagem = input("Linguagem de Programação:")
    cargo_pretendido = input("Cargo Pretendido:")

    payload = {
        "nome": nome,
        "nivel": nivel,
        "anos_experiencia": int(anos_experiencia),
        "salario": float(salario),
        "area": area,
        "linguagem": linguagem,
        "cargo_pretendido": cargo_pretendido
    }

    response = requests.put(f"{url_usuarios}/{id_usuario}", json=payload)

    if response.status_code == 200:
        print(f"Usuário com ID {id_usuario} atualizado com sucesso")
    else:
        print("Erro ao atualizar usuário")


def excluir_usuario():
    id_usuario = input("ID do Usuário:")

    response = requests.delete(f"{url_usuarios}/{id_usuario}")

    if response.status_code == 200:
        print(f"Usuário com ID {id_usuario} excluído com sucesso")
    else:
        print("Erro ao excluir usuário")


def filtrar_usuarios(nivel):
    response = requests.get(url_usuarios)
    if response.status_code == 200:
        usuarios = response.json()

        usuarios_filtrados = [
            usuario for usuario in usuarios if usuario['nivel'] == nivel]

        if usuarios_filtrados:
            dados_tabela = [[usuario['id'], usuario['nome'], usuario['nivel'], usuario['anos_experiencia'], usuario['salario'],
                             usuario['area'], usuario['linguagem'], usuario['cargo_pretendido']] for usuario in usuarios_filtrados]

            print(tabulate(dados_tabela, headers=['ID', 'Nome', 'Nível', 'Anos de Exp.', 'Salário', 'Área',
                                                  'Linguagem', 'Cargo Pretendido'], tablefmt='pretty'))
        else:
            print(f'Não há usuários no nível {nivel}')
    else:
        print("Erro ao listar usuários")


def agrupar_usuarios():
    response = requests.get(url_usuarios)
    if response.status_code == 200:
        usuarios = response.json()
        grupos = {'junior': [], 'pleno': [], 'senior': []}

        for usuario in usuarios:
            grupos[usuario['nivel']].append(usuario)

        dados_tabela = []
        for nivel, usuarios in grupos.items():
            if usuarios:
                total_salarios = sum(usuario['salario']
                                     for usuario in usuarios)
                media_salarios = total_salarios / len(usuarios)
                dados_tabela.append(
                    [f"Nível {nivel.capitalize()}", len(usuarios), media_salarios])

        if dados_tabela:
            print(tabulate(dados_tabela, headers=['Nível', 'Total de Usuários',
                                                  'Média Salarial'], tablefmt='pretty'))
        else:
            print("Não há usuários para agrupar")
    else:
        print("Erro ao listar usuários")


def filtrar_usuarios_por_nome(nome):
    response = requests.get(url_usuarios)
    if response.status_code == 200:
        usuarios = response.json()

        usuarios_filtrados = [
            usuario for usuario in usuarios if nome.lower() in usuario['nome'].lower()]

        if usuarios_filtrados:
            dados_tabela = [[usuario['id'], usuario['nome'], usuario['nivel'], usuario['anos_experiencia'], usuario['salario'],
                             usuario['area'], usuario['linguagem'], usuario['cargo_pretendido']] for usuario in usuarios_filtrados]

            print(tabulate(dados_tabela, headers=['ID', 'Nome', 'Nível', 'Anos de Exp.', 'Salário', 'Área',
                                                  'Linguagem', 'Cargo Pretendido'], tablefmt='pretty'))

        else:
            print(f'Não há usuários com o nome "{nome}"')
    else:
        print("Erro ao listar usuários")

# ------------


def incluir_empresa():
    nome = input("Nome da Empresa: ")
    cnpj = input("CNPJ: ")
    tamanho = input("Tamanho da Empresa (pequena, media, grande): ")
    descricao = input("Descrição: ")
    razao_social = input("Razão Social: ")

    payload = {
        "nome": nome,
        "cnpj": cnpj,
        "tamanho": tamanho,
        "descricao": descricao,
        "razao_social": razao_social
    }

    response = requests.post(url_empresas, json=payload)

    if response.status_code == 201:
        empresa_cadastrada = response.json()
        codigo = empresa_cadastrada["id"]
        print(f"Empresa cadastrada com o código: {codigo}")
    else:
        print("Erro ao cadastrar empresa")


def listar_empresas():
    response = requests.get(url_empresas)

    if response.status_code == 200:
        empresas = response.json()
        dados_tabela = [[empresa['id'], empresa['nome'], empresa['cnpj'], empresa['tamanho'], empresa['descricao'],
                         empresa['razao_social']] for empresa in empresas]
        print(tabulate(dados_tabela, headers=[
              'ID', 'Nome', 'CNPJ', 'Tamanho', 'Descrição', 'Razão Social'], tablefmt='pretty'))
    else:
        print("Erro ao listar empresas")


def atualizar_empresa():
    id_empresa = input("ID da Empresa:")
    nome = input("Nome da Empresa:")
    cnpj = input("CNPJ:")
    tamanho = input("Tamanho da Empresa (pequena, media, grande):")
    descricao = input("Descrição:")
    razao_social = input("Razão Social:")

    payload = {
        "nome": nome,
        "cnpj": cnpj,
        "tamanho": tamanho,
        "descricao": descricao,
        "razao_social": razao_social
    }

    response = requests.put(f"{url_empresas}/{id_empresa}", json=payload)

    if response.status_code == 200:
        print(f"Empresa com ID {id_empresa} atualizada com sucesso")
    else:
        print("Erro ao atualizar empresa")


def excluir_empresa():
    id_empresa = input("ID da Empresa:")

    response = requests.delete(f"{url_empresas}/{id_empresa}")

    if response.status_code == 200:
        print(f"Empresa com ID {id_empresa} excluída com sucesso")
    else:
        print("Erro ao excluir empresa")


def incluir_contratacao():
    usuarios_response = requests.get(url_usuarios)
    empresas_response = requests.get(url_empresas)

    if usuarios_response.status_code == 200 and empresas_response.status_code == 200:
        usuarios = usuarios_response.json()
        empresas = empresas_response.json()

        lista_usuarios = [[f"{usuario['id']}", usuario['nome']]
                          for usuario in usuarios]
        lista_empresas = [[f"{empresa['id']}", empresa['nome']]
                          for empresa in empresas]

        regime = input("Regime (CLT ou PJ): ")
        usuario_id = (input("Escolha o Usuário (ID): "))
        empresa_id = (input("Escolha a Empresa (ID): "))

        payload = {
            "regime": regime,
            "usuario_id": usuario_id,
            "empresa_id": empresa_id
        }

        response = requests.post(url_contratacoes, json=payload)

        if response.status_code == 201:
            contratacao_cadastrada = response.json()
            codigo = contratacao_cadastrada["id"]
            print(f"Contratação cadastrada com o código: {codigo}")
        else:
            print("Erro ao cadastrar contratação")


def listar_contratacoes():
    response = requests.get(url_contratacoes)

    if response.status_code == 200:
        contratacoes = response.json()
        dados_tabela = [[contratacao['id'], contratacao['regime'], contratacao['usuario_id'],
                         contratacao['empresa_id']] for contratacao in contratacoes]
        print(tabulate(dados_tabela, headers=[
              'ID', 'Regime', 'ID Usuário', 'ID Empresa'], tablefmt='pretty'))
    else:
        print("Erro ao listar contratações")


def atualizar_contratacao():
    id_contratacao = input("ID da Contratação:")
    regime = input("Regime (CLT ou PJ):")
    usuario_id = input("ID do Usuário:")
    empresa_id = input("ID da Empresa:")

    payload = {
        "regime": regime,
        "usuario_id": usuario_id,
        "empresa_id": empresa_id
    }

    response = requests.put(
        f"{url_contratacoes}/{id_contratacao}", json=payload)

    if response.status_code == 200:
        print(f"Contratação com ID {id_contratacao} atualizada com sucesso")
    else:
        print("Erro ao atualizar contratação")


def excluir_contratacao():
    id_contratacao = input("ID da Contratação:")

    response = requests.delete(f"{url_contratacoes}/{id_contratacao}")

    if response.status_code == 200:
        print(f"Contratação com ID {id_contratacao} excluída com sucesso")
    else:
        print("Erro ao excluir contratação")


def menu():
    while True:
        print("\nMenu de Opções")
        print("1 - Usuários")
        print("2 - Empresas")
        print("3 - Contratações")
        print("4 - Créditos")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '0':
            break
        elif opcao == '4':
            print("Desenvolvido por Thiago Vieira")
        elif opcao == '1':
            menu_usuarios()
        elif opcao == '2':
            menu_empresas()
        elif opcao == '3':
            menu_contratacoes()

    print("Até mais!")


def menu_usuarios():
    print("\nMenu de Usuários")
    print("1 - Incluir Usuário")
    print("2 - Listar Usuários")
    print("3 - Atualizar Usuário")
    print("4 - Excluir Usuário")
    print("5 - Filtrar Usuários")
    print("6 - Agrupar Usuários")
    print("7 - Filtrar Usuários por Nome")

    opcao_usuario = input("Escolha uma opção para Usuários: ")
    if opcao_usuario == '1':
        incluir_usuario()
    elif opcao_usuario == '2':
        listar_usuarios()
    elif opcao_usuario == '3':
        atualizar_usuario()
    elif opcao_usuario == '4':
        excluir_usuario()
    elif opcao_usuario == '5':
        nivel = input("Filtrar por Nível (Junior, Pleno, Senior): ")
        filtrar_usuarios(nivel)
    elif opcao_usuario == '6':
        agrupar_usuarios()
    elif opcao_usuario == '7':
        nome = input("Filtrar por Nome: ")
        filtrar_usuarios_por_nome(nome)


def menu_empresas():
    print("\nMenu de Empresas")
    print("1 - Incluir Empresa")
    print("2 - Listar Empresas")
    print("3 - Atualizar Empresa")
    print("4 - Excluir Empresa")

    opcao_empresa = input("Escolha uma opção para Empresas: ")
    if opcao_empresa == '1':
        incluir_empresa()
    elif opcao_empresa == '2':
        listar_empresas()
    elif opcao_empresa == '3':
        atualizar_empresa()
    elif opcao_empresa == '4':
        excluir_empresa()


def menu_contratacoes():
    print("\nMenu de Contratações")
    print("1 - Incluir Contratação")
    print("2 - Listar Contratações")
    print("3 - Atualizar Contratação")
    print("4 - Excluir Contratação")

    opcao_contratacao = input("Escolha uma opção para Contratações: ")
    if opcao_contratacao == '1':
        incluir_contratacao()
    elif opcao_contratacao == '2':
        listar_contratacoes()
    elif opcao_contratacao == '3':
        atualizar_contratacao()
    elif opcao_contratacao == '4':
        excluir_contratacao()


menu()
