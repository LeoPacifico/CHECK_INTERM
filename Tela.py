import flet as ft

class Tela():
    def __init__(self,usuario,page:ft.Page):
        self.usuario=usuario
        self.page=page
        self.telaPrincipal()

    def telaPrincipal(self):
        self.page.title="Principal"

        #Primeiro container: ft.Rows -> ft.Column
        self.nomeUsuario=ft.Text(value=f'Usuario: {self.usuario}')


        self.container01=ft.Container(
            bgcolor="blue",
            expand=False,
            content=ft.Row(
                alignment=ft.MainAxisAlignment.START,
                controls=[self.nomeUsuario],


            )

        )


        self.page.add(self.container01)






def main(page:ft.Page):
    app=Tela("Leonardo",page)

ft.app(target=main)
