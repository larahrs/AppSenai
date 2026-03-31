import asyncio
import flet
from flet import ThemeMode, Text, TextField, OutlinedButton, Column, CrossAxisAlignment, Container, Colors, FontWeight, \
    View, AppBar


def main(page: flet.Page):
    page.title = "Primeiro APP"
    page.theme_mode = ThemeMode.DARK
    page.window.width = 400
    page.window.height = 700


    # Navegar
    def navegar(route):
        asyncio.create_task(
            page.push_route(route)
        )

    def salvar_funcionario():
        text_nome.value = input_nome.value
        text_cpf.value = input_cpf.value
        text_salario.value = input_salario.value
        text_numero_clientes.value = input_numero_clientes.value
        text_regiao_trabalho.value = input_regiao_trabalho.value

        tem_erro = False

        if input_nome.value:
            input_nome.error = None
        else:
            tem_erro = True
            input_nome.error = "campo obrigatório"

        if input_cpf.value:
            input_cpf.error = None
        else:
            tem_erro = True
            input_cpf.error = "campo obrigatório"

        if input_salario.value:
            input_salario.error = None
        else:
            tem_erro = True
            input_salario.error = "campo obrigatório"

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
            input_nome.value = ""
            input_cpf.value = ""
            input_salario.value = ""
            input_numero_clientes.value = ""
            input_regiao_trabalho.value = ""
            navegar("/segunda_tela")

    # Gerenciar as telas (routes)
    def route_change():
        page.views.clear()
        page.views.append(
            View(
                route="/",
                controls=[
                    AppBar(
                        title="fornecedor",
                        bgcolor=Colors.BLUE_900
                    ),
                    Text("digite seu nome:"),
                    input_nome,

                    Text("digite seu CPF:"),
                    input_cpf,

                    Text("digite seu salario:"),
                    input_salario,

                    Text("digite seu numero de clientes:"),
                    input_numero_clientes,

                    Text("digite sua regiao de trabalho:"),
                    input_regiao_trabalho,
                    OutlinedButton("salvar", on_click=salvar_funcionario)
                ]
            )
        )
        if page.route == "/segunda_tela":
            page.views.append(
                View(
                    route="/segunda_tela",
                    controls=[
                        AppBar(
                            title="fornecedor",
                            bgcolor=Colors.BLUE_900
                        ),
                        text_nome,
                        text_cpf,
                        text_salario,
                        text_numero_clientes,
                        text_regiao_trabalho,
                    ]
                )
            )

    # Voltar
    async def view_pop(e):
        if e.view is not None:
            page.views.remove(e.view)
            top_view = page.views[-1]
            await page.push_route(top_view.route)

    # Componentes
    text = Text()
    input_nome = TextField(label="nome")
    input_cpf = TextField(label="CPF")
    input_salario = TextField(label="salario")
    input_numero_clientes = TextField(label="numero de clientes")
    input_regiao_trabalho = TextField(label="regiao de trabalho")
    text_nome = TextField(label="nome")
    text_cpf = TextField(label="cpf")
    text_salario = TextField(label="salario")
    text_numero_clientes = TextField(label="numero de clientes")
    text_regiao_trabalho = TextField(label="regiao de trabalho")

    # Eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()


flet.run(main)