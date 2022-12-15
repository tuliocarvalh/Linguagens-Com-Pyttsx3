import pyttsx3


#Iniciando as propriedades
en = pyttsx3.init()
en.setProperty('rate', 180) 
en.setProperty('volume', 0.8)


#Frases em linguagens diferentes
talkpt = "Ola, senhor. como vai?"
talken = "hello, sir. what's up?"
talkmex = "Hola señor. ¿y ahí?"
talkgerman = "Hallo Herr, wie gehts?"
talkrussian = "Zdravstvuyte. Kak dela?"
talkjapan = "Kon'nichiwa. Genkidesu ka?"



#metodos com a propriedade de idioma
def ingles() :
    en.setProperty('voice', 'English')

def portugues() :
    en.setProperty('voice', b'Brazil')

def espanhol() :
    en.setProperty('voice', 'Mexico')

def german() :
    en.setProperty('voice', 'German')

def russian() :
    en.setProperty('voice', 'Russian')

def japan() :
    en.setProperty('voice', 'japanese')

#Unindo as propriedades e as linguagnes especificas. Voce pode alterar as frases para retornar o texto de outra funcao com o Self.
def pt():
    portugues()
    en.say(talkpt)
    en.runAndWait()

def ing():
    ingles()
    en.say(talken)
    en.runAndWait()

def esp():
    espanhol()
    en.say(talkmex)
    en.runAndWait()

def germ():
    german()
    en.say(talkgerman)
    en.runAndWait()

def russ():
    russian()
    en.say(talkrussian)
    en.runAndWait()
    
def jap():
    japan()
    en.say(talkjapan)
    en.runAndWait()



