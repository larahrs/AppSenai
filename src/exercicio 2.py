import asyncio
from cProfile import label

import flet
from flet import ThemeMode, Text, TextField, OutlinedButton, Column, CrossAxisAlignment, Container, Colors, FontWeight, \
    View, AppBar
from flet.controls import page
from flet.controls.border_radius import horizontal


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

    def salvar_nome(nome):
        text.value = f"{input_nome.value}"
        page.update()

    def salvar_cpf(cpf):
        text.value = f"{input_cpf.value}"
        page.update()

    def salvar_email(email):
        text.value = f"{input_email.value}"
        page.update()

    def salvar_salario(salario):
        text.value = f"{input_salario.value}"
        page.update()

    text = Text()
    input_nome = TextField(label="nome")
    input_cpf = TextField(label="CPF")
    input_email = TextField(label="email")
    input_salario = TextField(label="salario")

    # Gerenciar as telas (routes)
    def route_change():
        page.views.clear()
        page.views.append(
            View(
                route="/",
                controls=[
                    AppBar(
                        title="funcionário",
                        bgcolor=Colors.CYAN_700
                    ),
                    Text("digite seu nome:"),
                    input_nome,

                    Text("digite seu CPF:"),
                    input_cpf,

                    Text("digite seu Email:"),
                    input_email,

                    Text("digite seu salário:"),
                    input_salario,
                    OutlinedButton("Salvar", on_click=lambda: navegar("/segunda_tela"))
                ]
            )
        )
        if page.route == "/segunda_tela":
            page.views.append(
                View(
                    route="/segunda_tela",
                    controls=[
                        AppBar(
                            title="funcionários",
                            bgcolor=Colors.CYAN_700
                        ),
                        Text(f"nome: {input_nome.value}"),
                        Text(f"CPF: {input_cpf.value}"),
                        Text(f"email: {input_email.value}"),
                        Text(f"salário: {input_salario.value}")
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

    # Eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()


flet.run(main)