def translate_text(language1, language2, text):
    from deep_translator import GoogleTranslator

    translated = GoogleTranslator(
        source=language1,
        target=language2
    ).translate(text)

    return translated