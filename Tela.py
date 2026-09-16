import flet as ft
from flet.core import margin


class Tela():
    def __init__(self,usuario,page:ft.Page):
        self.usuario=usuario
        self.page=page
        self.telaPrincipal()

    def telaPrincipal(self):
        self.page.title="Principal"

        #Primeiro container: ft.Rows -> ft.Column
        #Estilos:
        self.LabelEstilo = ft.TextStyle(size=10, weight=ft.FontWeight.BOLD)
        self.TextoEstilo1 = ft.TextStyle(size=12, weight=ft.FontWeight.W_500)
        self.TextoEstilo2 = ft.TextStyle(size=12, weight=ft.FontWeight.BOLD)


        #Criação dos Elementos
        self.nomeUsuario=ft.Text(value=f'Usuario: {self.usuario}')
        self.lista_qualidades=["W/Mo","W/Rh","W-MoNomexK","W-MoNomexS","W-MoNomexCSR","W-MoNomexKV","RQR","RQR-C","RQR-T","RQR-Tt","RP"]
        self.lista_detectores={"Piranha": {"Número de série":"NS", "Data Calib": "xx/xx/xxxx"},"Radcal": {"Número de série":"NS", "Data Calib": "xx/xx/xxxx"}}
        self.info_qualidade=ft.Text(spans=[ft.TextSpan("Mamografia: ",style=self.TextoEstilo2),ft.TextSpan("\n W/Mo ",style=self.TextoEstilo1),ft.TextSpan("\n 0.06 mm Mo",style=self.LabelEstilo)])
        self.info_cal=ft.Text("Última calibração: xx/xx/xxxx",style=self.TextoEstilo1)


        # Menu qualidades
        self.dropMenu01=ft.Dropdown(
            label="Qualidade",
            label_style=self.LabelEstilo,
            menu_height=150,
            width=150,
            text_align="center",
            text_style=self.TextoEstilo1,
            padding=10,
            enable_filter=True,
            enable_search=True,
            editable=True,
            options=[ft.dropdown.Option(i) for i in self.lista_qualidades],

        )
        # Menu detectores
        self.dropMenu02 = ft.Dropdown(

            label="Detector",
            label_style=self.LabelEstilo,
            menu_height=150,
            width=150,
            text_align='center',
            text_style=self.TextoEstilo1,
            enable_filter=True,
            enable_search=True,
            editable=True,
            options=[ft.dropdown.Option(text=i, text_style=self.TextoEstilo1,) for i in self.lista_detectores],

        )
        self.coluna01=ft.Column(
            alignment=ft.VerticalAlignment.START,
            controls=[self.dropMenu01,self.info_qualidade],
        )

        self.coluna02 = ft.Column(
            alignment=ft.VerticalAlignment.START,
            controls=[self.dropMenu02,self.info_cal],
        )

        #Elementos na tela
        self.container01=ft.Container(
            padding=5,
            bgcolor="lightblue",
            expand=False,
            content=ft.Row(
                vertical_alignment=ft.CrossAxisAlignment.START,
                controls=[self.coluna01,self.coluna02,],


            )

        )

        self.page.add(self.container01)

def main(page:ft.Page):
    tela=Tela("Leonardo",page)

ft.app(target=main)
