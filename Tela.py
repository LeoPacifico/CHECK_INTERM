import flet as ft

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
        self.TextoEstilo2 = ft.TextStyle(size=12, weight=ft.FontWeight.W_500,color="red")


        #Criação dos Elementos
        self.nomeUsuario=ft.Text(value=f'Usuario: {self.usuario}')
        self.lista_qualidades=["W/Mo","W/Rh","W-MoNomexK","W-MoNomexS","W-MoNomexCSR","W-MoNomexKV","RQR","RQR-C","RQR-T","RQR-Tt","RP"]
        self.lista_detectores={"Piranha": {"Número de série":"NS", "Data Calib": "xx/xx/xxxx"},"Radcal": {"Número de série":"NS", "Data Calib": "xx/xx/xxxx"}}
        self.info_qualidade=ft.Text(spans=[ft.TextSpan("Mamografia: ",style=self.TextoEstilo1),ft.TextSpan("W/Mo ",style=self.TextoEstilo2),ft.TextSpan("0.06 mm Mo",style=self.LabelEstilo)])
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
            options=[ft.DropdownOption(i) for i in self.lista_qualidades],

        )
        # Menu detectores
        self.dropMenu02 = ft.Dropdown(
            label="Detector",
            label_style=self.LabelEstilo,
            menu_height=150,
            width=150,
            text_align="center",
            text_style=self.TextoEstilo1,
            padding=10,
            enable_filter=True,
            enable_search=True,
            editable=True,
            options=[ft.DropdownOption(i) for i in self.lista_detectores],

        )
        self.coluna01=ft.Column(

            controls=[self.dropMenu01,self.info_qualidade],
        )

        self.coluna02 = ft.Column(

            controls=[self.dropMenu02,self.info_cal],
        )

        #Elementos na tela
        self.container01=ft.Container(
            bgcolor="blue",
            expand=False,
            content=ft.Row(

                controls=[self.coluna01,self.coluna02,],


            )

        )

        self.page.add(self.container01)

def main(page:ft.Page):
    tela=Tela("Leonardo",page)

ft.app(target=main)
