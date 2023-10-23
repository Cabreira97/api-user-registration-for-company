import requests
import PySimpleGUI as sg


url_usuarios = "http://localhost:3000/usuarios"
url_empresas = "http://localhost:3000/empresas"
url_contratacoes = "http://localhost:3000/contratacoes"


def popup_menu(choices, title):
    layout = [[sg.Button(choice, size=(20, 1))] for choice in choices]
    window = sg.Window(title, layout, keep_on_top=True)

    while True:
        event, _ = window.read()
        window.close()
        return event


def incluir_usuario():
    nome = sg.popup_get_text("Nome:")
    if not nome:
        sg.popup_error("O campo 'Nome' não pode ficar vazio.")
        return

    nivel = popup_menu(['junior', 'pleno', 'senior'], "Escolha o Nível")

    anos_experiencia = sg.popup_get_text("Anos de Experiência:")
    if not anos_experiencia:
        sg.popup_error("O campo 'Anos de Experiência' não pode ficar vazio.")
        return

    salario = sg.popup_get_text("Salário:")
    if not salario:
        sg.popup_error("O campo 'Salário' não pode ficar vazio.")
        return

    area = sg.popup_get_text("Área de Atuação:")
    if not area:
        sg.popup_error("O campo 'Área de Atuação' não pode ficar vazio.")
        return

    linguagem = sg.popup_get_text("Linguagem de Programação:")
    if not linguagem:
        sg.popup_error(
            "O campo 'Linguagem de Programação' não pode ficar vazio.")
        return

    cargo_pretendido = sg.popup_get_text("Cargo Pretendido:")
    if not cargo_pretendido:
        sg.popup_error("O campo 'Cargo Pretendido' não pode ficar vazio.")
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
        sg.popup(f"Usuário cadastrado com o código: {codigo}")
    else:
        sg.popup_error("Erro ao cadastrar usuário")


def listar_usuarios():
    response = requests.get(url_usuarios)

    if response.status_code == 200:
        usuarios = response.json()
        dados_tabela = [[usuario['id'], usuario['nome'], usuario['nivel'], usuario['anos_experiencia'],
                         usuario['salario'], usuario['area'], usuario['linguagem'], usuario['cargo_pretendido']] for usuario in usuarios]
        layout_tabela = [
            [sg.Table(dados_tabela, headings=['ID', 'Nome', 'Nível', 'Anos de Exp.', 'Salário', 'Área',
                      'Linguagem', 'Cargo Pretendido'], auto_size_columns=False, justification='left')]
        ]
        window_tabela = sg.Window("Listagem de Usuários", layout_tabela)
        while True:
            event, _ = window_tabela.read()
            if event == sg.WIN_CLOSED:
                break
        window_tabela.close()
    else:
        sg.popup_error("Erro ao listar usuários")


def atualizar_usuario():
    id_usuario = sg.popup_get_text("ID do Usuário:")
    nome = sg.popup_get_text("Nome:")
    nivel = sg.popup_get_text("Nível (junior, pleno, senior):")
    anos_experiencia = sg.popup_get_text("Anos de Experiência:")
    salario = sg.popup_get_text("Salário:")
    area = sg.popup_get_text("Área de Atuação:")
    linguagem = sg.popup_get_text("Linguagem de Programação:")
    cargo_pretendido = sg.popup_get_text("Cargo Pretendido:")

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
        sg.popup(f"Usuário com ID {id_usuario} atualizado com sucesso")
    else:
        sg.popup_error("Erro ao atualizar usuário")


def excluir_usuario():
    id_usuario = sg.popup_get_text("ID do Usuário:")

    response = requests.delete(f"{url_usuarios}/{id_usuario}")

    if response.status_code == 200:
        sg.popup(f"Usuário com ID {id_usuario} excluído com sucesso")
    else:
        sg.popup_error("Erro ao excluir usuário")


