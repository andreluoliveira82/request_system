import sys

sys.path.append("request_system/aux")
from request_system.aux.controls import *


def recovery_password(page: ft.Page, login: ft.Container):

    # function to close msgbox
    def close_msgbox(e):
        alert_dialog.open = False
        login.visible = True
        page.update()

    # function to validate user
    def validate_user(e):
        # remove o campo (textfield) 'email'
        # alert_dialog.content.controls.remove(email)
        email.visible=False
        alert_dialog.content.height = 160
        alert_dialog.content.width = 320
        username.prefix_icon = ft.icons.CONFIRMATION_NUM
        username.hint_text = 'Código de verificação'
        username.autofocus = True
        btn_recovery_password.text = "Verificar Código"
        page.update()
        

    page.expand = True

    alert_dialog = ft.AlertDialog(
        modal=True,
        title=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.Text(
                    value="Recuperar Senha",
                    size=18,
                    weight="bold",
                    color=ft.colors.BLACK,
                ),
                ft.IconButton(
                    icon=ft.icons.CLOSE,
                    icon_color=ft.colors.RED,
                    icon_size=25,
                    on_click=close_msgbox,
                ),
            ],
        ),
        content=ft.Column(
            width=320,
            height=168,

            controls=[
                username := text_field(
                    hint_text="Username",
                    autofocus=True,
                    prefix_icon=ft.icons.PERSON,
                    size=14,
                    color=ft.colors.BLACK,
                    border=ft.InputBorder.UNDERLINE,
                ),
                email := text_field(
                    hint_text="Email",
                    prefix_icon=ft.icons.EMAIL,
                    size=14,
                    color=ft.colors.BLACK,
                    border=ft.InputBorder.UNDERLINE,
                    password=True,
                ),
                btn_recovery_password := floating_button(
                    bgcolor=ft.colors.BLUE,
                    text="Recuperar Senha",
                    width=320,
                    height=42,
                    icon=ft.icons.SEND,
                    on_click=validate_user,
                ),
            ],
        ),
    )
    return alert_dialog
