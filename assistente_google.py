import speech_recognition as sr
from nltk import word_tokenize, corpus
from calcular import CALCULAR
import json

IDIOMA_CORPUS = "portuguese"
IDIOMA_FALA = "pt-BR"
CAMINHO_CONFIGURACAO = "config.json"

ATUADORES = [ CALCULAR ]

def iniciar():
    global reconhecedor
    global palavras_de_parada
    global nome_assistente
    global acoes

    reconhecedor = sr.Recognizer()
    palavras_de_parada = set(corpus.stopwords.words(IDIOMA_CORPUS))

    with open(CAMINHO_CONFIGURACAO, "r", encoding='utf8') as arquivo_configuracao:
        configuracao = json.load(arquivo_configuracao)

        nome_assistente = configuracao["nome"]
        acoes = configuracao["acoes"]

        arquivo_configuracao.close()



def escutar_comando():
    global reconhecedor

    comando = None

    with sr.Microphone() as fonte_audio:
        reconhecedor.adjust_for_ambient_noise(fonte_audio)

        print("Olá, sou a Ruth! Estou aqui pra poder ajuda-lo em algum cálculo simples...")
        print("Estou te ouvindo, pode fazer sua pergunta...")
        fala = reconhecedor.listen(fonte_audio, timeout=5, phrase_time_limit=5)
        try:
            comando = reconhecedor.recognize_google(fala, language=IDIOMA_FALA)
        except sr.UnknownValueError:
            pass

    return comando


def eliminar_palavras_de_parada(tokens):
    global palavras_de_parada

    tokens_filtrados = []
    for token in tokens:
        if token not in palavras_de_parada:
            tokens_filtrados.append(token)

    return tokens_filtrados


def tokenizar_comando(comando):
    global nome_assistente

    acao = None
    operacao = None
    numero1 = None
    numero2 = None

    tokens = word_tokenize(comando, IDIOMA_CORPUS)
    if tokens:
        tokens = eliminar_palavras_de_parada(tokens)

        if len(tokens) == 4:
            if nome_assistente == tokens[0].lower():
                acao = tokens[1].lower()
                numero1 = tokens[2].lower()
                operacao = tokens[3].lower()
                numero2 = 0
        
        if len(tokens) >= 5:
            if nome_assistente == tokens[0].lower():
                acao = tokens[1].lower()
                numero1 = tokens[2].lower()
                operacao = tokens[3].lower()
                numero2 = tokens[4].lower()  
    
    return acao,  numero1, operacao, numero2
        

   


def validar_comando(acao, operacao):
    global acoes

    valido = False

    if acao and operacao:
        for acao_cadastrada in acoes:
            if acao == acao_cadastrada["nome"]:
                if operacao in acao_cadastrada["operacoes"]:
                    valido = True

                break

    return valido


def executar_comando( numero1, operacao, numero2):
    print(f"Estou processando as operaçõs!")

    for atuador in ATUADORES:
        executado = atuador["executar"](  numero1, operacao, numero2)

        if executado:
            break


if __name__ == '__main__':
    iniciar()

    continuar = True
    while continuar:
        try:
            comando = escutar_comando()
            print(f"Lendo o comando: {comando}")

            if comando:
                              
                acao,  numero1, operacao, numero2 = tokenizar_comando(comando)
                valido = validar_comando(acao, operacao)
                if valido:
                    executar_comando(numero1, operacao, numero2)
                else:
                    print("Não entendi o comando. Repita, por favor!")
        except KeyboardInterrupt:
            continuar = False

    for atuador in ATUADORES:
        atuador["finalizar"]()

    print("Tchau!")