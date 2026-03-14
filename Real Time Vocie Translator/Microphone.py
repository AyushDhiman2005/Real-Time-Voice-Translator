

def mic():
    import speech_recognition as sr
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # print("module ends!")

        r.pause_threshold=2
        r.energy_threshold=250
        audio=r.listen(source)
    try:
        print("Recognising...")
        query=r.recognize_google(audio)   
        print("User said:",query) 
    except Exception as e:
        print("Error:",e)
        #print("Say that again please!")
        return "none"
    return query
    





