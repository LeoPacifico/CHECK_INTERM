import flet as ft
from flet.core import margin


class Tela():
    def __init__(self,usuario,page:ft.Page):
        self.usuario=usuario
        self.page=page
        self.page.bgcolor=ft.Colors.BLUE_50
        self.telaPrincipal()

    def telaPrincipal(self):
        self.page.title="Principal"


        #Estilos:
        self.LabelEstilo = ft.TextStyle(size=10, weight=ft.FontWeight.BOLD)
        self.TextoEstilo1 = ft.TextStyle(size=12, weight=ft.FontWeight.W_500)
        self.TextoEstilo2 = ft.TextStyle(size=12, weight=ft.FontWeight.BOLD)
        self.TextoEstilo3 = ft.TextStyle(size=12, weight=ft.FontWeight.BOLD, color="red")
        self.TextoEstilo_medidas=ft.TextStyle(size=16,weight=ft.FontWeight.BOLD)


        #CONTAINER 01
        #Criação dos Elementos
        self.nomeUsuario=ft.Text(value=f'Usuario: {self.usuario}')
        self.lista_qualidades=["W/Mo","W/Rh","W-MoNomexK","W-MoNomexS","W-MoNomexCSR","W-MoNomexKV","RQR","RQR-C","RQR-T","RQR-Tt","RP"]
        self.lista_detectores={"Piranha": {"Número de série":"NS", "Data Calib": "xx/xx/xxxx"},"Radcal": {"Número de série":"NS", "Data Calib": "xx/xx/xxxx"}}
        self.info_qualidade=ft.Text(spans=[ft.TextSpan("Mamografia: ",style=self.TextoEstilo2),ft.TextSpan("\n W/Mo ",style=self.TextoEstilo1),ft.TextSpan("\n 0.06 mm Mo",style=self.LabelEstilo)])
        self.info_cal=ft.Text("Última calibração: xx/xx/xxxx",style=self.TextoEstilo1)
        self.dados_list_title=ft.Text(value="XXX",style=self.TextoEstilo1)
        self.list_title=ft.ListTile(
            bgcolor=ft.Colors.BLUE_200,
            title=self.dados_list_title, subtitle=ft.Text("--"),
        )
        self.list_view=ft.ListView(
            padding=30,
            spacing=5,
            divider_thickness=2,
            auto_scroll=None,
            width=350,
            height=200,

            controls=[self.list_title for i in range(10)]
        )

        # Menu qualidades
        self.dropMenu01=ft.Dropdown(
            label="Qualidade",
            label_style=self.LabelEstilo,
            menu_height=150,
            width=200,
            text_align="center",
            text_style=self.TextoEstilo1,
            enable_filter=True,
            enable_search=True,
            editable=True,
            options=[ft.dropdown.Option(i) for i in self.lista_qualidades],

        )
        self.imagem=ft.Image(src="assets/img/teste.png", width=400, height=200, fit=ft.ImageFit.CONTAIN,)
        # Menu detectores
        self.dropMenu02 = ft.Dropdown(

            label="Detector",
            label_style=self.LabelEstilo,
            menu_height=150,
            width=200,
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

        #CONTAINER 02
        # Criação dos Elementos
        self.calculo_fuga = ft.Text("CÁLCULO FUGA")

        #CONTAINER 03
        # Criação dos Elementos
        self.cx_tensao_polar=ft.TextField(label="Tensão de polarizaçao",width=200,height=50)
        self.cx_escala = ft.TextField(label="Escala (nC)", width=200, height=50)
        self.cx_carga_inicial = ft.TextField(label="Carga incial (nC)", width=200, height=50)
        self.cx_carga_final = ft.TextField(label="Carga final (nC)", width=200, height=50)
        self.txt_resultado = ft.Text(spans=[ft.TextSpan(" Resultado: ",style=self.TextoEstilo1),
                                            ft.TextSpan(" Aprovado",style=self.TextoEstilo1),
                                            ft.TextSpan(" Reprovado",style=self.TextoEstilo3)])

        # CONTAINER 04
        # Criação dos Elementos
        self.medidas = ft.Text("DADOS DA CHECAGEM INTERMEDIÁRIA")

        # ----------CONTAINER 05----------
        # Criação dos Elementos
        def achar_elemento_container51():
            print(self.list_title01.control)

        self.indice=ft.Text("--")
        self.aux_ktp=1
        self.cx_medida=ft.TextField(value="10",label="Medida", width=200, height=30,text_style=self.TextoEstilo_medidas)
        self.cx_temperatura = ft.TextField(label="Temperatura (ºC)", width=200, height=30,text_style=self.TextoEstilo_medidas)
        self.cx_pressão_atm = ft.TextField(label="Pressão (kPa)", width=200, height=30,text_style=self.TextoEstilo_medidas)
        self.cx_umidade_rel = ft.TextField(label="Umidade rel. ar (%)", width=200, height=30,text_style=self.TextoEstilo_medidas)
        self.txt_ktp=ft.Text(value=f'Ktp = {self.aux_ktp}')


        #criação da coluna que vai receber os elementos
        self.coluna03=ft.Column(
            controls=[self.cx_medida,self.cx_temperatura,self.cx_pressão_atm,self.txt_ktp]
        )
        # criação da row que vai receber os colunas com os elementos
        self.linha01 = ft.Row(
            controls=[self.coluna03]
        )

        self.container051 = ft.Container(
            padding=5,
            border=ft.border.all(2, "red"),
            expand=False,
            content=ft.Row(
                vertical_alignment=ft.CrossAxisAlignment.START,
                controls=[self.linha01],
            )

        )

        self.list_title01=ft.ListTile(
            subtitle=ft.Container(
                content=ft.Row(
                    controls=[self.container051 for i in range (5)],
                )
            )

        )
        self.list_view01 = ft.ListView(
            padding=30,
            spacing=5,
            divider_thickness=4,
            auto_scroll=None,
            width=1000,
            height=500,

            controls=[self.list_title01 for i in range(2)]

        )


        #Elementos na tela CONTAINER01
        self.container01=ft.Container(
            padding=5,
            border=ft.border.all(1,"black"),
            #bgcolor=ft.Colors.AMBER_50,
            expand=False,
            content=ft.Row(
                vertical_alignment=ft.CrossAxisAlignment.START,
                controls=[self.coluna01,self.coluna02,self.list_view,self.imagem],
            )
        )

        # Elementos na tela CONTAINER02
        self.container02 = ft.Container(
            padding=5,
            border=ft.border.all(1, "black"),
            expand=False,
            content=ft.Row(
                vertical_alignment=ft.CrossAxisAlignment.START,
                controls=[self.calculo_fuga],
            )

        )


        # Elementos na tela CONTAINER03
        self.container03 = ft.Container(
            padding=5,
            border=ft.border.all(1, "black"),
            expand=False,
            content=ft.Row(
                vertical_alignment=ft.CrossAxisAlignment.START,
                controls=[self.cx_tensao_polar,self.cx_escala,self.cx_carga_inicial,self.cx_carga_final,self.txt_resultado],
            )

        )
        # Elementos na tela CONTAINER04
        self.container04 = ft.Container(
            padding=5,
            border=ft.border.all(1, "black"),
            expand=False,
            content=ft.Row(
                vertical_alignment=ft.CrossAxisAlignment.START,
                controls=[self.medidas],
            )

        )

        # Elementos na tela CONTAINER05
        self.container05 = ft.Container(

            padding=5,
            border=ft.border.all(1, "black"),
            expand=False,
            content=ft.Row(
                vertical_alignment=ft.CrossAxisAlignment.START,
                controls=[self.list_view01],
            )

        )

        achar_elemento_container51()
        self.page.add(self.container01,self.container02, self.container03,self.container04,self.container05)

def main(page:ft.Page):
    tela=Tela("Leonardo",page)

ft.app(target=main)
