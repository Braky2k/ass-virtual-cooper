import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import subprocess

# Objeto para reconhecer o aúdio
audio = sr.Recognizer()
# Iniciando a biblioteca na variável maquina
maquina = pyttsx3.init()

def execucao():
    # Tentativas de execução
    try:
        # Executa quando a fala for recebida
        with sr.Microphone() as source:
            print('Ouvindo...')
            # Variável para escutar o que for dito
            voz = audio.listen(source)
            # Variável para entender a ordem do usuário
            comando = audio.recognize_google(voz, language='pt-BR')
            # Transferindo a str do comando para caixa baixa.
            comando = comando.lower()
            # Nome do produto
            if 'cooper' in comando:
                # Se houver o nome Kuper no comando, o programa se executa.
                comando = comando.replace('cooper', '')
                # Executando
                maquina.runAndWait()
    except:
        print('Mensagem não captada')
    return(comando)

def abrir_programa(programa):
    try:
        subprocess.Popen(programa, shell=True)
    except Exception as e:
        print(f"Erro ao abrir o programa {programa}: {e}")

def comando_pedido():
    comando = execucao()
    # Caso o usuário pergunte sobre as horas exatas.
    if 'horas' in comando:
        hora = datetime.datetime.now().strftime('%H:%M')
        maquina.say('Agora são' + hora)
        maquina.runAndWait()
    # Pesquisa sobre informações
    elif 'pesquise sobre' in comando or 'procure por' in comando or 'pesquise' in comando:
        procurar = comando.replace('pesquise sobre', '').replace('pesquise', '').replace('procure por', '')
        wikipedia.set_lang('pt')
        resultado = wikipedia.summary(procurar, 2)
        print(resultado)
        maquina.say(resultado)
        maquina.runAndWait()
    elif 'abra' in comando or 'abra o aplicativo' in comando or 'execute' in comando:
        programa = comando.replace('abra', '').replace('abra o aplicativo', '').replace('execute', '')
        caminho_programa = f'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\{programa.title().strip()}.lnk'
        print(caminho_programa)
        abrir_programa(caminho_programa)

comando_pedido()