import asyncio

import flet
from flet import ThemeMode, Text, TextField, OutlinedButton, Column, CrossAxisAlignment, Container, Colors, FontWeight, \
    View, AppBar, FloatingActionButton, Button, ListView, Card, Row, Icon, ListTile, PopupMenuButton, PopupMenuItem
from flet.controls import page
from flet.controls.border_radius import horizontal
from flet.controls.material.icons import Icons


def main(page: flet.Page):

    page.title = "exemplo de listas"
    page.theme_mode = ThemeMode.DARK
    page.window.width = 400
    page.window.height = 700

    lista_dados = []

    # funções


    # navegar
    def navegar(route):
        asyncio.create_task(
            page.push_route(route)
        )

    def montar_lista_texto():
        list_view.controls.clear()


        for item in lista_dados:
            list_view.controls.append(
                Text(item)
        )

    def montar_lista_card():
        list_view.controls.clear()
        for item in lista_dados:
            list_view.controls.append(
                Card(
                    height=50,
                    content=Row([
                            Icon(Icons.PERSON),
                            Text(item)
                    ],
                    margin=8,
                    ),
                )
            )


    def montar_lista_padrao():
        list_view.controls.clear()


        for item in lista_dados:
            list_view.controls.append(
                ListTile(
                    leading= Icon(Icons.PERSON),
                    title=item,
                    subtitle="subtitulo",
                    trailing=PopupMenuButton(
                        icon=Icons.MORE_VERT,
                        items=[
                            PopupMenuItem("ver detalhes", icon=Icons.REMOVE_RED_EYE),
                            PopupMenuItem("excluir", icon=Icons.DELETE, on_click=lambda: excluir(item))
                        ]
                    ),
                )
        )


    def excluir(item):
        lista_dados.remove(item)
        montar_lista_padrao()



    def salvar_dados():
        nome = input_nome.value.strip()

        if nome:
            lista_dados.append(nome)
            input_nome.error = None
            input_nome.value = ""
        else:
            input_nome.error = "campo obrigatório"

        montar_lista_texto()
        montar_lista_card()
        montar_lista_padrao()


    # gerenciar as telas (routes)

    def route_change():
        page.views.clear()
        page.views.append(
            View(
                route="/",
                controls=[
                    AppBar(
                        title="exemplo de listas",
                        bgcolor=Colors.CYAN_700
                    ),
                    OutlinedButton("lista de texto", on_click=lambda: navegar("/lista_texto")),
                    OutlinedButton("lista de card", on_click=lambda: navegar("/lista_card")),
                    OutlinedButton("lista padrão android", on_click=lambda: navegar("/lista_padrao"))

                ]
            )
        )
        if page.route == "/lista_texto":
            montar_lista_texto()
            page.views.append(
                View(
                    route="/lista_texto",
                    controls=[
                        AppBar(
                            title="lista de texto",
                        ),
                    input_nome,
                    btn_salvar,
                    list_view

                ]
            )
        )
        elif page.route == "/lista_card":
            montar_lista_card()
            page.views.append(
                View(
                    route="/lista_card",
                    controls=[
                        AppBar(
                            title="lista de Card",
                        ),
                        input_nome,
                        btn_salvar,
                        list_view
                    ]
                )
            )
        elif page.route == "/lista_padrao":
            montar_lista_padrao()
            page.views.append(
                View(
                    route="/lista_padrao",
                    controls=[
                        AppBar(
                            title="lista padrão Android",
                        ),
                        list_view
                    ],
                    floating_action_button=FloatingActionButton(
                        icon=Icons.ADD,
                        on_click=lambda: navegar("/form_cadastro"),
                    )
                )
            )
        elif page.route == "/form_cadastro":
            page.views.append(
                View(
                    route="/form_cadastro",
                    controls=[
                        AppBar(
                            title="cadastro",
                        ),
                        input_nome,
                        input_profissao,
                        btn_salvar,
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


    input_nome = TextField(label="nome", hint_text="digite seu nome", on_submit=salvar_dados)
    input_profissao = TextField(label="profissão", hint_text="digite sua profissão", on_submit=salvar_dados)


    btn_salvar = Button("salvar", width=400, on_click=lambda: salvar_dados())
    list_view = ListView(height=500)


    # eventos


    page.on_route_change = route_change
    page.on_view_pop= view_pop

    route_change()

flet.run(main)

