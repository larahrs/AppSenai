import asyncio

import flet
from flet import ThemeMode, View, Colors, Button, Column, Container, Text, TextField, OutlinedButton, FontWeight, \
    CrossAxisAlignment


def main(page: flet.Page):
    # configuracoes
    page.tittle = "exemplo de navegacao"
    page.theme_mode = ThemeMode.LIGHT
    page.window.width = 400
    page.window.height = 700

    # funcoes

    # nagevar
    def navegar(route):
        asyncio.create_task(
            page.push_route(route)
        )

    def salvar_nome(nome):
        text.value = f" {input_nome.value} "
        page.update()

    # componentes
    text = Text()
    input_nome = TextField(label="Nome")
    btn_salvar = OutlinedButton("Salvar", on_click=salvar_nome)



    # gerenciar as telas(routes)

    def route_change():
        page.views.clear()

        page.views.append(
            View(
                route="/",
                controls=[
                    flet.AppBar(
                        title="digite seu nome",
                        bgcolor=Colors.CYAN_700
                    ),
                    Column (
                        [
                            input_nome,
                            text
                        ]
                    ),
                    OutlinedButton("salvar", on_click=lambda: navegar("/segunda_tela"))
                ]
            )
        )
        if page.route == "/segunda_tela":
            page.views.append(
                View(
                    route="/segunda_tela",
                    controls=[
                        flet.AppBar(
                            title=f"bom dia {input_nome.value} ",
                        )
                    ]
                )
            )

    # voltar
    async def view_pop(e):
        if e.view is not None:
            page.views.remove(e.view)
            top_view = page.views[-1]
            await page.push_route(top_view.route)

    # componentes

    # eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()


flet.run(main)
