import flet as ft


def main(page: ft.Page):
    page.add(
        ft.Column(
            controls=[
                ft.Image(
                    src="Gemini_Generated_Image_kirrzikirrzikirr.png"
                ),
                ft.Button(content="Enabled button")
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True
        )
    )


ft.run(main)