def filtrar_usuarios(nivel):
    response = requests.get(url_usuarios)
    if response.status_code == 200:
        usuarios = response.json()

        usuarios_filtrados = [
            usuario for usuario in usuarios if usuario['nivel'] == nivel]

        if usuarios_filtrados:
            dados_tabela = [[usuario['id'], usuario['nome'], usuario['nivel'], usuario['anos_experiencia'], usuario['salario'],
                             usuario['area'], usuario['linguagem'], usuario['cargo_pretendido']] for usuario in usuarios_filtrados]
            layout_tabela = [
                [sg.Table(dados_tabela, headings=['ID', 'Nome', 'Nível', 'Anos de Exp.', 'Salário', 'Área',
                          'Linguagem', 'Cargo Pretendido'], auto_size_columns=False, justification='left')]
            ]
            window_tabela = sg.Window(
                f"Listagem de Usuários - Nível {nivel}", layout_tabela)
            while True:
                event, _ = window_tabela.read()
                if event == sg.WIN_CLOSED:
                    break
            window_tabela.close()
        else:
            sg.popup(f'Não há usuários no nível {nivel}')
    else:
        sg.popup_error("Erro ao listar usuários")


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
            layout_tabela = [
                [sg.Table(values=dados_tabela, headings=['Nível', 'Total de Usuários',
                          'Média Salarial'], auto_size_columns=True, justification='left')]
            ]
            window_tabela = sg.Window("Agrupamento de Usuários", layout_tabela)
            event, _ = window_tabela.read()
            window_tabela.close()
        else:
            sg.popup("Não há usuários para agrupar")
    else:
        sg.popup_error("Erro ao listar usuários")


def filtrar_usuarios_por_nome(nome):
    response = requests.get(url_usuarios)
    if response.status_code == 200:
        usuarios = response.json()

        usuarios_filtrados = [
            usuario for usuario in usuarios if nome.lower() in usuario['nome'].lower()]

        if usuarios_filtrados:
            dados_tabela = [[usuario['id'], usuario['nome'], usuario['nivel'], usuario['anos_experiencia'], usuario['salario'],
                             usuario['area'], usuario['linguagem'], usuario['cargo_pretendido']] for usuario in usuarios_filtrados]
            layout_tabela = [
                [sg.Table(dados_tabela, headings=['ID', 'Nome', 'Nível', 'Anos de Exp.', 'Salário', 'Área',
                          'Linguagem', 'Cargo Pretendido'], auto_size_columns=False, justification='left')]
            ]
            window_tabela = sg.Window(
                f"Listagem de Usuários - Nome '{nome}'", layout_tabela)
            while True:
                event, _ = window_tabela.read()
                if event == sg.WIN_CLOSED:
                    break
            window_tabela.close()
        else:
            sg.popup(f'Não há usuários com o nome "{nome}"')
    else:
        sg.popup_error("Erro ao listar usuários")


def incluir_empresa():
    nome = sg.popup_get_text("Nome da Empresa:")
    cnpj = sg.popup_get_text("CNPJ:")
    tamanho = sg.popup_get_text("Tamanho da Empresa (pequena, media, grande):")
    descricao = sg.popup_get_text("Descrição:")
    razao_social = sg.popup_get_text("Razão Social:")

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
        sg.popup(f"Empresa cadastrada com o código: {codigo}")
    else:
        sg.popup_error("Erro ao cadastrar empresa")


def listar_empresas():
    response = requests.get(url_empresas)

    if response.status_code == 200:
        empresas = response.json()
        dados_tabela = [[empresa['id'], empresa['nome'], empresa['cnpj'], empresa['tamanho'],
                         empresa['descricao'], empresa['razao_social']] for empresa in empresas]
        layout_tabela = [
            [sg.Table(dados_tabela, headings=['ID', 'Nome da Empresa', 'CNPJ', 'Tamanho',
                      'Descrição', 'Razão Social'], auto_size_columns=False, justification='left')]
        ]
        window_tabela = sg.Window("Listagem de Empresas", layout_tabela)
        while True:
            event, _ = window_tabela.read()

            if event == sg.WIN_CLOSED:
                break
        window_tabela.close()
    else:
        sg.popup_error("Erro ao listar empresas")


