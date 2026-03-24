import flet
from flet import ThemeMode, Text, TextField, Button, OutlinedButton, Column, CrossAxisAlignment


def main(page: flet.Page):
    # configuracoes
    page.tittle = "primeiro APP"
    page.theme_mode = ThemeMode.LIGHT
    page.window.width = 400
    page.window.height = 700

    # funcoes

    def salvar_nome():
        text.value = f"bom dia {input_nome.value} {input_sobrenome.value}"
        page.update()

    # componentes
    text = Text()
    input_nome = TextField(label="Nome")
    input_sobrenome = TextField(label="sobrenome")
    btn_salvar_1 = OutlinedButton("Salvar", on_click=salvar_nome)

    def verificar_numero():
        num1 = int(input_numero.value)
        print(f'asd {num1}')
        try:
            if num1 % 2 == 0:
                t1.value = f'o numero: {num1} é par'
                page.update()
            else:
                t1.value = f'o numero {num1} é impar'
                page.update()
        except Exception as e:
            t1.value = f'apenas numeros'
            page.update()

    t1 = Text()
    input_numero = TextField(label="digite um numero")
    btn_salvar_2 = OutlinedButton("Salvar", on_click=verificar_numero)

    def data_nascimento():
        idade = int(input_idade.value)
        resultado_idade = 2026 - idade
        if resultado_idade >= 18:
            text.value = f'maior de idade {resultado_idade}'
            page.update()
        else:
            text.value = f'menor de idade {resultado_idade}'
            page.update()


    input_idade = TextField(label="ano de nascimento")
    btn_salvar_3 = OutlinedButton("Salvar", on_click=data_nascimento)
    text = Text()

# construcao da tela

    page.add(
    Column(
        [
            input_nome,
            input_sobrenome,
            btn_salvar_1,

            input_numero,
            btn_salvar_2,

            input_idade,
            btn_salvar_3,
            t1,
            text,
        ],
        width=400,
        horizontal_alignment=CrossAxisAlignment.CENTER
    )
)

flet.app(main)
