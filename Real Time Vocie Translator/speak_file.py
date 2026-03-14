#This function takes query input and return audio as output

def speak(audio):
    #importing pyttsx3 module whcih stores the functions getProperty() , setProperty() , say() and runAndWait
    import pyttsx3

    #engine is taken as a variable which stores the voice of sapi5 
    engine=pyttsx3.init('sapi5')

    #getting the voice property of sapi5
    voices=engine.getProperty('voices')

    #selecting the voice id that are available in sapi5
    engine.setProperty('voices',voices[0].id)
    current_rate = engine.getProperty('rate')
    new_rate = 150
    engine.setProperty('rate', new_rate)
    #this function returns the audio
    engine.say(audio)
    
    #this function is for wait
    engine.runAndWait()
    

