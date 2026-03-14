def main(lang1='hi',lang2='en'):
    from Microphone import mic
    from speak_file import speak
    from Translation import translate_text
    from Speak_2 import speak_text


    query = mic().lower()
    print("Translation...")
    result = translate_text(lang1,lang2,query)
    print(f"Converted text : {result}")
    speak_text(result,lang2)



