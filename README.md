# codigosinvertexto
códigos do invertexto
INSTALAR: pip install google-generativeai  

CÓDIGO DE IA NO CÓDIGO






import google.generativeai as genai

genai.configure(api_key="")

prompts = {
  "Resumo": "Resuma o seguinte assunto de forma clara e objetiva: ",
  "Explicação Simples": "Explique de forma simples e didática para um iniciante o seguinte assunto: ",
  "Gerador De Ideias": "Gere ideias criativa sobre o seguinte tema: ",
  "Tradutor": "Traduza o seguinte texto para o inglês, coloque uma aplicação em uma frase, e dê exemplos de flexibilidade dessa mesma palavra: "
}



def gerarResposta(pergunta, filtro):
  texto_final = f"{filtro} {pergunta}"
  modelo = genai.GenerativeModel("gemini-pro")
  resposta =  modelo.generate_content(texto_final)
  return resposta.text


while True:
  menu = input("""
  Escolha uma Opção:
  1 - Resumo
  2 - Explicação Simples
  3 - Gerador de Ideias
  4 - Tradutor
  0 - Sair
  """)

  match menu:
    case "1":
      assunto = input("Digite o assunto que você quer um resumo: ")
      print(gerarResposta(pergunta=assunto, filtro=prompts["Resumo"]))
    case "2":
      assunto = input("Digite o assunto que você quer ler uma explicação simples: ")
      print(gerarResposta(pergunta=assunto, filtro=prompts["Explicação Simples"]))
    case "3":
      assunto = input("Digite o assunto que você quer gerar ideias: ")
      print(gerarResposta(pergunta=assunto, filtro=prompts["Gerador De Ideias"]))
    case "4":
      assunto = input("Digite o assunto que você quer traduzir: ")
      print(gerarResposta(pergunta=assunto, filtro=prompts["Tradutor"]))
    case "0":
      print("Fim do programa")
      break
    case _:
      print("Opção inválida")



      outra aula de ia no código em python

      https://github.com/abelardojr0



import google.generativeai as genai
from colorama import Fore, Style, init

init(autoreset=True)  

genai.configure(api_key="VÁ ATRAS DA SUA CHAVE NO GEMINI")


prompts = {
    "resumo": "Resuma o seguinte assunto de forma clara e objetiva: ",
    "explicacao_simples": "Explique de forma simples e didática para um iniciante:",
    "geracao_de_ideias": "Gere ideias criativas sobre o seguinte tema:",
    "traducao": "Traduza o seguinte texto para inglês, coloque uma aplicação em uma frase e explique palavra por palavra:"
}


def gerar_resposta(opcao, entrada_usuario):
        prompt_escolhido = f"{prompts[opcao]} {entrada_usuario}"
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt_escolhido)

        return response.text




opcoes = ['resumo', 'explicacao_simples', 'geracao_de_ideias', 'traducao']

while True:
    posicao_escolhida = int(input("""
    📜 MENU DE OPÇÕES 📜
    1️⃣ - Resumo
    2️⃣ - Explicação Simples
    3️⃣ - Geração de Ideias
    4️⃣ - Tradução
    0️⃣ - Sair
    🛑 Digite o número da opção desejada:
        """))
    if posicao_escolhida > 0 and posicao_escolhida <= len(opcoes):
        opcao = opcoes[posicao_escolhida - 1]

        if opcao not in prompts:
            print("❌ Opção inválida. Tente novamente. ❌ ")
        else:
            entrada_usuario = input("Digite o tema: ").strip()
            resposta = gerar_resposta(opcao, entrada_usuario)
            resposta = resposta.replace("**", "").replace("* ", "- ")
            print(f"""
🤖🤖🤖🤖🤖🤖🤖🤖

Resposta da IA: 
{Fore.GREEN}{resposta}{Style.RESET_ALL}

🤖🤖🤖🤖🤖🤖🤖🤖
            """)
    elif posicao_escolhida == 0:
        print("👋  Fim do programa 👋 " )
        break
    else:
        print("❌ Opção inválida ❌")
================================================================================================

SUPER MÓDULO DE AUTOMAÇÃO EM PYTHON
https://github.com/EricWSS/automacao_ia
================================================================================================
CÓDIGO DE INTERFACE EM FLET AULA 14 PYTHON
import flet as ft
import random

# ---- Back-end (sua classe) ----
class Clientes:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.__ID = self.gerar_ID()
    
    def mostrarDados(self):
        dados = (
            f"Cliente ({self.nome}) cadastrado\n"
            f"Telefone: (85) 9 {self.telefone}\n"
            f"E-mail: {self.email}\n"
            f"ID: {self.__ID}\n"
        )
        return dados  # Vamos retornar os dados como texto para mostrar no app
    
    def gerar_ID(self):
        numeros = [str(random.choice([1,2,3,4])) for i in range(4)]
        return ''.join(numeros)

# ---- Front-end (Flet) ----
def main(page: ft.Page):
    page.title = "Cadastro de Clientes"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Criar os campos de entrada
    nome_input = ft.TextField(label="Nome", width=300)
    telefone_input = ft.TextField(label="Telefone (sem DDD)", width=300)
    email_input = ft.TextField(label="E-mail", width=300)

    # Área onde vamos mostrar o resultado
    resultado_text = ft.Text()

    # Função que será chamada quando o botão for clicado
    def cadastrar_cliente(e):
        nome = nome_input.value
        telefone = telefone_input.value
        email = email_input.value

        if nome and telefone and email:
            cliente = Clientes(nome, telefone, email)
            resultado_text.value = cliente.mostrarDados()
            page.update()
        else:
            resultado_text.value = "Por favor, preencha todos os campos."
            page.update()

    # Botão para acionar o cadastro
    botao_cadastrar = ft.ElevatedButton("Cadastrar Cliente", on_click=cadastrar_cliente)

    # Adicionar tudo na tela
    page.add(
        nome_input,
        telefone_input,
        email_input,
        botao_cadastrar,
        resultado_text,
    )

# Rodar o app
ft.app(target=main)


