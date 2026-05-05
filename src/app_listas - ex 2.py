import asyncio
from cProfile import label

import flet
from flet import ThemeMode, Text, TextField, OutlinedButton, Column, CrossAxisAlignment, Container, Colors, FontWeight, \
    View, AppBar, FloatingActionButton, Button, ListView, Card, Row, Icon, ListTile, PopupMenuButton, PopupMenuItem, \
    Dropdown, DropdownOption
from flet.controls import page
from flet.controls.border_radius import horizontal
from flet.controls.material.icons import Icons


class Fornecedor:
    def __init__(self, nome, salario, cpf, idade, numero_clientes, regiao_trabalho, ):
        self.nome = nome
        self.salario = salario
        self.cpf = cpf
        self.idade = idade
        self.numero_clientes = numero_clientes
        self.regiao_trabalho = regiao_trabalho


def main(page: flet.Page):
    page.title = "exemplo de listas"
    page.theme_mode = ThemeMode.DARK
    page.window.width = 400
    page.window.height = 700

    lista_dados = []

    # navegar
    def navegar(route):
        asyncio.create_task(
            page.push_route(route)
        )

    def montar_lista_padrao():
        list_view.controls.clear()

        for item in lista_dados:
            print(item)
            list_view.controls.append(
                ListTile(
                    leading=Icon(Icons.CIRCLE),
                    title=item.nome,
                    subtitle=item.salario,
                    trailing=PopupMenuButton(
                        icon=Icons.MORE_VERT,
                        items=[
                            PopupMenuItem("ver detalhes", icon=Icons.REMOVE_RED_EYE, on_click=lambda _, fornecedor=item: ver_detalhes(fornecedor)),
                            PopupMenuItem("excluir", icon=Icons.DELETE)
                        ]
                    )
                )
            )

    def ver_detalhes(fornecedor):
        text_nome.value = fornecedor.nome
        text_salario.value = fornecedor.salario
        text_cpf.value = fornecedor.cpf
        text_idade.value = fornecedor.idade
        text_numero_clientes.value = fornecedor.numero_clientes
        text_regiao_trabalho.value = fornecedor.regiao_trabalho

        navegar("/form_detalhes")

    def excluir(item):
        lista_dados.remove(item)
        montar_lista_padrao()

    def salvar_dados():
        tem_erro = False

        if input_nome.value:
            input_nome.error = None
        else:
            tem_erro = True
            input_nome.error = "campo obrigatório"

        if input_salario.value:
            input_salario.error = None
        else:
            tem_erro = True
            input_salario.error = "campo obrigatório"

        if input_cpf.value:
            input_cpf.error = None
        else:
            tem_erro = True
            input_cpf.error = "campo obrigatório"

        if input_idade.value:
            input_idade.error = None
        else:
            tem_erro = True
            input_idade.error = "campo obrigatório"

        if input_numero_clientes.value:
            input_numero_clientes.error = None
        else:
            tem_erro = True
            input_numero_clientes.error = "campo obrigatório"

        if input_regiao_trabalho.value:
            input_regiao_trabalho.error = None
        else:
            tem_erro = True
            input_regiao_trabalho.error = "campo obrigatório"

        if not tem_erro:
            fornecedor = Fornecedor(
                nome=input_nome.value,
                salario=input_salario.value,
                cpf=input_cpf.value,
                idade=input_idade.value,
                numero_clientes=input_numero_clientes.value,
                regiao_trabalho=input_regiao_trabalho.value,
            )

            lista_dados.append(fornecedor)

            input_nome.value = ""
            input_salario.value = ""
            input_cpf.value = ""
            input_idade.value = ""
            input_numero_clientes.value = ""
            input_regiao_trabalho.value = ""

    # gerenciar as telas (routes)
    def route_change():
        page.views.clear()

        montar_lista_padrao()

        page.views.append(
            View(
                route="/lista_padrao",
                controls=[
                    AppBar(
                        title="fornecedor",
                    ),
                    list_view
                ],
                floating_action_button=FloatingActionButton(
                    icon=Icons.ADD,
                    on_click=lambda: navegar("/form_cadastro"),
                )
            )
        )

        if page.route == "/form_cadastro":
            page.views.append(
                View(
                    route="/form_cadastro",
                    controls=[
                        AppBar(
                            title="cadastro",
                        ),
                        input_nome,
                        input_salario,
                        input_cpf,
                        input_idade,
                        input_numero_clientes,
                        input_regiao_trabalho,
                        btn_salvar
                    ]
                )
            )

        elif page.route == "/form_detalhes":
            page.views.append(
                View(
                    route="/form_detalhes",
                    controls=[
                        AppBar(
                            title="Detalhes",
                        ),
                        text_nome,
                        text_salario,
                        text_cpf,
                        text_idade,
                        text_numero_clientes,
                        text_regiao_trabalho,
                    ]
                )
            )

    # voltar
    async def view_pop(e):
        if e.view is not None:
            page.views.remove(e.view)
            top_view = page.views[-1]
            await page.push_route(top_view.route)

    # Componentes
    input_nome = TextField(label="nome", hint_text="digite o nome")
    input_salario = TextField(label="salario", hint_text="")
    input_cpf = TextField(label="cpf", hint_text="")
    input_idade = Dropdown(
        label="idade",
        editable=True,
        options=[
            DropdownOption("10"),
            DropdownOption("11"),
            DropdownOption("12"),
            DropdownOption("13"),
            DropdownOption("14"),
            DropdownOption("15"),
            DropdownOption("16"),
            DropdownOption("17"),
            DropdownOption("18"),
            DropdownOption("19"),
            DropdownOption("20"),
            DropdownOption("21"),
            DropdownOption("22"),
            DropdownOption("outro"),
        ],
        width=400,
    )
    input_numero_clientes = TextField(label="numero de clientes", hint_text="ex: 20 clientes")
    input_regiao_trabalho = TextField(label="região de trabalho", hint_text="ex: são paulo")

    btn_salvar = Button("salvar", width=400, on_click=lambda: salvar_dados())

    list_view = ListView(height=500)

    text_nome = Text()
    text_salario = Text()
    text_cpf = Text()
    text_idade = Text()
    text_numero_clientes = Text()
    text_regiao_trabalho = Text()

    # eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()


flet.run(main)
