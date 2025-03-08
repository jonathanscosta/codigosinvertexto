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
