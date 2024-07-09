from request_system.views.password_recovery import *


def main(page: ft.Page):
    page.title = "Request Management System"
    page.window.maximized = True
    page.theme_mode = ft.ThemeMode.LIGHT

    # function to open dialog recovery password
    def forgot_password(e):
        page.dialog = recovery_password(page, login)
        page.dialog.open = True
        login.visible = False
        page.update()

    container = ft.Container(
        width=page.window.width,
        height=page.window.height,
        alignment=ft.alignment.center,
        content=ft.Column(
            controls=[
                login := ft.Container(
                    width=320,
                    height=380,
                    bgcolor=ft.colors.WHITE,
                    border_radius=10,
                    padding=ft.padding.only(left=10, top=20, right=10),
                    expand=False,
                    content=ft.Column(
                        controls=[
                            ft.Text(
                                "Login",
                                size=20,
                                weight=ft.FontWeight.BOLD,
                                color=ft.colors.with_opacity(
                                    0.6, color=ft.colors.BLACK
                                ),
                            ),
                            username := text_field(
                                hint_text="Username",
                                autofocus=True,
                                prefix_icon=ft.icons.PERSON,
                                size=14,
                                color=ft.colors.BLACK,
                                border=ft.InputBorder.UNDERLINE,
                            ),
                            password := text_field(
                                hint_text="Password",
                                prefix_icon=ft.icons.KEY,
                                suffix_icon=ft.icons.VISIBILITY,
                                size=14,
                                color=ft.colors.BLACK,
                                border=ft.InputBorder.UNDERLINE,
                                password=True,
                            ),
                            btn_login := floating_button(
                                bgcolor=ft.colors.BLUE,
                                text="Login",
                                width=300,
                                height=38,
                            ),
                            btn_forgot_password := ft.TextButton(
                                text="Esqueci minha senha",
                                width=None,
                                style=ft.ButtonStyle(
                                    color=ft.colors.BLUE, overlay_color=ft.colors.WHITE
                                ),
                                on_click=forgot_password,
                            ),
                        ],
                        spacing=25,
                        expand=True,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
    )

    page.add(container)
    page.update()


if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")
