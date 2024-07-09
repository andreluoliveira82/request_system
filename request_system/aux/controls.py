import flet as ft


def text_field(
    hint_text: str,
    size: int,
    color: ft.colors,
    prefix_icon: ft.icons = None,
    suffix_icon: ft.icons = None,
    border: ft.InputBorder = ft.InputBorder.OUTLINE,
    password: bool = False,
    autofocus: bool = False,
    on_change: ft.ControlEvent = None,
    col: dict = {"sm": 12, "md": 4},
):
    text_field = ft.TextField(
        hint_text=hint_text,
        hint_style=ft.TextStyle(
            size=size, weight="normal", color=ft.colors.with_opacity(0.2, color=color)
        ),
        text_style=ft.TextStyle(size=size, weight="normal", color=color),
        prefix_icon=prefix_icon,
        suffix_icon=suffix_icon,
        border=border,
        password=password,
        autofocus=autofocus,
        on_change=on_change,
        col=col,
    )
    return text_field


def floating_button(
    bgcolor: ft.colors,
    width: int,
    height: int,
    text: str = None,
    icon: ft.icons = None,
    on_click: ft.ControlEvent = None,
    col: dict = {"sm": 12, "md": 4},
):
    btn_floating = ft.FloatingActionButton(
        bgcolor=bgcolor,
        width=width,
        height=height,
        text=text,
        icon=icon,
        on_click=on_click,
        col=col,
    )
    return btn_floating
