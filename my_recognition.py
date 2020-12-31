import time
from datetime import datetime
import speech_recognition as sr


# Começaremos criando o método de callback que será chamado quando a captura do microfone for concluído
def callback(recognizer, audio):
    # Vamo usar o Google Speech Recognition para reconhecer o áudio
    try:
        now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"{now} - O que será que você disse?")
        recognized = recognizer.recognize_google(audio, language="pt-BR")
        now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"{now} - Google Speech Recognition acha que você disse: {recognized}")
    except sr.UnknownValueError:
        now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"{now} - Google Speech Recognition não conseguiu reconhecer o áudio")
    except sr.RequestError as e:
        now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"{now} - O serviço do Google Speech Recognition falhou; {0}".format(e))

r = sr.Recognizer()
m = sr.Microphone()
with m as source:
    r.adjust_for_ambient_noise(source, duration=2)  
    # Usamos este método para calibrar o microfone, ele é executado apenas uma vez

print('Diga alguma coisa:')
# Começará ouvir em segundo plano. Note que não temos que fazer isso dentro de uma instrução 'with'
listening = r.listen_in_background(m, callback, phrase_time_limit=5)

# Manteremos um loop infinito com um contador que servirá para mostrar que
# continuamos a ouvir em segundo plano.
while True: 
    print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    time.sleep(3)