def atualizar_empresa():
    id_empresa = sg.popup_get_text("ID da Empresa:")
    nome = sg.popup_get_text("Nome da Empresa:")
    cnpj = sg.popup_get_text("CNPJ:")
    tamanho = sg.popup_get_text("Tamanho da Empresa (pequena, media, grande):")
    descricao = sg.popup_get_text("Descrição:")
    razao_social = sg.popup_get_text("Razão Social:")

    payload = {
        "nome": nome,
        "cnpj": cnpj,
        "tamanho": tamanho,
        "descricao": descricao,
        "razao_social": razao_social
    }

    response = requests.put(f"{url_empresas}/{id_empresa}", json=payload)

    if response.status_code == 200:
        sg.popup(f"Empresa com ID {id_empresa} atualizada com sucesso")
    else:
        sg.popup_error("Erro ao atualizar empresa")


def excluir_empresa():
    id_empresa = sg.popup_get_text("ID da Empresa:")

    response = requests.delete(f"{url_empresas}/{id_empresa}")

    if response.status_code == 200:
        sg.popup(f"Empresa com ID {id_empresa} excluída com sucesso")
    else:
        sg.popup_error("Erro ao excluir empresa")


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

        layout = [
            [sg.Text("Regime (CLT ou PJ):"), sg.InputText(
                size=(10, 1), key='-REGIME-')],
            [sg.Text("Escolha o Usuário:"), sg.Table(values=lista_usuarios, headings=['ID', 'Nome'],
                                                     auto_size_columns=False, col_widths=[5, 20], justification='left', num_rows=5, key='-USUARIO-')],
            [sg.Text("Escolha a Empresa:"), sg.Table(values=lista_empresas, headings=['ID', 'Nome'],
                                                     auto_size_columns=False, col_widths=[5, 20], justification='left', num_rows=5, key='-EMPRESA-')],
            [sg.Button("Cadastrar")]
        ]

        window = sg.Window("Cadastro de Contratação", layout)

        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED:
                break
            elif event == "Cadastrar":
                regime = values['-REGIME-']
                usuario_id = int(values['-USUARIO-'][0])
                empresa_id = int(values['-EMPRESA-'][0])

                payload = {
                    "regime": regime,
                    "usuario_id": usuario_id,
                    "empresa_id": empresa_id
                }

                response = requests.post(url_contratacoes, json=payload)

                if response.status_code == 201:
                    contratacao_cadastrada = response.json()
                    codigo = contratacao_cadastrada["id"]
                    sg.popup(f"Contratação cadastrada com o código: {codigo}")
                    break
                else:
                    sg.popup_error("Erro ao cadastrar contratação")
                    break

        window.close()

    else:
        sg.popup_error("Erro ao obter dados de usuários ou empresas")


def listar_contratacoes():
    response = requests.get(url_contratacoes)

    if response.status_code == 200:
        contratacoes = response.json()

        dados_tabela = [[
            contratacao['id'],
            contratacao['regime'],
            contratacao['usuario_id'],
            contratacao['empresa_id']
        ] for contratacao in contratacoes]

        layout_tabela = [
            [sg.Table(dados_tabela,
                      headings=['ID', 'Regime', 'ID Usuário', 'ID Empresa'],
                      auto_size_columns=False,
                      justification='left')]
        ]

        window_tabela = sg.Window("Listagem de Contratações", layout_tabela)
        while True:
            event, _ = window_tabela.read()
            if event == sg.WIN_CLOSED:
                break
        window_tabela.close()
    else:
        sg.popup_error("Erro ao listar contratações")


def atualizar_contratacao():
    id_contratacao = sg.popup_get_text("ID da Contratação:")
    regime = sg.popup_get_text("Regime (CLT ou PJ):")
    usuario_id = sg.popup_get_text("ID do Usuário:")
    empresa_id = sg.popup_get_text("ID da Empresa:")

    payload = {
        "regime": regime,
        "usuario_id": usuario_id,
        "empresa_id": empresa_id
    }

    response = requests.put(
        f"{url_contratacoes}/{id_contratacao}", json=payload)

    if response.status_code == 200:
        sg.popup(f"Contratação com ID {id_contratacao} atualizada com sucesso")
    else:
        sg.popup_error("Erro ao atualizar contratação")


