

# def speak_text(text, language):
#     from gtts import gTTS
#     from playsound import playsound
#     import os
#     import uuid

#     filename = str(uuid.uuid4()) + ".mp3"

#     tts = gTTS(text=text, lang=language)
#     tts.save(filename)

#     playsound(filename)

#     os.remove(filename)




def speak_text(text, lang):
    from gtts import gTTS
    import pygame
    import uuid
    import os
    filename = f"{uuid.uuid4()}.mp3"

    tts = gTTS(text=text, lang=lang)
    tts.save(filename)

    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        continue

    pygame.mixer.quit()
    os.remove(filename)