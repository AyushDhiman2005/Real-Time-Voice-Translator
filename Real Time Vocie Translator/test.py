from Microphone import mic
from speak_file import speak
from Translation import translate_text
from Speak_2 import speak_text

query = mic()
result = translate_text("hi","en",query)
print("translating...")
print(result)
speak_text(result,'en')


