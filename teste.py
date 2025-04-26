import flet as ft
import random

# ---- Classes (Cliente e Quarto) ----
class Clientes:
    def __init__(self, nome, telefone, email, quarto_escolhido):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.quarto = quarto_escolhido
        self.__ID = self.gerar_ID()
    
    def mostrarDados(self):
        dados = (
            f"Cliente: {self.nome}\n"
            f"Telefone: {self.telefone}\n"
            f"E-mail: {self.email}\n"
            f"Quarto escolhido: {self.quarto}\n"
            f"ID: {self.__ID}\n"
        )
        return dados
    
    def gerar_ID(self):
        numeros = [str(random.choice([1,2,3,4])) for i in range(4)]
        return ''.join(numeros)

# ---- Interface Flet ----
def main(page: ft.Page):
    page.title = "Sistema de Reservas de Hotel"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START

    # Campos de input
    nome_input = ft.TextField(label="Nome", width=300)
    telefone_input = ft.TextField(label="Telefone", width=300)
    email_input = ft.TextField(label="Email", width=300)

    resultado_text = ft.Text()

    # Variável para guardar qual quarto foi selecionado
    quarto_selecionado = ft.Text(value="Nenhum quarto selecionado", size=14)

    # Função para quando clicar numa imagem de quarto
    def selecionar_quarto(e):
        quarto_selecionado.value = e.control.data  # data contém o nome do quarto
        page.update()

    # Lista de imagens dos quartos
    quartos = [
        {"nome": "Quarto Luxo", "imagem": "https://picsum.photos/200/150?1"},
        {"nome": "Quarto Simples", "imagem": "https://picsum.photos/200/150?2"},
        {"nome": "Suíte Master", "imagem": "https://picsum.photos/200/150?3"},
    ]

    imagens_quartos = []
    for quarto in quartos:
        imagem = ft.Image(
            src=quarto["imagem"],
            width=200,
            height=150,
            fit=ft.ImageFit.COVER
        )
        imagem_container = ft.Container(
            content=imagem,
            on_click=selecionar_quarto,
            data=quarto["nome"],  # Guarda o nome do quarto nesse botão
            border=ft.border.all(1, ft.colors.BLACK),
            border_radius=10,
            padding=5,
            margin=10,
            ink=True,  # Deixa clicável com efeito
        )
        imagens_quartos.append(imagem_container)

    # Botão de cadastro
    def cadastrar_cliente(e):
        nome = nome_input.value
        telefone = telefone_input.value
        email = email_input.value
        quarto = quarto_selecionado.value

        if nome and telefone and email and quarto != "Nenhum quarto selecionado":
            cliente = Clientes(nome, telefone, email, quarto)
            resultado_text.value = cliente.mostrarDados()
            page.update()
        else:
            resultado_text.value = "Preencha todos os campos e selecione um quarto!"
            page.update()

    botao_cadastrar = ft.ElevatedButton("Reservar Quarto", on_click=cadastrar_cliente)

    # Layout da tela
    layout_formulario = ft.Column([
        nome_input,
        telefone_input,
        email_input,
        quarto_selecionado,
        botao_cadastrar,
        resultado_text
    ])

    layout_imagens = ft.Column(imagens_quartos)

    page.add(
        ft.Row(
            [
                layout_formulario,
                layout_imagens
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.START
        )
    )

ft.app(target=main)


                             EXPLICANDO O CÓDIGO
=================================================================================================================
                                 Vamos linha por linha e bem detalhado para você entender tudo o que está acontecendo:


imagens_quartos = []
Cria uma lista vazia chamada imagens_quartos.

Essa lista vai guardar todos os "cartõezinhos" de quartos (as imagens que o usuário poderá clicar).


for quarto in quartos:
Inicia um laço (for) para percorrer cada item da lista quartos.

A lista quartos é aquela que tem dicionários com nome e imagem de cada quarto, lembra?

Exemplo do que quartos contém:


[
    {"nome": "Quarto Luxo", "imagem": "imagens_quartos/quarto_luxo.jpg"},
    {"nome": "Quarto Simples", "imagem": "imagens_quartos/quarto_simples.jpg"},
    {"nome": "Suíte Master", "imagem": "imagens_quartos/suite_master.jpg"},
]

    imagem = ft.Image(
        src=quarto["imagem"],  # Usando o caminho local
        width=200,
        height=150,
        fit=ft.ImageFit.COVER
    )
Cria um componente de imagem do Flet (ft.Image).

src=quarto["imagem"]: define o caminho da imagem que foi informado no dicionário ("imagens_quartos/quarto_luxo.jpg", por exemplo).

width=200: largura da imagem será 200 pixels.

height=150: altura da imagem será 150 pixels.

fit=ft.ImageFit.COVER: garante que a imagem se encaixe perfeitamente dentro do espaço, sem distorcer (ela "cobre" o espaço).


    imagem_container = ft.Container(
        content=imagem,
        on_click=selecionar_quarto,
        data=quarto["nome"],  # Guarda o nome do quarto nesse botão
        border=ft.border.all(1, ft.colors.BLACK),
        border_radius=10,
        padding=5,
        margin=10,
        ink=True,  # Deixa clicável com efeito
    )
Cria um container (caixinha) para a imagem.

content=imagem: coloca a imagem que acabamos de criar dentro da caixinha.

on_click=selecionar_quarto: define o que acontece quando o usuário clicar nesse container.
(Chama a função selecionar_quarto, que vai registrar qual quarto foi escolhido.)

data=quarto["nome"]: guarda informações extras no container — no caso, o nome do quarto (ex.: "Quarto Luxo").
Isso é útil para saber depois qual quarto foi clicado.

border=ft.border.all(1, ft.colors.BLACK): coloca uma borda preta de 1 pixel ao redor do container.

border_radius=10: deixa os cantos da borda arredondados (10 de raio).

padding=5: adiciona um espaço interno de 5 pixels (entre a borda e a imagem).

margin=10: adiciona um espaço externo de 10 pixels (entre este container e o próximo).

ink=True: ativa efeito visual de clique (tipo um efeito de "onda" quando clica, bem bonito).


    imagens_quartos.append(imagem_container)
Adiciona o container com a imagem (e suas configurações) na lista imagens_quartos.

Assim, no final do for, teremos uma lista cheia de containers — um para cada quarto.

Resumindo a ideia geral:
Percorremos todos os quartos.

Para cada quarto, criamos:

Uma imagem (ft.Image).

Um container clicável (ft.Container) envolvendo a imagem.

Cada container guarda o nome do quarto associado.

Salvamos todos os containers numa lista para depois mostrar tudo junto na tela.