def excluir_contratacao():
    id_contratacao = sg.popup_get_text("ID da Contratação:")

    response = requests.delete(f"{url_contratacoes}/{id_contratacao}")

    if response.status_code == 200:
        sg.popup(f"Contratação com ID {id_contratacao} excluída com sucesso")
    else:
        sg.popup_error("Erro ao excluir contratação")


layout_menu = [
    [sg.Text("Menu de Opções")],
    [sg.Button("Usuários"), sg.Button("Empresas"), sg.Button(
        "Contratações"), sg.Button("Créditos"), sg.Button("Sair")]
]


window_menu = sg.Window("Cadastro de Usuários e Empresas", layout_menu)

while True:
    event, _ = window_menu.read()

    if event == sg.WIN_CLOSED or event == "Sair":
        break
    elif event == "Créditos":
        sg.popup("Desenvolvido por Thiago Vieira", title="Créditos")

    elif event == "Usuários":
        layout_usuarios = [
            [sg.Button("Incluir Usuário", size=(20, 1)), sg.Button(
                "Listar Usuários", size=(20, 1)), sg.Button("Atualizar Usuário", size=(20, 1))],
            [sg.Button("Excluir Usuário", size=(20, 1)), sg.Button(
                "Filtrar Usuários", size=(20, 1)), sg.Button("Agrupar Usuários", size=(20, 1))],
            [sg.Button("Filtrar Usuários por Nome", size=(20, 1))]
        ]
        window_usuarios = sg.Window("CRUD de Usuários", layout_usuarios)

        while True:
            event_usuarios, _ = window_usuarios.read()

            if event_usuarios == sg.WIN_CLOSED:
                break
            elif event_usuarios == "Incluir Usuário":
                incluir_usuario()
            elif event_usuarios == "Listar Usuários":
                listar_usuarios()
            elif event_usuarios == "Atualizar Usuário":
                atualizar_usuario()
            elif event_usuarios == "Excluir Usuário":
                excluir_usuario()
            elif event_usuarios == "Filtrar Usuários":
                nivel = sg.popup_get_text(
                    "Filtrar por Nível (Junior, Pleno, Senior):")
                if nivel in ['junior', 'pleno', 'senior']:
                    filtrar_usuarios(nivel)
                else:
                    sg.popup_error(
                        "Nível inválido. Use 'Junior', 'Pleno' ou 'Senior'")
            elif event_usuarios == "Agrupar Usuários":
                agrupar_usuarios()
            elif event_usuarios == "Filtrar Usuários por Nome":
                nome = sg.popup_get_text("Filtrar por Nome:")
                filtrar_usuarios_por_nome(nome)

        window_usuarios.close()

    elif event == "Empresas":
        layout_empresas = [
            [sg.Button("Incluir Empresa"), sg.Button("Listar Empresas"), sg.Button(
                "Atualizar Empresa"), sg.Button("Excluir Empresa")],
        ]
        window_empresas = sg.Window("CRUD de Empresas", layout_empresas)

        while True:
            event_empresas, _ = window_empresas.read()

            if event_empresas == sg.WIN_CLOSED:
                break
            elif event_empresas == "Incluir Empresa":
                incluir_empresa()
            elif event_empresas == "Listar Empresas":
                listar_empresas()
            elif event_empresas == "Atualizar Empresa":
                atualizar_empresa()
            elif event_empresas == "Excluir Empresa":
                excluir_empresa()

        window_empresas.close()

    elif event == "Contratações":
        layout_contratacoes = [
            [sg.Button("Incluir Contratação"), sg.Button("Listar Contratações"), sg.Button(
                "Atualizar Contratação"), sg.Button("Excluir Contratação")],
        ]
        window_contratacoes = sg.Window(
            "CRUD de Contratações", layout_contratacoes)

        while True:
            event_contratacoes, _ = window_contratacoes.read()
            if event_contratacoes == sg.WIN_CLOSED:
                break
            elif event_contratacoes == "Incluir Contratação":
                incluir_contratacao()
            elif event_contratacoes == "Listar Contratações":
                listar_contratacoes()
            elif event_contratacoes == "Atualizar Contratação":
                atualizar_contratacao()
            elif event_contratacoes == "Excluir Contratação":
                excluir_contratacao()

        window_contratacoes.close()

window_menu.close()
