import asyncio

import flet
from flet import ThemeMode, View, Colors, Button


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

    # gerenciar as telas(routes)
    def route_change():
        page.views.clear()

        page.views.append(
            View(
                route="/",
                controls=[
                    flet.AppBar(
                        title="primeira pagina",
                        bgcolor=Colors.CYAN_700
                    ),
                    Button("ir para seguda tela", on_click= lambda: navegar("/segunda_tela"))
                ]
            )
        )
        if page.route == "/segunda_tela":
            page.views.append(
                View(
                    route="/segunda_tela",
                    controls=[
                        flet.AppBar(
                            title="segunda pagina",
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
